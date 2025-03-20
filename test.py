#-------------------------------------------------------------------------------
# Name:        Voltage Divider Circuit
# Author:      dhiab fathi
# Created:     19/03/2025
# Copyright:   (c) PyAMS 2025
# Licence:     GPLv3
#-------------------------------------------------------------------------------

'''
test 1:
The voltage divider consists of
A voltage source (V1) providing the input voltage.,
Two resistors (R1 and R2) connected in series.
The output voltage is measured across R2.
'''


from pyams_lib import circuit
from models.Basic.Resistor  import Resistor
from models.Source.DCVoltage import DCVoltage

# Create a circuit instance
myCircuit = circuit()

# Add elements to the circuit
myCircuit.addElements({
    'V1': DCVoltage('1', '0'),  # Voltage source between node '1' and ground '0'
    'R1': Resistor('1', '2'),   # Resistor R1 between node '1' and '2'
    'R2': Resistor('2', '0')    # Resistor R2 between node '2' and ground '0'
})

# Set parameters for the elements
myCircuit.elem['V1'].setParams("Vdc=10V")  # Set input voltage to 10V
myCircuit.elem['R1'].setParams("R=2kΩ")  # Set R1 to 2kΩ
myCircuit.elem['R2'].setParams("R=2kΩ")  # Set R2 to 2kΩ

# Set outputs for plotting (output voltage at node '2')
myCircuit.setOutPuts('2')

# Perform DC analysis (operating point analysis)
myCircuit.analysis(mode='op')
myCircuit.run()
print(myCircuit.elem['V1'].V.value)

# Print the output voltage
output_voltage = myCircuit.x[myCircuit.nodes.index('2') - 1]  # Get voltage at node '2'
print(f"Output Voltage at node '2': {output_voltage:.2f} V")