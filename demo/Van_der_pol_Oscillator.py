#-------------------------------------------------------------------------------
# Name:        Van der pol Oscillator
# Author:      D.fathi
# Created:     29/03/2025
# Copyright:   (c) PyAMS 2025
# Licence:     free GPLv3
#-------------------------------------------------------------------------------



from pyams.lib import model, signal, param
from pyams.lib import voltage, current

# Modeling Nonlinear Resistance  R=1/(µ*(V² - 1))---------------------------------
class NonlinearResistance(model):
    """
    This class implements a Nonlinear Resistance model.

    A nonlinear resistor exhibits a current-voltage relationship that is not
    governed by Ohm's law. Instead, the current depends on a nonlinear function
    of voltage.

    Attributes:
        V (signal): Input voltage signal across the nonlinear resistor, defined between nodes (p, n).
        I (signal): Output current signal through the nonlinear resistor, defined between nodes (p, n).
        µ (param): Scalar multiplier for nonlinearity, default is 1.0.

    Methods:
        analog(): Defines the nonlinear current-voltage relationship:
                  I = µ * V * (V² - 1)
    """

    def __init__(self, p, n):
        # Signal declarations
        self.V = signal('in', voltage, p, n)
        self.I = signal('out', current, p, n)

        # Parameter declarations
        self.µ = param(1.0, ' ', 'Scalar of nonlinearity')

    def analog(self):
        """Defines the nonlinear current-voltage relationship."""
        self.I += self.µ * self.V * (self.V * self.V - 1)



#Applicated Modele of Nonlinear Resistance to simulation Van der pol Oscillator

from pyams.lib import circuit
from pyams.models  import CapacitorIc, InductorIc


R1 = NonlinearResistance("Vout","0");
C1 = CapacitorIc("Vout","0");
L1 = InductorIc("Vout","0");


C1.setParams("C=1F Ic=2V");
L1.setParams("Ic=-6A L=1H ");

# Create circuit and add elements
circuit = circuit();
circuit.addElements({'R1':R1,'C1':C1,'L1':L1})


# Set outputs for plotting;
circuit.setOutPuts("Vout");


# Perform transient analysis
circuit.analysis(mode="tran",start=0,stop=70,step=0.1);
circuit.run();
circuit.plot();