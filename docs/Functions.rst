.. _functions-page:

.. include:: importCSS.txt

Local functions
===============
.. role:: red

The fundamental local functions of the behavioral modeling of analog elements referring to a specific PyAMS library are listed in this page:

:red:`1. ddt()`

* **Application:** *ddt([Signal])* is used to calculate the signal derivative by time.
* **from:** pyams.lib
* **library name:** *dynamic.py*

:red:`2. idt()`

* **Application:** *idt([Signal])* is used to calculate integral of signal.
* **from:** pyams.lib
* **library name:** *dynamic.py*

:red:`3. realTime()`

* **Application:** *realTime()* the simulation time function provides an access to current simulation time or returns a value of time as a real number.
* **from:** pyams.lib
* **library name:** *dynamic.py*

:red:`4. limexp()`

* **Application:** *limexp([Value])* Limitation in exponential function.
* **from:** pyams.lib
* **library name:** *std.py*

:red:`5. vth()`

* **Application:** *vth([value=tnom])* Thermal voltage function.
* **from:** pyams.lib
* **library name:** *std.py*

:red:`6. toKelvin()`

* **Application:** *toKelvin([value])* Degree to kelvin.
* **from:** pyams.lib
* **library name:** *std.py*

:red:`7. trap()`

* **Application:** *trap( [Initial],[Peak],[Initial delay time],[Rise time],[Pulse-width],[Fall time],[Period of wave])* genrate trapezoid or pulse function.
* **from:** pyams.lib
* **library name:** *std.py*

        
        
