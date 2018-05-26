import web
import json
import inflection
from thermometer import ThermometerEncoder
from errors import InvalidInputError
from store import Store

urls = (
    '', 'Thermometers',
    '/([0-0]+)', 'Thermometer',
    '/([0-9]+)/([a-zA-Z0-9]+)', 'ThermometerFields'
)

store = Store()

class Thermometers:
    def GET(self):
        return json.dumps({'data': store.thermos}, cls=ThermometerEncoder)


class Thermometer:
    def GET(self, thermoId):
        thermo = store.thermos.get(int(thermoId))

        return json.dumps(thermo, cls=ThermometerEncoder)

    def PUT(self, thermoId):
        thermo = store.thermos.get(int(thermoId))
        body = json.loads(web.data())
        if 'data' in body:
            thermo.merge(body['data'])
        elif 'key' in body and 'value' in body:
            thermo[body['key']] = body['value']

        return json.dumps({ 'msg': 'success' })


class ThermometerFields:
    def GET(self, thermoId, field):
        thermo = store.thermos.get(int(thermoId))
        return json.dumps({'data': thermo[field]})

app = web.application(urls, locals())
