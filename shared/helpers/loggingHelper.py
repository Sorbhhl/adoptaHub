import logging

class LogginHelper:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.level = logging.DEBUG
        self.logger.info("LoggingHelper initialized")