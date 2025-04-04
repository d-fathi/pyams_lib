#-------------------------------------------------------------------------------
# Name:        BJT_characteristics
# Author:      D.fathi
# Created:     30/03/2025
# Copyright:   (c) PyAMS 2025
# Licence:     free GPLv3
#-------------------------------------------------------------------------------

from pyams_lib import circuit
from models import DCCurrent, DCVoltage, NPN, Resistor;

# Define elements
Ib = DCCurrent("0","N02");
V1 = DCVoltage("N01","0");
Q1 = NPN("N01","N04","0");
R1 = Resistor("N02","N04");


# Set component values
Ib.setParams("Idc=1mA ");
V1.setParams("Vdc=10.0V ");
Q1.setParams("Bf=100.0 Br=1.0 Is=1e-16 Nf=1.0 Nr=1.0 Vaf=10 Var=10 Vt=0.025 area=1.0 gmin=1e-12 ");
R1.setParams("R=100");

# Create circuit and add elements
circuit = circuit();
circuit.addElements({'Ib':Ib,'V1':V1,'Q1':Q1,'R1':R1})


# Set outputs for plotting;
circuit.setOutPuts(Q1.Vce,Q1.Ic);
circuit.analysis(mode="dc",param=V1.Vdc,start=0,stop=0.4,step=0.001);


# Execute and plot for different base currents
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

for i in [10,20,30,40]:
    print(f"\nCurrent value of Ib: {i}mA")
    Ib.Idc+=i/1000
    circuit.run();
    Vce,Ic=circuit.getOutPuts()
    label=f"\nCurrent value of Ib: {i}mA"
    plt.plot(Vce, Ic, label=label)


plt.xlabel("Vce(V)")
plt.ylabel("Ic(A)")
plt.title("Circuit Outputs")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

