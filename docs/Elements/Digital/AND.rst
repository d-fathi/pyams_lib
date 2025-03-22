

.. include:: ../importCSS.txt

AND gate
========

.. role:: red

:red:`Symbol`

.. figure:: AND.svg

:red:`Information`

The AND gate is an electronic circuit that gives a high output (1) only if all its inputs are high.

:red:`Ports`

* $In1$ input terminal type electrical.
* $In2$ input terminal type electrical.
* $Out$ output terminal type electrical.


:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; AND
   Symbol.file; AND.sym
   Symbol.directory; Digital
   Symbol.referance; ``X``
   Model.name; ``AND``
   Model.file; AND.py


:red:`PyAMS model`

The AND gate model in PyAMS is

.. code-block:: py3

 from PyAMS import model,signal,param
 from electrical import voltage

 # AND Gate Model---------------------------------------------------------------
 class AND(model):
     def __init__(self,Out,In1,In2):
        #Signals declarations---------------------------------------------------
         self.Vin1 = signal('in',voltage,In1)
         self.Vin2 = signal('in',voltage,In2)
         self.Vout = signal('out',voltage,Out)
        #Parameter declarations-------------------------------------------------
         self.IL=param(0.2,'V','In low voltage')
         self.IH=param(3.2,'V','In high voltage')
         self.OL=param(0.0,'V','Out low voltage')
         self.OH=param(5.0,'V','Out high voltage')

     def analog(self):
         if((self.Vin1<=self.IL)or(self.Vin2<=self.IL)):
            self.Vout+=self.OL
         elif((self.Vin1>=self.IH)and(self.Vin2>=self.IH)):
            self.Vout+=self.OH
