# Lesson 6 package. Written by Pakholchuk Nikita
from tax_park_cls import Tax_Park
from cars_cls import CarsFactory
from constants import Constants
from utility import Utility
import logging
import sys

# Logging set up stuff
logger = logging.getLogger('myapp')
Utility.setup_file_logger('./lesson6.log', logger)
Utility.setup_console_logger(logger)

# Body
logger.info('########### START OF THE SCRIPT ###########')
logger.info('Major python verion: ' + str(sys.version_info[0]) + '\n')

Utility.result_prints(logger)
