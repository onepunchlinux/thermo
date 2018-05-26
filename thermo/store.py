from thermometer import Thermometer, counter, FluxMeter
class Store(object):
    def __init__(self):

        cntr = counter(2)
        meter = FluxMeter(70, 75)
        thermos = {}

        for i in range(2):
            thermo = Thermometer(cntr, meter)
            thermos[thermo.id] = thermo

        self.thermos = thermos
