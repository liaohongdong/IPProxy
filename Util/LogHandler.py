import os
import logging
import Print

from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')


class LogHandler(logging.Logger):
    pass


if __name__ == "__main__":
    # Print.out(os.path.abspath(__file__))
    # Print.out(os.path.dirname(os.path.abspath(__file__)))
    Print.out(LOG_PATH)
    Print.out(CURRENT_PATH)
    Print.out(ROOT_PATH)
