from thermometer import Thermometer, counter, FluxMeter
from errors import InvalidInputError

class Store(object):
    def __init__(self):

        cntr = counter(2)
        meter = FluxMeter(70, 75)
        thermos = {}

        for i in range(2):
            thermo = Thermometer(cntr, meter)
            thermos[thermo.id] = thermo

        self.thermos = thermos

    def find(self, id):
        try:
            return self.thermos[id]
        except:
            raise InvalidInputError('thermometer doesn\'t exist')
        

