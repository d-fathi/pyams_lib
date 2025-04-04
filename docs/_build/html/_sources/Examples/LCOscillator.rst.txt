LC Oscillator Simulation
========================

Overview
--------

The circuit consists of an **inductor (L1)** and a **capacitor (C1)** forming an LC oscillator. The capacitor stores energy in an electrostatic field, producing a potential voltage across its plates, while the inductor stores energy in an electromagnetic field. 

Initially, the capacitor is charged to **Ic = 5V**. When the capacitor discharges through the inductor, energy oscillates between the capacitor and the inductor, generating a sinusoidal waveform.

Oscillation Frequency
---------------------

The resonant frequency of the LC circuit is given by:

.. math::

   f_r = \frac{1}{2\pi\sqrt{LC}}

For this simulation:

- **Resonant Frequency**: `fr = 0.5 Hz`
- **Time Period**: `T = 2 s`

Circuit Diagram
---------------

The LC oscillator circuit is illustrated in the following diagram:

.. image:: LC_Oscillator.png
   :align: center
   :alt: LC Oscillator Circuit Diagram

Simulation Code
---------------

The following Python script simulates the LC oscillator using the **PyAMS library**:

.. code-block:: python

   from pyams_lib import circuit
   from models import Inductor, CapacitorIc
   from math import pi

   # Define components
   L1 = Inductor("out","0")
   C1 = CapacitorIc("out","0")

   # Set component values
   L1.L += 1/pi
   C1.C += 1/pi
   C1.Ic += 5  # Initial capacitor charge

   # Create circuit and add elements
   circuit = circuit()
   circuit.addElements({'L1': L1, 'C1': C1})

   # Set output for plotting
   circuit.setOutPuts("out")

   # Perform transient analysis
   circuit.analysis(mode="tran", start=0, stop=6, step=0.05)
   circuit.run()
   circuit.plot()

Simulation Output
-----------------

The simulation generates the following sinusoidal waveform:

.. image:: Figure_1.png
   :align: center
   :alt: LC Oscillator Output Waveform

Conclusion
----------

The LC oscillator generates an AC waveform due to the continuous exchange of energy between the inductor and capacitor. The PyAMS simulation verifies this behavior by producing a sinusoidal voltage output over time.
