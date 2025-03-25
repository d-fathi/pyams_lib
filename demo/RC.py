#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dhiab fathi
#
# Created:     24/03/2025
# Copyright:   (c) dhiab fathi 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pyams_lib import circuit
from models import Resistor, SquareVoltage, Capacitor

#------------------------------------------------------------------
R1=Resistor("Vin","Vout");
V1=SquareVoltage("Vin","0");
C1=Capacitor("Vout","0");
#------------------------------------------------------------------
R1.setParams("R=100");
V1.setParams("Va=10V T=200ms");
C1.setParams("C=100uF");

#------------------------------------------------------------------
circuit = circuit();
circuit.addElements({'R1':R1,'V1':V1,'C1':C1})


# Set outputs for plotting;
circuit.setOutPuts("Vin","Vout");


# Set outputs for plotting;
circuit.analysis(mode="tran",start=0,stop=1,step=0.001);
circuit.run();
circuit.plot();