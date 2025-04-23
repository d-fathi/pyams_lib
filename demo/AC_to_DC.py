#-------------------------------------------------------------------------------
# Name:        AC to DC converter
# Author:      d.fathi
# Created:     04/04/2025
# Copyright:   (c) pyams 2025
# Licence:     free GPlv3
#-------------------------------------------------------------------------------



from pyams.lib import circuit
from pyams.models  import DiodeBridge, SinVoltage,Resistor,Capacitor, Transformer

# Define elements
D1 = DiodeBridge("sec","Out","N05","0");
V1 = SinVoltage("In","0");
R1 = Resistor("In","N01");
R2 = Resistor("Out","0");
C1 = Capacitor("Out","0");
T2 = Transformer("N01","0","sec","N05");

# Set component values
V1.setParams("Va=120V Fr=60Hz ");
R1.setParams("R=10mΩ");
R2.setParams("R=1KΩ");
C1.setParams("C=0.1mF ");
T2.setParams("Lp=1H Ls=1H M=1H");

# Create circuit and add elements
circuit = circuit();
circuit.addElements({'D1':D1,'V1':V1,'R1':R1,'R2':R2,'C1':C1,'T2':T2})


# Set outputs for plotting;
circuit.setOutPuts("In","Out");


# Perform transient analysis
circuit.analysis(mode="tran",start=0,stop=0.1,step=0.0001);
circuit.run();
circuit.plot();