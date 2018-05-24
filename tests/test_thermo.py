import unittest
from hamcrest import *
from thermo.lib import *

class TestStringMethods(unittest.TestCase):

    def test_foo(self):
        assert_that(foo(), 'foobar')
