import logging
from datetime import datetime
from silvhua import *

class Custom_Logger:
    def __init__(
            self, logger_name='custom_logger', level=logging.DEBUG,
            propagate=False, log_file=None, log_path=r'C:\Users\silvh\OneDrive\lighthouse\custom_python\files\logger_files'
            ):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)
        self.logger.propagate = propagate
        self.log_messages = []  # New attribute to store log messages
        log_path = convert_windows_path(log_path)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if log_file:
            file_handler = logging.FileHandler(f'{log_path}/{log_file}')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def save_log_messages(self, level, message):
        # Format the log message in the specified format and append to the log_messages list
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]  # Adjusted format for microseconds
        log_message = f"{log_time} - {self.logger.name} - {level.upper()} - {message}"
        self.log_messages.append(log_message)

    def get_log_messages(self):
        return self.log_messages
    
    def debug(self, message, save=False):
        self.logger.debug(message)
        if save:
            self.save_log_messages('debug', message)

    def info(self, message, save=False):
        self.logger.info(message)
        if save:
            self.save_log_messages('info', message)

    def warning(self, message, save=False):
        self.logger.warning(message)
        if save:
            self.save_log_messages('warning', message)

    def error(self, message, save=False):
        self.logger.error(message)
        if save:
            self.save_log_messages('error', message)

    def critical(self, message, save=False):
        self.logger.critical(message)
        if save:
            self.save_log_messages('critical', message)
            
def test_logger(logger, messages_dict, save=True):
    for level in messages_dict:
        message = messages_dict[level]
        if level == 'debug':
            logger.debug(message, save=save)
        elif level == 'info':
            logger.info(message, save=save)
        elif level == 'warning':
            logger.warning(message, save=save)
        elif level == 'error':
            logger.error(message, save=save)
        elif level == 'critical':
            logger.critical(message, save=save)
