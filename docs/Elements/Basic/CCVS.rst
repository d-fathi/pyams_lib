.. include:: ../importCSS.txt

CCVS
====
.. role:: red

:red:`Symbol`

.. figure:: CCVS.svg

:red:`Information`

.. figure:: CCVS.png
   :scale: 50%
   :align: center

The Current-Controlled Voltage Source (CCVS) block model a linear current-controlled voltage source, described with the following equation:


.. math::

  	V_{out}=G*I_{in}

where:

* $V_{out}$ is out voltage signal [V] flowing from the p2 to the n2 control port.
* $I_{in}$ is in current signal [A] flowing from the p1 to the n1 control port.
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

   Symbol.name; CCVS
   Symbol.file; CCVS.sym
   Symbol.directory; Basic
   Symbol.referance; ``C``
   Model.name; ``CCVS``
   Model.file; CCVS.py

:red:`PyAMS model`

.. code-block:: py3

   from PyAMS import model,signal,param
   from electrical import voltage,current

   #Current-controlled voltage source model-------------------------------------
   class CCVS(model):
     def __init__(self,p1,n1,p2,n2):
        #Signals declarations---------------------------------------------------
         self.I = signal('in',current,p1,n1)
         self.V = signal('out',voltage,p2,n2)

        #Parameter declarations-------------------------------------------------
         self.G = param(1.0,'Ohm','Gain multiplier')

     def analog(self):
         self.V+=self.G*self.I

:red:`Command syntax`

.. code-block:: py3
    
   #import model
   from CCVS import *
   
   #Cname: is the name of the model.
   #p1,n1,p2,n2: The connection position in the circuit.
   Cname=CCVS(p1,n1,p2,n2)