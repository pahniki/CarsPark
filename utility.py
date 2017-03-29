from tax_park_cls import Tax_Park
from cars_cls import CarsFactory
from constants import Constants
import logging


class Utility:
    @staticmethod
    def setup_file_logger(filename, logger):
        """ Sets file logger properties """
        file_handler = logging.FileHandler(filename)
        formatter = logging.Formatter('%(name)-20s %(levelname)-8s %(message)s')
        file_handler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    @staticmethod
    def setup_console_logger(logger):
        """ Sets console logger properties """
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        console.setFormatter(formatter)
        logger.addHandler(console)

    # @staticmethod
    # def wait_cars(car_list):
    #     while any(car.isAlive() for car in car_list):
    #         pass

    @staticmethod
    def result_prints(logger):
        """ Function that controls the main page log output. """
        CarsFactory.self_create(50)
        Evil_Park = Tax_Park(CarsFactory.array)
        # CarsFactory.self_create(60)
        # Evil_Park.add_new_cars(CarsFactory.array)
        logger.info('Preparing cars to send them into far away travel!!!')
        Evil_Park.drive_them_all(55000, 285000)
        Evil_Park.wait_cars()
        logger.info('\n##################################################')
        logger.info('List of all cars registred in park: \n')
        Evil_Park.show_cars()
        logger.info('\n##################################################')
        logger.info('\nTotal value of all cars is : ' + str(Evil_Park.cars_value_sum()))
        logger.info('Total credits of all cars is : ' + str(Evil_Park.credit_sum()))
        logger.info('\n##################################################')
        logger.info('List of sorted gasoline cars: \n')
        Evil_Park.pent_sort_list()
        logger.info('\n##################################################')
        logger.info('List of sorted diesel cars: \n')
        Evil_Park.dies_sort_list()
        logger.info('\n THE END')
