

.. include:: ../importCSS.txt

XNOR gate
=========

.. role:: red

:red:`Symbol`

.. figure:: XNOR.svg

:red:`Information`

The XNOR gate or the 'Exclusive-NOR' gate circuit does the opposite to the EOR gate.
It will give a low output if either, but not both, of its two inputs are high.

:red:`Ports`

* $In1$ input terminal type electrical.
* $In2$ input terminal type electrical.
* $Out$ output terminal type electrical.


:red:`Symbol description`

.. csv-table::
   :header: Field; Value
   :widths: 10, 10
   :delim: ;

   Symbol.name; XNOR
   Symbol.file; XNOR.sym
   Symbol.directory; Digital
   Symbol.referance; ``X``
   Model.name; ``XNOR``
   Model.file; XNOR.py

:red:`PyAMS model`

The XNOR gate model in PyAMS is

.. code-block:: py3

 from PyAMS import model,signal,param
 from electrical import voltage

 # XNOR Gate Model---------------------------------------------------------------
 class XNOR(model):
     def __init__(self,Out,In1,In2):
        #Signals declarations---------------------------------------------------
         self.In1 = signal('in',voltage,In1)
         self.In2 = signal('in',voltage,In2)
         self.Out = signal('out',voltage,Out)

        #Parameter declarations-------------------------------------------------
         self.IL=param(0.2,'V','In low voltage')
         self.IH=param(3.2,'V','In high voltage')
         self.OL=param(0.0,'V','Out low voltage')
         self.OH=param(5.0,'V','Out high voltage')

     def analog(self):
         if((self.Vin1<=self.IL) and (self.Vin2>=self.IH)):
            self.Vout+=self.OL
         elif((self.Vin1>=self.IH) and (self.Vin2<=self.IL)):
            self.Vout+=self.OL
         elif((self.Vin1>=self.IH) and (self.Vin2>=self.IH)):
            self.Vout+=self.OH
         elif((self.Vin1<=self.IL) and (self.Vin2<=self.IL)):
            self.Vout+=self.OH

