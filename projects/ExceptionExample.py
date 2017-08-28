# _*_coding=utf-8_*_
# __author__='xj'
"""exception example"""

import logging


class DealError(object):
    @staticmethod
    def test_exception(i):
        try:
            j = 100 / i
        except ZeroDivisionError as e:
            print(e)
            logging.exception(e)
        except ValueError:
            print('ValueError')
        else:
            print('No error')
        finally:
            print('End')


def traceback_example(s):
    return 10 / int(s)


def call(s):
    return traceback_example(s) * 2


def foo(i):
    if i == 0:
        raise TypeError()
    return 10 / i


def bar():
    try:
        foo(0)
    except TypeError as e:
        raise
    print('End')

# call('s')
# DealError.test_exception(0)
bar()
