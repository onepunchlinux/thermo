import web
import json
import inflection
from thermometer import ThermometerEncoder
from errors import InvalidInputError
from store import Store

urls = (
    '', 'Thermometers',
    '/([0-9]+)', 'Thermometer',
    '/([0-9]+)/([a-zA-Z0-9]+)', 'ThermometerFields'
)

store = Store()

class Thermometers:
    def GET(self):
        return json.dumps(
            {'data': store.thermos.values()},
            cls=ThermometerEncoder
        )


class Thermometer:
    def GET(self, thermoId):
        try:
            thermo = store.find(int(thermoId))
            res = {'data': thermo}
        except InvalidInputError as e:
            res = bad_input_err(e.message)

        return json.dumps(res, cls=ThermometerEncoder)

    def PUT(self, thermoId):
        try:
            thermo = store.find(int(thermoId))
            body = json.loads(web.data())
            res = {'msg': 'success'}
            thermo.merge(body)

        except InvalidInputError as e:
            res = bad_input_err(e.message)

        return json.dumps(res)


class ThermometerFields:
    def GET(self, thermoId, field):
        try:
            thermo = store.find(int(thermoId))
            res = {'data': thermo[field]}
        except InvalidInputError as e:
            res = bad_input_err(e.message)

        return json.dumps(res)

    def PUT(self, thermoId, field):
        try:
            thermo = store.find(int(thermoId))
            body = json.loads(web.data())

            res = {'msg': 'success'}
            if 'value' in body:
                    thermo[field] = body['value']
            else:
                res = bad_input_err('missing value field')
                
        except InvalidInputError as e:
            res = bad_input_err(e.message)

        return json.dumps(res)
                

def bad_input_err(msg):
    return {
        'err': 400,
        'msg': msg
    }

def global_headers(handler):
    web.header('Content-Type', 'application/json')
    return handler()

app = web.application(urls, locals())
app.add_processor(global_headers)
