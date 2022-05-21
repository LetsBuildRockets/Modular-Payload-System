import pyvisa, time

class INST_4388A:
    
    OPEN = 1
    CLOSED = 0
    
    def __init__(self, Addr):
        self.ADDR = Addr
        self.visa_rm = pyvisa.ResourceManager()
        self.inst = self.visa_rm.open_resource('GPIB0::'+str(self.ADDR)+'::INSTR', write_termination='\r\n', read_termination='\r\n')
        self.inst.control_ren(1)

    def identify(self):
        response = ""
        self.inst.write("ID?")
        response += self.inst.read()
        for n in range(1,6):
            self.inst.write("CTYPE {}".format(n))
            response += ', ' + self.inst.read()
        
        return response
        
    def setState(self, relay_lst, state):
        if len(relay_lst) > 0:
            relay_lst_str = "{}".format(relay_lst[0])
            for n in range(1,len(relay_lst)):
                relay_lst_str += ", {}".format(relay_lst[n])
            if state == self.OPEN:
                self.inst.write("OPEN {}".format(relay_lst_str))
            elif state == self.CLOSED:
                self.inst.write("CLOSE {}".format(relay_lst_str))
            else:
                raise Exception("State \"{}\" is not valid. Acceptable sates are 0 (open) or 1 (close).".format(state))   
        else:
            raise Exception("relay list must be > 0 in length")
        
    def getState(self, relay):
        self.inst.write("VIEW {}".format(relay))
        return int(self.inst.read()[-1])
    
    def reset(self, card_lst=[]):
        if len(card_lst) > 0:
            card_lst_str = "{}".format(card_lst[0])
            for n in range(1,len(card_lst)):
                card_lst_str += ", {}".format(card_lst[n])
            self.inst.write("CRESET {}".format(card_lst_str))
        else:
            card_lst = [1,2,3,4,5]
            self.reset(card_lst)
            
                