#-------------------------------------------------------------------------------
# Name:        Voltage Divider Circuit
# Author:      dhiab fathi
# Created:     19/03/2025
# Update:      23/04/2025
# Copyright:   (c) PyAMS 2025
# Licence:     GPLv3
#-------------------------------------------------------------------------------

'''
The voltage divider consists of
A voltage source (V1) providing the input voltage.,
Two resistors (R1 and R2) connected in series.
The output voltage is measured across R2.
'''

#--------------------------------------------------------------------------------
# Step 1: Creat resistor model
#--------------------------------------------------------------------------------


from pyams.lib import model,signal,param
from pyams.lib import voltage,current

#Creat resistor model------------------------------------------------------------
class resistor(model):
    """
    This class implements a Resistor model.
    init(): initals Signals and  Parameters
    analog(): Defines the resistor behavior using Ohm's Law:
                  I = V / R
    """
    def __init__(self, p, n):
        #Signals declarations---------------------------------------------------
        self.V = signal('in',voltage,p,n)
        self.I = signal('out',current,p,n)

        #Parameters declarations------------------------------------------------
        self.R=param(1000.0,'Ω','Resistance')
        self.Pout=param(1000.0,'Ω','Resistance')

    def analog(self):
        """Defines the resistor's current-voltage relationship using Ohm's Law."""
        #Resistor equation-low hom (Ir=Vr/R)------------------------------------
        self.I+=self.V/self.R




#------------------------------------------------------------------------------
# Step2 :Applicated resistor Model in circuit
#-----------------------------------------------------------------------------
from pyams.lib import circuit
from pyams.models import DCVoltage


# Elements of circuit
V1= DCVoltage('n1', '0')    # Voltage source between node 'n1' and ground '0'
R1= resistor('n1', 'n2')   # Resistor R1 between node 'n1' and 'n2'
R2= resistor('n2', '0')    # Resistor R2 between node 'n2' and ground '0'

# Set parameters for the elements
V1.setParams("Vdc=15V")  # Set input voltage to 15V
R1.setParams("R=2kΩ")    # Set R1 to 2kΩ
R2.setParams("R=2kΩ")    # Set R2 to 2kΩ

# Create a circuit instance
myCircuit = circuit()

# Add elements to the circuit
myCircuit.addElements({'V1': V1,'R1': R1, 'R2': R2})


# Perform DC analysis (operating point analysis)
myCircuit.analysis(mode='op')
myCircuit.run()


# print value voltage at node 'n2' and current in 'R1'
myCircuit.print('n2', R1.I)


'''
Output Voltage at node n2: 7.5 V
Output current R1.I: 3.75 mA
'''


