import shutil

from openhtf.plugs import BasePlug
from INST_Drivers.INST_6626A import INST_6626A

class PSU(BasePlug):
    def __init__(self):
        super().__init__()
        self.psu = INST_6626A(3)
    
