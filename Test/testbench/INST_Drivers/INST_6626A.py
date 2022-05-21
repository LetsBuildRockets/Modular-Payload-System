import pyvisa, time, warnings
import numpy as np

class INST_6626A:
    def __init__(self, Addr):
        self.ADDR = Addr
        self.visa_rm = pyvisa.ResourceManager()
        self.inst = self.visa_rm.open_resource('GPIB0::'+str(self.ADDR)+'::INSTR')

    def identify(self):
        self.inst.write("ID?")
        return self.inst.read()

    def enable(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        self.inst.write("OUT {:d} 1".format(channel))

    def disable(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        self.inst.write("OUT {:d} 0".format(channel))

    def setVoltage(self, channel, voltage, vrange=None):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        if voltage < 0:
            raise Exception("Voltage \"{}\" is not valid. Voltage set point must be > 0.".format(voltage))
        elif voltage > 50.5:
            raise Exception("Voltage \"{}\" is not valid. Max voltage is 50.5V".format(voltage))
        if vrange is not None:
            if vrange < voltage:
                raise Exception("Voltage range \"{}\" is not valid. Voltage range must be greater or equal to the output Voltage".format(vrange))
            else:
                self.inst.write("VRSET {:d},{:0.6f}".format(channel, vrange))
        else:
            self.inst.write("VRSET {:d},{:0.6f}".format(channel, voltage))
        self.inst.write("VSET {:d},{:0.6f}".format(channel, voltage))

    def setCurrent(self, channel, current):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        if current < 0:
            raise Exception("Current \"{}\" is not valid. Current set point must be > 0.".format(current))
        elif (channel == 1 or channel == 2) and current > 0.515:
            raise Exception("Current \"{}\" is not valid. Max current for channels 1 and 2 is 0.515A".format(current))
        elif (channel == 3 or channel == 4) and current > 2.060:
            raise Exception("Current \"{}\" is not valid. Max current for channels 1 and 2 is 2.060A".format(current))           
        self.inst.write("IRSET {:d},{:0.6f}".format(channel, current))
        self.inst.write("ISET {:d},{:0.6f}".format(channel, current))

    def getVoltage(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        return float(self.inst.query("VOUT? {:d}".format(channel)))

    def getVoltageSetpoint(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        return float(self.inst.query("VSET? {:d}".format(channel)))
    
    def getCurrentSetpoint(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        return float(self.inst.query("ISET? {:d}".format(channel)))
    
    def getCurrent(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        return float(self.inst.query("IOUT? {:d}".format(channel)))
    
    def getPower(self, channel):
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        return float(self.inst.query("IOUT? {:d}".format(channel)))*float(self.inst.query("VOUT? {:d}".format(channel)))

    def slewOutput(self,channel, endVoltage, slewRate, startVoltage=None, stepsize=0.05):
        if slewRate < 0:
            raise Exception("Slew rate \"{}\" V/s is not valid. Must be > 0.".format(slewRate))
        elif slewRate > 5:
            warnings.warn("Slew rate is > 5 V/s. This will cause the output voltage to be stepped in large steps. Consider a lower slew rate")
        if stepsize < 0.05:
            raise Exception("Slew rate \"{}\" s is not valid. Must be > 0.050.".format(stepsize))
        elif stepsize > 0.25:
            warnings.warn("Step size is > 0.25 s. This will cause the output voltage to be stepped in large steps. Consider a lower step size")
        if channel < 1 or channel > 4:
            raise Exception("Channel {} is not valid. Channel must be 1-4.".format(channel))
        if startVoltage is not None:
            if startVoltage < 0:
                raise Exception("Start Voltage \"{}\" is not valid. Voltage set point must be > 0.".format(startVoltage))
            elif startVoltage > 50.5:
                raise Exception("Start Voltage \"{}\" is not valid. Max voltage is 50.5V".format(startVoltage))
        else:
            startVoltage=self.getVoltageSetpoint(channel)
        if endVoltage < 0:
            raise Exception("End Voltage \"{}\" is not valid. Voltage set point must be > 0.".format(endVoltage))
        elif endVoltage > 50.5:
            raise Exception("End Voltage \"{}\" is not valid. Max voltage is 50.5V".format(endVoltage))

        
        if endVoltage < startVoltage:
            stepsize = -stepsize
            
        self.setVoltage(1,startVoltage,vrange=max(startVoltage,endVoltage))
        start = time.time()
        count = 0
        for V in np.arange(startVoltage, endVoltage, slewRate*stepsize):
            self.setVoltage(1,V,vrange=max(startVoltage,endVoltage))
            count += 1
            while time.time() < start+(count+1)*stepsize:
                pass

        self.setVoltage(1,endVoltage)
