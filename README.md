# pyams_lib
 Python library for analog and mixed-signal simulation (PyAMS Library)

<h1 align="center">
    <a href="https://pypi.org/project/pyams-lib/"><img src="https://pyams.sourceforge.io/logo.png" width="175px" alt="PyAMS"></a>
</h1>

---

<p align="center">
 
 <a href="#News">
    <img src="https://img.shields.io/badge/Version-0.1.1-blue" alt="V 0.1.1">
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

## Example Usage

### Voltage Divider Circuit Simulation

This example demonstrates a simple voltage divider circuit consisting of:

- A **DC voltage source (V1)** supplying the input voltage.
- Two **resistors (R1 and R2)** connected in series.
- The output voltage measured across **R2**.

### Code:

```python
from pyams_lib import circuit
from models.Basic.Resistor import Resistor
from models.Source.DCVoltage import DCVoltage

# Create a circuit instance
myCircuit = circuit()

# Add elements to the circuit
myCircuit.addElements({
    'V1': DCVoltage('1', '0'),  # Voltage source between node '1' and ground '0'
    'R1': Resistor('1', '2'),   # Resistor R1 between node '1' and '2'
    'R2': Resistor('2', '0')    # Resistor R2 between node '2' and ground '0'
})

# Set parameters for the elements
myCircuit.elem['V1'].setParams("Vdc=10V")  # Set input voltage to 10V
myCircuit.elem['R1'].setParams("R=2kΩ")  # Set R1 to 2kΩ
myCircuit.elem['R2'].setParams("R=2kΩ")  # Set R2 to 2kΩ

# Set outputs for plotting (output voltage at node '2')
myCircuit.setOutPuts('2')

# Perform DC analysis (operating point analysis)
myCircuit.analysis(mode='op')
myCircuit.run()

# Print the output voltage
output_voltage = myCircuit.x[myCircuit.nodes.index('2') - 1]  # Get voltage at node '2'
print(f"Output Voltage at node '2': {output_voltage:.2f} V")
```

### Expected Output:

```
Output Voltage at node '2': 5.00 V
```

---

This example demonstrates how `pyams_lib` simplifies circuit simulation, making it easier to analyze electronic components and their behavior efficiently.


