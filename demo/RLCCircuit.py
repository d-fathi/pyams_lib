#-------------------------------------------------------------------------------
# Name:        Series RLC Circuit
# Author:      d. fathi
# Created:     26/03/2025
# Copyright:   (c) PyAMS
#-------------------------------------------------------------------------------


from pyams_lib import circuit
from models import Resistor, DCVoltage, Capacitor, Inductor

# Define elements
V1=DCVoltage("Vin","0");
R1=Resistor("Vin","Vs");
L1=Inductor("Vs","Vout");
C1=Capacitor("Vout","0");


# Set component values
R1.setParams("R=10");
V1.setParams("Vdc=10V");
L1.setParams("L1=1mH");
C1.setParams("C=1uF");

# Create circuit and add elements
circuit = circuit();
circuit.addElements({'V1':V1, 'R1':R1,'L1':L1,'C1':C1})




# Set outputs for plotting;
circuit.analysis(mode="tran",start=0,stop=1e-3,step=1e-6);

# Perform transient analysi
circuit.setOutPuts("Vout",R1.I);
circuit.run();
circuit.plot();
