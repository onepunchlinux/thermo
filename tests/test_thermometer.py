import unittest
from hamcrest import *
from thermo.thermometer import Thermometer, counter, DeadMeter
from thermo.errors import InvalidInputError

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.default_temp = 70
        self.therm = Thermometer(counter(1), DeadMeter(self.default_temp))

    def test_can_read_id(self):
        assert_that(self.therm.id, equal_to(0))

    def test_can_set_and_read_name(self):
        expected = 'foo'
        self.therm.name = expected
        assert_that(self.therm.name, equal_to(expected))

    def test_can_read_current_temp(self):
        assert_that(self.therm.current_temp, equal_to(self.default_temp))

    def test_can_set_and_read_op_mode(self):
        modes = ['cool', 'heat', 'off']
        for mode in modes:
            self.therm.operating_mode = mode
            assert_that(self.therm.operating_mode, equal_to(mode))

    def test_setting_invalid_op_mode_raises_error(self):
        invalid_mode = 'foo'
        assert_that(calling(setattr).with_args(self.therm, 'operating_mode', invalid_mode),
                    raises(InvalidInputError))

    def test_can_set_and_read_heat_point(self):
        expected = self.therm.heat_point + 1
        self.therm.heat_point = expected
        assert_that(self.therm.heat_point, equal_to(expected))

    def test_can_set_and_read_cool_point(self):
        expected = self.therm.cool_point - 1
        self.therm.cool_point = expected
        assert_that(self.therm.cool_point, equal_to(expected))

    def test_setting_temp_has_lower_bound(self):
        self.therm.cool_point = 20
        self.therm.heat_point = 20
        assert_that(self.therm.cool_point, equal_to(30))
        assert_that(self.therm.heat_point, equal_to(30))

    def test_setting_temp_has_upper_bound(self):
        self.therm.cool_point = 110
        self.therm.heat_point = 110
        assert_that(self.therm.cool_point, equal_to(100))
        assert_that(self.therm.heat_point, equal_to(100))

    def test_can_set_and_read_fan_mode(self):
        modes = ['auto', 'off']
        for mode in modes:
            self.therm.fan_mode = mode
            assert_that(self.therm.fan_mode, equal_to(mode))

    def test_setting_invalid_fan_mode_raises_error(self):
        invalid_mode = 'foo'
        assert_that(calling(setattr).with_args(self.therm, 'fan_mode', invalid_mode),
                    raises(InvalidInputError))
