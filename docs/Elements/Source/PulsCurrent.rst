.. include:: ../importCSS.txt

Puls current
==============
.. role:: red

:red:`Symbol`

.. figure:: PulsCurrent.svg

:red:`Information`

.. figure:: PulsCurrent.png
   :scale: 50%
   :align: center

A puls wave current source is an electrical component that generates a rectangular current in a the duty cycle of period T. That describe its shape as shown in figure.

.. figure:: PulsI.png
   :scale: 50%
   :align: center

where:

* $Ia$   is the parameter of amplitude of square wave current [A].
* $D$    is the duty cycle
* $T$    is the parameter represent period of wave [Sec].


:red:`Ports`

* $p$ Positive terminal type electrical.
* $n$ Negative terminal type electrical.


:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; Puls Current
   Symbol.file; PulsCurrent.sym
   Symbol.directory; Source
   Symbol.referance; ``I``
   Model.name; ``PulsCurrent``
   Model.file; PulsCurrent.py

:red:`PyAMS model`

.. code-block:: py3

 from PyAMS import model,signal,param, time
 from electrical import current

 #Source for puls current--------------------------------------------------------
 class PulsCurrent(model):
     def __init__(self, p, n):
         #Signal  declaration---------------------------------------------------
         self.I = signal('out',current,p,n)

         #Parameters declarations-----------------------------------------------
         self.Ia=param(1.0,'A','Amplitude of square wave current  ')
         self.T=param(0.1,'Sec','Period')
         self.D=param(50,'%','Duty cycle')
         self.Ioff=param(0.0,'A','Offset current')

     def analog(self):
         n=time-int(time/self.T)*self.T

         if(n<=self.T*self.D/100):
             self.I+=self.Ia+self.Ioff
         else:
             self.I+=self.Ioff

:red:`Command syntax`

.. code-block:: py3
    
   #import model
   from PulsCurrent import *
   
   #Iname: is the name of the model.
   #p,n: The connection position in the circuit.
   Iname=PulsCurrent(p,n)