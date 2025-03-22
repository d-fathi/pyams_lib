.. include:: ../importCSS.txt

VCVS
====
.. role:: red

:red:`Symbol`

.. figure:: VCVS.svg

:red:`Information`

.. figure:: VCVS.png
   :scale: 50%
   :align: center


The Voltage-Controlled Voltage Source (VCVS) block model a linear voltage-controlled voltage source, described with the following equation:


.. math::

  	V_{out}=G*V_{in}

where:

* $V_{out}$ is out voltage signal [V] flowing from the p2 to the n2 control port.
* $V_{in}$ is in voltage signal [A] flowing from the p1 to the n1 control port.
* $G$ is gain multiplier.

:red:`Ports`

* $p1$ Positive terminal type electrical.
* $n1$ Negative terminal type electrical.
* $p2$ Positive terminal type electrical.
* $n2$ Negative terminal type electrical.

:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; VCVS
   Symbol.file; VCVS.sym
   Symbol.directory; Basic
   Symbol.referance; ``C``
   Model.name; ``VCVS``
   Model.file; VCVS.py


:red:`PyAMS model`

.. code-block:: py3

  from PyAMS import model,signal,param
  from electrical import voltage

  #Voltage-controlled voltage source Model--------------------------------------
  class VCVS(model):
     def __init__(self,p1,n1,p2,n2):
        #Signals declarations---------------------------------------------------
         self.Vin = signal('in',voltage,p1,n1)
         self.Vout = signal('out',voltage,p2,n2)

        #Parameter declarations-------------------------------------------------
         self.G=param(1.0,' ','Gain multiplier')

     def analog(self):
         self.Vout+=self.G*self.Vin

:red:`Command syntax`

.. code-block:: py3
    
   #import model
   from VCVS import *
   
   #Cname: is the name of the model.
   #p1,n1,p2,n2: The connection position in the circuit.
   Cname=VCVS(p1,n1,p2,n2)