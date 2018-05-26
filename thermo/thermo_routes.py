import web
import json
import inflection
from thermometer import ThermometerEncoder
from errors import InvalidInputError
from store import Store

urls = (
    '/', 'Thermometers',
    '/(.+)', 'ThermometerById'
)

store = Store()

class Thermometers:
    def GET(self):
        return json.dumps(store.thermos, cls=ThermometerEncoder)

class ThermometerById:
    def GET(self, thermoId):
        thermo = store.thermos.get(int(thermoId))

        return json.dumps(thermo, cls=ThermometerEncoder)

    def PUT(self, thermoId):
        thermo = store.thermos.get(int(thermoId))
        data = json.loads(web.data())

        writable_fields = [
            'name',
            'operatingMode',
            'coolPoint',
            'heatPoint',
            'fanMode'
        ]

        for field in writable_fields:
            update_or_not(thermo, inflection.underscore(field), data.get(field))

        return json.dumps({ 'msg': 'success' })


def update_or_not(obj, obj_key, val):
    if val != None:
        setattr(obj, obj_key, val)
    return

app = web.application(urls, locals())
