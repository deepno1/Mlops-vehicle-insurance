import logging
import os
from from_root import from_root
from datetime import datetime
from logging.handlers import RotatingFileHandler

log_dir = 'logs'
log_dir_path = os.path.join(from_root(),log_dir)
os.makedirs(log_dir_path,exist_ok = True)

log_file = '{}.log'.format(datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))
log_file_path = os.path.join(log_dir_path,log_file)

def configure_logger():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(log_file_path,maxBytes= 5 * 1024 * 1024,backupCount= 3)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


configure_logger()
