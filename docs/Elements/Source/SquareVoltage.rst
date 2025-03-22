.. include:: ../importCSS.txt

Square voltage
===========
.. role:: red

:red:`Symbol`

.. figure:: SquareVoltage.svg

:red:`Information`

.. figure:: SquareVoltage.png
   :scale: 50%
   :align: center

A square wave voltage source is an electrical component that generates a rectangular voltage in a half-period T. That describe its shape as shown in figure.

.. figure:: SquareV.png
   :scale: 50%
   :align: center

where:

* $Va$   is the parameter of amplitude of square wave voltage [V].
* $T$    is the parameter represent period of wave [Sec].


:red:`Ports`

* $p$ Positive terminal type electrical.
* $n$ Negative terminal type electrical.

:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; Square Voltage
   Symbol.file; SquareVoltage.sym
   Symbol.directory; Source
   Symbol.referance; ``V``
   Model.name; ``SquareVoltage``
   Model.file; SquareVoltage.py

:red:`PyAMS model`

.. code-block:: py3

 from PyAMS import model,signal,param, time
 from electrical import voltage

 #Source for square voltage-----------------------------------------------------
 class SquareVoltage(model):
     def __init__(self, p, n):
         #Signal  declaration--------------------------------------------------
         self.V= signal('out',voltage,p,n)

         #Parameters declarations----------------------------------------------
         self.Va=param(1.0,'V','Amplitude of square wave voltage  ')
         self.T=param(0.1,'Sec','Period')
         self.Voff=param(0.0,'V','Offset voltage')

     def analog(self):
         n=time-int(time/self.T)*self.T
  
         if(n<=self.T/2):
             self.V+=self.Va+self.Voff
         else:
             self.V+=self.Voff


:red:`Command syntax`

.. code-block:: py3
    
   #import model
   from SquareVoltage import *
   
   #Vname: is the name of the model.
   #p,n: The connection position in the circuit.
   Vname=SquareVoltage(p,n)