import unittest
from hamcrest import *
from thermo.lib import *
from thermo.thermo_routes import app
from nose.tools import *
from paste.fixture import TestApp
import json



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))
        self.headers = headers = {"Content-Type": "application/json"}


    # Happy path
    def test_can_list_thermos(self):
        r = self.testApp.get('')
        assert_that(len(json.loads(r.body)['data']), equal_to(2))

    def test_can_show_and_update_individual_thermos(self):
        expected = 'foobar'
        payload = {'data': {'name': expected}}
        r = self.testApp.put(
            '/0',
            params = json.dumps(payload),
            headers = self.headers
        )
        assert_that(json.loads(r.body)['msg'], 'success')

        r = self.testApp.get('/0')
        assert_that(json.loads(r.body)['data']['name'], equal_to(expected))

    def test_can_show_and_update_individual_props_on_individual_thermos(self):
        expected = 'foobar'
        payload = {'value': expected}
        r = self.testApp.put(
            '/0/name',
            params = json.dumps(payload),
            headers = self.headers
        )
        assert_that(json.loads(r.body)['msg'], 'success')

        r = self.testApp.get('/0/name')
        assert_that(json.loads(r.body)['data'], equal_to(expected))


    # Error cases
    def test_updating_non_existant_individual_prop(self):
        expected = {
            'msg': 'property foo can\'t be updated',
            'err': 400
        }
        payload = {'value': 'foo'}
        r = self.testApp.put(
            '/0/foo',
            params = json.dumps(payload),
            headers = self.headers
        )
        assert_that(json.loads(r.body), equal_to(expected))

    def test_quering_non_existant_thermo(self):
        expected = {
            'msg': 'thermometer doesn\'t exist',
            'err': 400
        }
        r = self.testApp.get('/3')
        assert_that(json.loads(r.body), equal_to(expected))

    def test_updating_non_existant_thermo(self):
        expected = {
            'msg': 'thermometer doesn\'t exist',
            'err': 400
        }
        r = self.testApp.put(
            '/4',
            params = json.dumps({}),
            headers = self.headers
        )
        assert_that(json.loads(r.body), equal_to(expected))

    def test_quering_individual_prop_on_existant_thermo(self):
        expected = {
            'msg': 'thermometer doesn\'t exist',
            'err': 400
        }
        r = self.testApp.get('/3/name')
        assert_that(json.loads(r.body), equal_to(expected))

    def test_updating_individual_prop_on_existant_thermo(self):
        expected = {
            'msg': 'thermometer doesn\'t exist',
            'err': 400
        }
        r = self.testApp.put(
            '/3/name',
            params = json.dumps({}),
            headers = self.headers
        )
        assert_that(json.loads(r.body), equal_to(expected))
