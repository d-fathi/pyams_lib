#-------------------------------------------------------------------------------
# Name:        CCVS
# Author:      d.fathi
# Created:     10/03/2017
# Modified:    24/01/2020
# Copyright:   (c) PyAMS
# Licence:     free  "GPLv3"
#-------------------------------------------------------------------------------

from PyAMS import model,signal,param
from  electrical  import voltage,current


#Current-controlled voltage source Model----------------------------------------
class CCVS(model):
     def __init__(self,p1,n1,p2,n2):
        #Signals declarations---------------------------------------------------
         self.Iin= signal('in',current,p1,n1)
         self.Vout= signal('out',voltage,p2,n2)
        #Parameter declarations-------------------------------------------------
         self.G=param(1.0,'Ohm','Gain multiplier')

     def analog(self):
         self.Vout+=self.G*self.Iin


