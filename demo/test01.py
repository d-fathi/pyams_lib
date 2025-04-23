



from pyams.lib import time,circuit
from pyams.models  import Resistor, SinVoltage, Diode;

R1 = Resistor("Out","0");
V1 = SinVoltage("In","0");
D1 = Diode("In","Out");

R1.setParams("R=1KΩ ");
V1.setParams("Va=10V Fr=2Hz");

circuit = circuit();
circuit.addElements({'R1':R1,'V1':V1,'D1':D1})


# Set outputs for plotting;
circuit.setOutPuts("In","Out");


# Set outputs for plotting;
circuit.analysis(mode="tran",start=0,stop=2,step=0.001);
circuit.run();
circuit.plot();