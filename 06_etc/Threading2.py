import logging
import threading


def get_logger():
    logger = logging.getLogger("Thread Example")
    logger.setLevel(logging.DEBUG)
    fh = logging.StreamHandler()
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def execute(number, logger):
    logger.debug('execute function executing')
    result = number * 2
    logger.debug('execute function ended with: {}'.format(result))


if __name__ == '__main__':
    logger = get_logger()
    for i, name in enumerate(['Kim', 'Lee', 'Park', 'Cho', 'Hong']):
        my_thread = threading.Thread(target=execute, name=name, args=(i, logger))
        my_thread.start()
