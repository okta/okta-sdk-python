import logging


LOG_FORMAT = \
    '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s'


def setup_logging(log_level=logging.INFO):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    log_formatter = logging.Formatter(LOG_FORMAT)
    stream_handler.setFormatter(log_formatter)

    logger = logging.getLogger('okta-sdk-python')
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    # disable logger by default
    logger.disabled = True
