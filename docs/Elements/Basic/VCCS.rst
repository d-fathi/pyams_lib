.. include:: ../importCSS.txt

VCCS
====
.. role:: red

:red:`Symbol`

.. figure:: VCCS.svg

:red:`Information`

.. figure:: VCCS.png
   :scale: 50%
   :align: center


The Voltage-Controlled Current Source (VCCS) block model a linear voltage-controlled current source, described with the following equation:


.. math::

  	I_{out}=G*V_{in}

where:

* $I_{out}$ is out current signal [A] flowing from the p2 to the n2 control port.
* $V_{in}$ is in voltage signal [V] flowing from the p1 to the n1 control port.
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

   Symbol.name; VCCS
   Symbol.file; VCCS.sym
   Symbol.directory; Basic
   Symbol.referance; ``C``
   Model.name; ``VCCS``
   Model.file; VCCS.py


:red:`PyAMS model`

.. code-block:: py3

   from PyAMS import model,signal,param
   from electrical import voltage,current

   #Voltage-controlled current source Model-------------------------------------
   class VCCS(model):
     def __init__(self,p1,n1,p2,n2):
        #Signals declarations---------------------------------------------------
         self.Vin = signal('in',voltage,p1,n1)
         self.Iout = signal('out',current,p2,n2)
        #Parameter declarations-------------------------------------------------
         self.G=param(1.0,' ','Gain multiplier')

     def analog(self):
         self.Iout+=self.G*self.Vin

:red:`Command syntax`

.. code-block:: py3
    
   #import model
   from VCCS import *
   
   #Cname: is the name of the model.
   #p1,n1,p2,n2: The connection position in the circuit.
   Cname=VCCS(p,n)