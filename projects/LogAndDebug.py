# _*_coding=utf-8_*_
# __author__='xj'
"""log and debug example"""

import logging

logging.basicConfig(level=logging.INFO)


def print_example():
    n = 0
    print('n>>>%d' % n)
    return 10 / n


def assert_example():
    n = 0
    assert n != 0
    return 10 / n


def log_example():
    n = 0
    logging.info('n>>>%d' % n)
    return 10 / n


# print_example()
assert_example()