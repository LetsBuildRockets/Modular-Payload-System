import pyvisa, time

class INST_6050A:
    def __init__(self, Addr):
        self.ADDR = Addr
        self.visa_rm = pyvisa.ResourceManager()
        self.inst = self.visa_rm.open_resource('GPIB0::'+str(self.ADDR)+'::INSTR')

    def identify(self):
        self.inst.write("*IDN?")
        return self.inst.read()

    def enable(self, Channel):
        self.inst.write("CHAN "+str(Channel))
        self.inst.write("INPUT ON")

    def disable(self, Channel):
        self.inst.write("CHAN "+str(Channel))
        self.inst.write("INPUT OFF")

    def set(self, Channel, Mode, Value):
        self.inst.write("CHAN "+str(Channel))
        if Mode.upper() == "CC":
            self.inst.write("MODE:CURR")
            self.inst.write("CURR {:0.4f}".format(Value))
        elif Mode.upper() == "CV":
            self.inst.write("MODE:VOLT")
            self.inst.write("VOLT {:0.4f}".format(Value))
        elif Mode.upper() == "CR":
            self.inst.write("MODE:RES")
            self.inst.write("RES {:0.4f}".format(Value))
        
    def getVoltage(self, Channel):
        self.inst.write("CHAN "+str(Channel))
        self.inst.write("MEAS:VOLT?")
        return float(self.inst.read())

    def getCurrent(self, Channel):
        self.inst.write("CHAN "+str(Channel))
        self.inst.write("MEAS:CURR?")
        return float(self.inst.read())
    
    def getPower(self, Channel):
        self.inst.write("CHAN "+str(Channel))
        self.inst.write("MEAS:POW?")
        return float(self.inst.read())
        
