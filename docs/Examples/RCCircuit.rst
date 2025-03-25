RC Circuit Simulation
=====================

Overview
--------

The circuit consists of a **resistor (R1)** and a **capacitor (C1)** forming an RC circuit. The circuit is driven by a **square wave voltage source (V1)**. 

- When the input voltage **Vin** switches from low to high, the capacitor **C1** begins charging through the resistor **R1**.
- When **Vin** switches from high to low, the capacitor discharges.
- This creates a characteristic **exponential charging and discharging** behavior.

Time Constant
-------------

The **time constant** (τ) of an RC circuit is given by:

.. math::

   \tau = R \cdot C

For this simulation:

- **Resistance**: `R = 100 \Omega`
- **Capacitance**: `C = 100 \mu F`
- **Time Constant**: `τ = 100 × 100 × 10^{-6} = 0.01 s`

Circuit Diagram
---------------

The following diagram illustrates the RC circuit:

.. image:: RC.png
   :align: center
   :alt: RC Circuit Diagram

Simulation Code
---------------

The following Python script simulates the RC circuit using the **PyAMS library**:

.. code-block:: python

   from pyams_lib import circuit
   from models import Resistor, SquareVoltage, Capacitor

   # Define components
   R1 = Resistor("Vin", "Vout")
   V1 = SquareVoltage("Vin", "0")
   C1 = Capacitor("Vout", "0")

   # Set component parameters
   R1.setParams("R=100")
   V1.setParams("Va=10V T=200ms")
   C1.setParams("C=100uF")

   # Create circuit and add elements
   circuit = circuit()
   circuit.addElements({'R1': R1, 'V1': V1, 'C1': C1})

   # Set output for plotting
   circuit.setOutPuts("Vin", "Vout")

   # Perform transient analysis
   circuit.analysis(mode="tran", start=0, stop=1, step=0.001)
   circuit.run()
   circuit.plot()

Simulation Output
-----------------

The output voltage **Vout** follows an exponential response due to the capacitor's charging and discharging behavior. The simulation produces the following waveform:

.. image:: Figure_2.png
   :align: center
   :alt: RC Circuit Output Waveform

Conclusion
----------

The RC circuit acts as a **low-pass filter**, smoothing the square wave input into a more gradual exponential waveform. The simulation confirms this behavior by displaying the expected charging and discharging curves.
