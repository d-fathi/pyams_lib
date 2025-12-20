.. _commands-manual-page:

Commands
========

The pyams.lib command syntax for simulation.

Create the Circuit Object
*************************
   
Initialize a ``circuit`` object to hold the components.

Syntax:

.. code-block:: py3

   from pyams.lib import circuit

   cir=circuit()
   cir.addElements(model_name_1,model_name_2,......,model_name_n)


Outputs
*******

``cir.outputs()`` This command saves results from op, dc, and transient analyzes
into data for showing by wave form(matplotlib) . The outputs are: the nodes, signals and parameters used in the circuit.

Syntax:

.. code-block:: py3

   cir.outputs(*nodes_name,*parameters_name,*signals_name)

Analysis
********
``cir.analysis()`` This command used to analyses or simulation circuit in 
the  time-domain (tran) or direct-current (DC) or operating-points (op).

Syntax:[time-domain]

.. code-block:: py3

   cir.analysis(mode="tran",start=[start_value],stop=[stop_value],step=[step_value]);

Syntax:[direct-current]

.. code-block:: py3

   cir.analysis(mode="dc",param=[param_name],start=[start_value],stop=[stop_value],step=[step_value]);

Syntax:[operating-points]

.. code-block:: py3

   cir.analysis(mode="op");

Run the Simulation
*******************
``cir.run()`` This command used to Execute the analysis and plot the results.

   .. code-block:: python

       cir.run()

Plot the Simulation
*******************
``cir.plot()`` This command used to plot the results.

   .. code-block:: python

       cir.plot()
