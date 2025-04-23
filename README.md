# pyams_lib
 Python library for analog and mixed-signal simulation (PyAMS Library)

<h1 align="center">
    <a href="https://pypi.org/project/pyams-lib/"><img src="https://pyams-lib.readthedocs.io/en/latest/_static/logo_.png" width="150px" alt="PyAMS-lib"></a>
</h1>

---

<p align="center">

<a href="https://pyams-lib.readthedocs.io/">
    <img src="https://img.shields.io/badge/docs-PyAMS--lib-blue?logo=readthedocs" alt="PyAMS-lib Docs">
</a>
 
 <a href="#News">
    <img src="https://img.shields.io/badge/Version-0.1.6-blue" alt="V 0.1.6">
 </a>
  <a href="#Installation">
      <img src="https://img.shields.io/badge/Python->=3-blue" alt="Python 3+">
  </a>

  <a href="#Installation">
      <img src="https://img.shields.io/badge/PyPy->=3-blue" alt="PyPy 3+">
  </a>
    
  <a href="https://github.com/d-fathi/pyams_lib/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/GPLv3-blue" alt="GPLv3">
  </a>
</p>



# PyAMS Library

## What is `pyams_lib`?

`pyams_lib` is a Python package designed to simplify the modeling of analog elements and the simulation of electronic circuits. It provides:

- The ability to create custom models of electrical components.
- Simulation of circuits in different modes of operation.
- Visualization of simulation results using `matplotlib`.
- Compatibility with Python 3+ and PyPy, working across Linux, Windows, and macOS.
- PyAMS library (pyams_lib) documentation   <a href="https://pyams-lib.readthedocs.io/">https://pyams-lib.readthedocs.io/</a>.

## Installation

To install `pyams_lib`, use the following command:

```sh
pip install pyams_lib
```

To upgrade to the latest version:

```sh
pip install --upgrade pyams_lib
```

## License

`pyams_lib` is free to use and distributed under the **GPLv3** license.

---

# Example

## Example of modeling resistor and simulation in circuit

### Modeling Resistor

```python

from pyams.lib import model,signal,param
from pyams.lib import voltage,current

#Creat resistor model------------------------------------------------------------
class resistor(model):
    """
    This class implements a Resistor model.
    init(): initals Signals and  Parameters
    analog(): Defines the resistor behavior using Ohm's Law:
                  I = V / R
    """
    def __init__(self, p, n):
        #Signals declarations---------------------------------------------------
        self.V = signal('in',voltage,p,n)
        self.I = signal('out',current,p,n)

        #Parameters declarations------------------------------------------------
        self.R=param(1000.0,'Ω','Resistance')
        self.Pout=param(1000.0,'Ω','Resistance')

    def analog(self):
        """Defines the resistor's current-voltage relationship using Ohm's Law."""
        #Resistor equation-low hom (Ir=Vr/R)------------------------------------
        self.I+=self.V/self.R

```

### Voltage Divider Circuit Simulation

This example demonstrates a simple voltage divider circuit consisting of:

- A **DC voltage source (V1)** supplying the input voltage.
- Two **resistors (R1 and R2)** connected in series.
- The output voltage measured across **R2**.

### Code:

```python

from pyams.lib import circuit
from pyams.models  import  DCVoltage


# Elements of circuit
V1= DCVoltage('n1', '0')    # Voltage source between node 'n1' and ground '0'
R1= resistor('n1', 'n2')   # Resistor R1 between node 'n1' and 'n2'
R2= resistor('n2', '0')    # Resistor R2 between node 'n2' and ground '0'

# Set parameters for the elements
V1.setParams("Vdc=10V")  # Set input voltage to 10V
R1.setParams("R=2kΩ")    # Set R1 to 2kΩ
R2.setParams("R=2kΩ")    # Set R2 to 2kΩ

# Create a circuit instance
myCircuit = circuit()

# Add elements to the circuit
myCircuit.addElements({'V1': V1,'R1': R1, 'R2': R2})


# Perform DC analysis (operating point analysis)
myCircuit.analysis(mode='op')
myCircuit.run()


# print value voltage at node 'n2' and current in 'R1'
myCircuit.print('n2', R1.I)

```

### Expected Output:

```
Output Voltage at node n2: 5.00 V
Output current R1.I: 2.5 mA
```

---

This example demonstrates how `pyams_lib` simplifies circuit simulation, making it easier to analyze electronic components and their behavior efficiently.


