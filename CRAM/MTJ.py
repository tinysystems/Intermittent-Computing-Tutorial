from params import *

class MTJ:

    def __init__(self, resistance, voltage) -> None:
        self.resistance = resistance
        self.voltage = voltage

    def set_resistance(self, value) -> None:
        self.resistance = value

    def set_voltage(self, value) -> None:
        self.voltage = value

    def get_resistance(self):
        return self.resistance

    def get_voltage(self):
        return self.voltage

    def get_resistance_om(self):
        return RAP if (self.resistance) else RP
