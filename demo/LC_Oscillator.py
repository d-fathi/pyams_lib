#-------------------------------------------------------------------------------
# Name:       LC Oscillator
# Author:      dhiab fathi
# Created:     24/03/2025
# Copyright:   (c) PyAMS 2025
#-------------------------------------------------------------------------------



'''
The circuit consists of an inductive coil, L1 and a capacitor, C1.
The capacitor stores energy in the form of an electrostatic field and which produces
a potential (static voltage) across its plates, while the inductive coil stores its energy
in the form of an electromagnetic field. The capacitor is charged up to the DC supply voltage Ic=5V.
The capacitor now starts to discharge again back through the coil and the whole process is
repeated. The polarity of the voltage changes as the energy is passed back and forth
between the capacitor and inductor
producing an AC type sinusoidal voltage and current waveform.

with frequency:  fr= \frac{1}{2\pi\sqrt{LC}}
num:
fr=0.5 and T=2
'''

from pyams_lib import circuit
from models import Inductor, CapacitorIc
from math import pi

L1 = Inductor("out","0");
C1 = CapacitorIc("out","0");

L1.L+=1/pi
C1.C+=1/pi
C1.Ic+=5

circuit = circuit();
circuit.addElements({'L1':L1,'C1':C1})


# Set outputs for plotting;
circuit.setOutPuts("out");


# Set outputs for plotting;
circuit.analysis(mode="tran",start=0,stop=6,step=0.05);
circuit.run();
circuit.plot();