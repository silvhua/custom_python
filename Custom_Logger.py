import logging
from datetime import datetime

class Custom_Logger:
    def __init__(
            self, logger_name='custom_logger', log_file=None, level=logging.DEBUG,
            propagate=False
            ):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)
        self.logger.propagate = propagate
        self.log_messages = []  # New attribute to store log messages

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_log_messages(self):
        return self.log_messages

def test_logger(logger, messages_dict):
    for level in messages_dict:
        message = messages_dict[level]
        if level == 'debug':
            formatted_message = f'DEBUG: {message}'
            logger.logger.debug(message)
        elif level == 'info':
            formatted_message = f'INFO: {message}'
            logger.logger.info(message)
        elif level == 'warning':
            formatted_message = f'WARNING: {message}'
            logger.logger.warning(message)
        elif level == 'error':
            formatted_message = f'ERROR: {message}'
            logger.logger.error(message)
        elif level == 'critical':
            formatted_message = f'CRITICAL: {message}'
            logger.logger.critical(message)
        
        # Format the log message in the specified format and append to the log_messages list
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]  # Adjusted format for microseconds
        log_message = f"{log_time} - {logger.logger.name} - {level.upper()} - {message}"
        logger.log_messages.append(log_message)
