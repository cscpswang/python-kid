# _*_coding=utf-8_*_
# __author__='xj'
"""example for unit test"""

import unittest


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict have no object %s" % key)


class DictUnitTest(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='2')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, '2')
        self.assertIsInstance(d, Dict)

    def test_key(self):
        d = Dict()
        d['a'] = 1
        self.assertEquals(d['a'], 1)

    def test_attr(self):
        d = Dict()
        d.a = 1
        self.assertEquals(d.a, 1)

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
