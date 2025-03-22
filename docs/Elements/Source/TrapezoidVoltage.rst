.. include:: ../importCSS.txt

Trapezoid voltage
=================
.. role:: red

:red:`Symbol`

.. figure:: TrapezoidVoltage.svg

:red:`Information`

.. figure:: TrapezoidVoltage.png
   :scale: 50%
   :align: center

A voltage trapezoid or pulse train can be applied as an independent source in PyAMS using has seven parameters that describe its shape as shown in figure.

.. figure:: TrapV.png
   :scale: 50%
   :align: center

where:

* $V$    is voltage signal [V].
* $Vo$   is the parameter of initial voltage [V].
* $V1$   is the parameter of peak voltage [V].
* $Td$   is the parameter represent initial delay time [Sec].
* $Tr$   is the parameter represent rise time [Sec].
* $Tf$   is the parameter represent fall time [Sec].
* $Tw$   is the parameter represent pulse-width [Sec].
* $T$    is the parameter represent period of wave [Sec].

:red:`Ports`

* $p$ Positive terminal type electrical.
* $n$ Negative terminal type electrical.

:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; Trapezoid Voltage
   Symbol.file; TrapezoidVoltage.sym
   Symbol.directory; Source
   Symbol.referance; ``V``
   Model.name; ``TrapezoidVoltage``
   Model.file; TrapezoidVoltage.py

:red:`PyAMS model`

.. code-block:: py3

 from PyAMS import model,signal,param,time
 from electrical import voltage


 #Source for Trapezoid voltage---------------------------------------------------
 class TrapezoidVoltage(model):
     def __init__(self, a, b):
         #Signal  declaration---------------------------------------------------
         self.V = signal('out',voltage,a,b)

         #Parameters declarations-----------------------------------------------
         self.V0=param(1.0,'V','Initial voltage ')
         self.V1=param(1.0,'V','Peak voltage ')
         self.Td=param(0,'Sec','Initial delay time')
         self.Tr=param(0,'Sec','Rise time')
         self.Tw=param(0.05,'Sec','Pulse-width')
         self.Tf=param(0,'Sec','Fall time')
         self.T=param(0.1,'Sec','Period of wave')
         self.Voff=param(0.0,'V','Offset voltage')

     def analog(self):
         n=(time-self.Td)-int((time-self.Td)/self.T)*self.T
         if(time<=self.Td):
            self.V+=self.V0+self.Voff
         elif(n<=self.Tr):
            a=(self.V1-self.V0)/self.Tr
            self.V+=a*n+self.V0+self.Voff 
         elif(n<=(self.Tr+self.Tw)):
            self.V+=self.V1+self.Voff
         elif(n<=(self.Tr+self.Tw+self.Tf)):
            a=(self.V0-self.V1)/self.Tf
            self.V+=a*(n-self.Tr-self.Tw)+self.V1+self.Voff
         else:
            self.V+=self.V0



:red:`Command syntax`

.. code-block:: py3
    
   #import model
   from TrapezoidVoltage import *
   
   #Vname: is the name of the model.
   #p,n: The connection position in the circuit.
   Vname=TrapezoidVoltage(p,n)