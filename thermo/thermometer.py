import random
import json
from errors import InvalidInputError

class Thermometer(object):
    def __init__(self, counter, meter):
        init_id = counter.next()
        self.id = init_id
        self.name = 'thermometer' + str(init_id)
        self.current_temp = meter.temp
        self.operating_mode = 'cool'
        self.cool_point = 72
        self.heat_point = 72
        self.fan_mode = 'auto'

        self.writable_fields = [
            'name',
            'operating_mode',
            'cool_point',
            'heat_point',
            'fan_mode'
        ]

    def __getitem__(self, field):
        if field == 'id':
            return self.id
        elif field == 'name':
            return self.name
        elif field == 'current_temp':
            return self.current_temp
        elif field == 'operating_mode':
            return self.operating_mode
        elif field == 'cool_point':
            return self.cool_point
        elif field == 'heat_point':
            return self.heat_point
        elif field == 'fan_mode':
            return self.fan_mode

    def __setitem__(self, field, val):
        if field == 'name':
            self.name = val
        elif field == 'operating_mode':
            self.operating_mode = val
        elif field == 'cool_point':
            self.cool_point = val
        elif field == 'heat_point':
            self.heat_point = val
        elif field == 'fan_mode':
            self.fan_mode = val

    def merge(self, obj):
        for field in writable_fields:
            val = obj.get(inflection.camelize(field, False))
            if val != None:
                thermo[field] = val
        

    @property
    def operating_mode(self):
        return self.__operating_mode

    @operating_mode.setter
    def operating_mode(self, mode):
        valid_modes = ['cool', 'heat', 'off']
        if mode in valid_modes:
            self.__operating_mode = mode
        else:
            raise InvalidInputError('operating mode must be one of ' + " ".join(valid_modes))

    @property
    def cool_point(self):
        return self.__cool_point

    @cool_point.setter
    def cool_point(self, temp):
        self.__cool_point = min(100, max(30, temp))

    @property
    def heat_point(self):
        return self.__heat_point

    @heat_point.setter
    def heat_point(self, temp):
        self.__heat_point = min(100, max(30, temp))

    @property
    def fan_mode(self):
        return self.__fan_mode

    @fan_mode.setter
    def fan_mode(self, mode):
        valid_modes = ['auto', 'off']
        if mode in valid_modes:
            self.__fan_mode = mode
        else:
            raise InvalidInputError('fan mode must be one of ' + " ".join(valid_modes))


class ThermometerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Thermometer):
            return {
                'id': obj.id,
                'name': obj.name,
                'currentTemp': obj.current_temp,
                'operatingMode': obj.operating_mode,
                'coolPoint': obj.cool_point,
                'heatPoint': obj.heat_point,
                'fanMode': obj.fan_mode
            }
        else:
            return super(ThermometerEncoder, self).default(obj)
            


class DeadMeter:
    def __init__(self, t):
        self.temp = t

    @property
    def temp(self):
        return self.__temp


class CrazyMeter:
    @property
    def temp(self):
        return random.randint(1,120)


class FluxMeter:
    def __init__(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    @property
    def temp(self):
        return random.randint(self.min_temp, self.max_temp)


def counter(n):
    for x in xrange(n):
        yield x
