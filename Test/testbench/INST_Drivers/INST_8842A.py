import pyvisa, time

class INST_8842A:
    def __init__(self, Addr):
        self.ADDR = Addr
        self.visa_rm = pyvisa.ResourceManager()
        self.inst = self.visa_rm.open_resource('GPIB0::'+str(self.ADDR)+'::INSTR', write_termination='\r\n', read_termination='\r\n')
        self.inst.control_ren(1)

    def identify(self):
        self.inst.write("*IDN?")
        return self.inst.read()

    def getVoltage(self, speed='MEDIUM'):
        self.inst.write('F1')
        self.inst.write('R0')
        if speed.upper() == 'SLOW':
            self.inst.write('S0')
        elif speed.upper() == 'MEDIUM':
            self.inst.write('S1')
        elif speed.upper() == 'FAST':
            self.inst.write('S2')
        else:
            raise Exception("Measurement speed \"{}\" is not valid. Acceptable speeds are SLOW, MEDIUM, or FAST.".format(speed))   
        
        return float(self.inst.read())

    
    def getCurrent(self, speed='MEDIUM'):
        self.inst.write('F5')
        self.inst.write('R0')
        if speed.upper() == 'SLOW':
            self.inst.write('S0')
        elif speed.upper() == 'MEDIUM':
            self.inst.write('S1')
        elif speed.upper() == 'FAST':
            self.inst.write('S2')
        else:
            raise Exception("Measurement speed \"{}\" is not valid. Acceptable speeds are SLOW, MEDIUM, or FAST.".format(speed))   
        
        return float(self.inst.read())
    
        
