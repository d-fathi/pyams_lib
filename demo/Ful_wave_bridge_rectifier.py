#-------------------------------------------------------------------------------
# Name:        Ful wave bridge rectifier
# Author:      d. fathi
# Created:     28/03/2025
# Copyright:   (c) PyAMS
# Licence:     free  "GPLv3"
#-------------------------------------------------------------------------------


from pyams_lib import circuit
from models import Resistor, SinVoltage, DiodeBridge

# Define elements
R1 = Resistor("Vout", "0")
Vin = SinVoltage("N04", "N03")
D1 = DiodeBridge("N04", "Vout", "N03", "0")

# Set elements Parameters
R1.setParams("R=1KΩ")
Vin.setParams("Fr=2Hz Ph=0.0 Va=10V Voff=0.0")
D1.setParams("Iss=1pA Vt=25mV")

# Create Circuit and Add Elements
circuit = circuit()
circuit.addElements({"R1": R1, "Vin": Vin, "D1": D1})

# Set Outputs for Plotting
circuit.setOutPuts(Vin.V, "Vout")

# Perform Transient Analysis
circuit.analysis(mode="tran", start=0, stop=10, step=0.001)
circuit.run()
circuit.plot()