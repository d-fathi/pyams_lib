#-------------------------------------------------------------------------------
# Name:        RL circuit
# Author:      d. fathi
# Created:     27/03/2025
# Copyright:   (c) PyAMS
#-------------------------------------------------------------------------------

from pyams.lib import circuit
from pyams.models  import Resistor, SquareVoltage, Inductor, C

# Define elements
R1=Resistor("Vin","Vout");
V1=SquareVoltage("Vin","0");
L1=Inductor("Vout","0");


# Set component values
R1.setParams("R=100");
V1.setParams("Va=10V T=100ms");
L1.setParams("L=1H");

# Create circuit and add elements
circuit = circuit();
circuit.addElements({'R1':R1,'V1':V1,'L1':L1})


# Set outputs for plotting;
circuit.setOutPuts("Vin","Vout");


# Perform transient analysi
circuit.analysis(mode="tran",start=0,stop=0.3,step=0.0001);
circuit.run();
circuit.plot();