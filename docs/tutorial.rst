.. _tutorial:

Tutorial
================================

First, navigate to the example folder and take a look at the files inside this directory:

.. code-block:: bash
    
    cd example
    ls -l

The directory contains temperature data in matrix form and also precipitation data and snowfall data.
The statistics of these files (starting from iteration 2) could be done by issuing the following command:

.. code-block:: bash
    
    python -m statsfiles 2 -f example.yml


