# Script with Tax_Park class.

from random import randint as rand
import logging

logger = logging.getLogger('myapp.tax_park_cls')


class Tax_Park:
    def __init__(self, cars_array=[]):
        """  __Init__ Receives cars array as argument """
        self.cars_list = list()
        self.cars_list.extend(cars_array)

    def add_new_cars(self, cars_array):
        """ Adds new car list to already existed """
        self.cars_list.extend(cars_array)

    def drive_them_all(self, start, finish):
        """ Drive all vulnerable cars in the Tax park """
        for car in self:
            car.drive_in_thread(rand(start, finish))

    def cars_value_sum(self):
        tot_sum = sum([car.value for car in self])
        return tot_sum

    def credit_sum(self):
        cred_sum = sum([car.value for car in self if car.value < 0])
        return cred_sum

    def pent_sort_list(self):
        """ Produce a 'pentol' only car list and sort it by the vlaue """
        pent_sort = [car for car in self if car.is_pentol]
        # Since cars value that left represents the distance that a car will be able to travel
        pent_sort.sort(key=lambda car: car.value)
        for car in pent_sort:
            logger.info(car)
        return pent_sort

    def dies_sort_list(self):
        """ Produce a 'diesel' only car list and sort it by the vlaue """
        dies_sort = [car for car in self if car.is_diesel]
        dies_sort.sort(key=lambda car: car.value)
        for car in dies_sort:
            logger.info(car)
        return dies_sort

    def wait_cars(self):
        while any(car.isAlive() for car in self.cars_list):
            pass

    def show_cars(self):
        for car in self:
            logger.info(car)

    def __iter__(self):
        for car in self.cars_list:
            yield car