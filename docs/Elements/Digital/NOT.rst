

.. include:: ../importCSS.txt

NOT gate
========

.. role:: red

:red:`Symbol`

.. figure:: NOT.svg

:red:`Information`

The NOT gate is an electronic circuit that produces an inverted version of the input at its output.
It is also known as an inverter.

:red:`Ports`

* $In$ input terminal type electrical.
* $Out$ output terminal type electrical.


:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; NOT
   Symbol.file; NOT.sym
   Symbol.directory; Digital
   Symbol.referance; ``X``
   Model.name; ``NOT``
   Model.file; NOT.py

:red:`PyAMS model`

The NOT gate model in PyAMS is

.. code-block:: py3

 from PyAMS import model,signal,param
 from electrical import voltage

 # NOT Gate Model---------------------------------------------------------------
 class NOT(model):
     def __init__(self,Out,In):
        #Signals declarations---------------------------------------------------
         self.Vin = signal('in',voltage,In)
         self.Vout = signal('out',voltage,Out)

        #Parameter declarations-------------------------------------------------
         self.IL=param(0.2,'V','In low voltage')
         self.IH=param(3.2,'V','In high voltage')
         self.OL=param(0.0,'V','Out low voltage')
         self.OH=param(5.0,'V','Out high voltage')

     def analog(self):
         if(self.Vin<=self.IL):
            self.Vout+=self.OH
         elif(self.Vin>=self.IH):
            self.Vout+=self.OL
