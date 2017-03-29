# Engine and Fuel classes.
from constants import Constants
import logging

logger = logging.getLogger('myapp.engine&fuel_cls')


class Engine:
    """ Represents the engine of a car. Receives Fuel obj as attribute."""

    def __init__(self, fu_name):
        self.fuel = Fuel(fu_name)
        self.cost = 3000  # $

    def switch(self):
        """ Switching Fuel type for pentol car. """
        if (self.fuel.type is 'pentol_92'):
            # logger.info('#We\'ve switched the fuel type to A95')
            self.fuel = Fuel('pentol_95')

    def degrade(self):
        """ Engine degradation. Fuel consumption increase 1% every 1.000km """
        self.fuel.consum *= Constants.burn_incr  # increases fuel consumption every 1000km by 1%


class Fuel():
    def __init__(self, fu_type):
        self.type = fu_type
        self.__set_properties()

    def __set_properties(self):
        """ Sets fuel properties depending on its type."""
        if (self.type is 'diesel'):
            self.consum = 6  # 6 l/100km
            self.price = 1.8  # $ per litr
            self.re_point = 150000  # km
        else:
            self.consum = 8  # 8 l/100km
            if (self.type == 'pentol_95'):
                self.price = 2.4  # $
            else:
                self.type = 'pentol_92'
                self.price = 2.2  # $ per litr AI92
            self.re_point = 100000  # km
