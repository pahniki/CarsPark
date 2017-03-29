# Lesson 6 homework script. Written by Pakholchuk Nikita
from engine_cls import Engine, Fuel
import logging
from constants import Constants
from threading import Thread

logger = logging.getLogger('myapp.cars_cls')


class CarsFactory(Thread):
    """CarsFactory class. Creates a cars in it's list to pass it to other objects"""
    NEW_CAR_PRICE = 10000
    MOVE_STEP = 1  # km. step that is being used for calculations(could also use 10 but it will lower that accurancy)
    item_index = 1  # Unique index for every car ever created
    array = []

    def __init__(self, engine):
        Thread.__init__(self)
        CarsFactory.array.append(self)
        self.numer = CarsFactory.item_index
        CarsFactory.item_index += 1  # Unique index increase
        self.engine = engine
        self.value = CarsFactory.NEW_CAR_PRICE
        self.__set_properties()
        self.__tachograph = 0
        self._deg_step = 1000  # 1000km will need that for calculations
        self._hund = 100  # 100km
        self.info_msg = '\n'  # Will comntain info about car travel

    def __set_properties(self):
        """ Set's starting set up for each car """
        self.__dist_left = self.engine.fuel.re_point
        # Set tank volume
        if (not (CarsFactory.item_index - 1) % 5):
            self.__tank = 75  # litrs
        else:
            self.__tank = 60  # litrs
        self.__fuel_left = self.__tank
        self.tank_cost = self.engine.fuel.price * self.__tank

    def drive(self, final_dist):
        """ Method that moves the car and calculates it's modification during its travel. """
        passed_dist = 0
        drive_cost = 0
        fuel_cost = 0
        tank_count = 0
        step = CarsFactory.MOVE_STEP
        self.counter = self.__tachograph % self._deg_step
        self.info_msg += ('A Car {} travel info:\n'.format(self.numer))
        while (passed_dist < final_dist):
            self.__tachograph += step
            drive_cost += self.__repair_works(step)
            tmp_fuel_cost, tmp_tank_count = self.__fuel_burn(step)
            tank_count += tmp_tank_count
            fuel_cost += tmp_fuel_cost
            passed_dist += step

        drive_cost += fuel_cost
        self.value -= drive_cost
        self.info_msg += ('Car {} moved {} km. '
                          'Car is worth {} $. '
                          'Last drive cost: {} $. '
                          'Fueled {} times. Cost: {}. '
                          '{} km left untill capital repair\n'.format(self.numer, final_dist, \
                                                                    self.value, drive_cost, tank_count, fuel_cost,
                                                                    self.__dist_left))
        logger.info(self.info_msg)

    def __repair_works(self, step):
        """ Calculates the price of summarised repair works during the travel """
        drive_price = 0
        repair_count = 0
        self.__dist_left -= step
        if (not self.__dist_left):
            self.__dist_left = self.engine.fuel.re_point
            repair_count += 1
        # Engine reinstall
        drive_price += self.engine_reinstall()
        # Change fuel type after 50.000km for pentol
        if (self.__tachograph == Constants.Pentol.switch_point):
            self.engine.switch()

        drive_price += self.rep_cost(repair_count)
        return drive_price

    def __fuel_burn(self, step):
        """ Calculates the price of summarised fuel burned during the travel """
        tank_count = 0
        lit_in_step = (step / Constants.hund) * self.engine.fuel.consum
        self.__fuel_left -= lit_in_step
        self.__degradation(step)
        if (self.__fuel_left <= 0):
            tank_count += 1
            self.__fuel_left = self.__tank
        fuel_cost = tank_count * self.tank_cost
        return (int(fuel_cost), int(tank_count))

    def __degradation(self, step):
        """ Sets the degradation of a car for every 1.000 km """
        if (not (self.counter % Constants.deg_step)):
            self.engine.degrade()
            self.value = self.value_lower(self.value)
        self.counter += step

    def engine_reinstall(self):
        if (not (self.__tachograph % self.engine.fuel.re_point)):
            self.engine = Engine(self.engine.fuel.type)
            self.info_msg+= ('#The engine was reinstalled.\n')
            return self.engine.cost
        else:
            return 0

    def value_lower(self, value):
        """ Lowers the value of a car """
        if (self.engine.fuel.type == 'diesel'):
            value -= Constants.Diesel.value_lower
        else:
            value -= Constants.Pentol.value_lower
        return (value)

    def rep_cost(self, count):
        """ Calculates the repair cost for current type of engine """
        if (self.engine.fuel.type == 'diesel'):
            value = count * Constants.Diesel.repare_cost
        else:
            value = count * Constants.Pentol.repare_cost
        return value

    @property
    def is_pentol(self):
        return self.engine.fuel.type.startswith('pentol')

    @property
    def is_diesel(self):
        return self.engine.fuel.type == 'diesel'

    def __repr__(self):
        return ('I am a car {}. '
                'I\'m a {} l {} type. '
                'I\'ve travaled: {} km. '
                'My current price is: {} $.'.format(self.numer, self.__tank, self.engine.fuel.type,
                                                          self.__tachograph, self.value))

    def drive_in_thread(self, dist):
        self.info_msg +=('Drive in thread\n')
        self.dist_for_run = dist
        self.start()

    def run(self, dist=0):
        self.drive(self.dist_for_run)

    @classmethod
    def self_create(cls, amount):
        """ Creates a list of [pent:pent:dies...] cars."""
        CarsFactory.array.clear()
        for i in range(amount):
            if (not CarsFactory.item_index % 3):
                CarsFactory(Engine('diesel'))
            else:
                CarsFactory(Engine('pentol'))
