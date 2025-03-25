#-------------------------------------------------------------------------------
# Name:        Voltage Divider Circuit
# Author:      dhiab fathi
# Created:     19/03/2025
# Copyright:   (c) PyAMS 2025
# Licence:     GPLv3
#-------------------------------------------------------------------------------

'''
The voltage divider consists of
A voltage source (V1) providing the input voltage.,
Two resistors (R1 and R2) connected in series.
The output voltage is measured across R2.
'''


from pyams_lib import circuit
from models  import Resistor, DCVoltage


# Elements of circuit
V1= DCVoltage('n1', '0')    # Voltage source between node 'n1' and ground '0'
R1= Resistor('n1', 'n2')   # Resistor R1 between node 'n1' and 'n2'
R2= Resistor('n2', '0')    # Resistor R2 between node 'n2' and ground '0'

# Set parameters for the elements
V1.setParams("Vdc=10V")  # Set input voltage to 10V
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


