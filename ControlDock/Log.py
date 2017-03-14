import logging


class Log:
    """Handle log writing."""

    def __init__(self, level):
        """Attributes:
                level (string): Use logging constants to define level."""
        self.__level = level

    def write(self, message):
        """Writes a log record at logs/appliction.log

            Attributes:
                message (string): Log message."""
        logger = logging.getLogger('error')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler = logging.FileHandler('./logs/application.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.log(self.__level, message)
