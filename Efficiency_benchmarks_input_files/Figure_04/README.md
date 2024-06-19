# Benchmarks 
Inputs, scripts, and model information necessary to reproduce benchmark runs present in the main text.

## DeepMD
The model used in the simulations is taken from https://github.com/deepmodeling-activity/deepmd-kit-v2-paper/blob/main/models/03/frozen_model.pb 

This folder contains all the script to generate the data for the benchmark runs with DeePMD, both on GPU and CPU:

- The `1-beads` folder contains the inputs to generate the data for the simple MD runs with 1 beads, on all the architectures and both with i-Pi and LAMMPS alone.
I contains two folders `cpu` and `gpu` that determine on which architecture the tests are run on.
Each of these subfolders contains other 2 folders `i-pi` and `lammps` that defines if the calculations are run with i-Pi or with LAMMPS alone. Each of these two folder contains all the data, inputs and the job examples to run the actaul test. These two folder should be independent with the rest, and they can be copied somewhere else *as it is* to be uses for your tests, given that the job scripts are changed properly.
- The `32-beads` folder contains the inputs to generate the data for the PIMD runs with 32 beads on all the architectures. I contains two folders `cpu` and `gpu` that determine on which architecture the tests are run on.
Each of these subfolders contains folders named `i_lammps`, each one containing the simulation with `i` lammps instances.


All the calculations on CPU are done on compute nodes of JED (https://www.epfl.ch/research/facilities/scitas/jed/): 2 Intel(R) Xeon(R) Platinum 8360Y processors running at 2.4 GHz, with 36 cores each (72 cores per machine)
All the calculations on GPU are done on compute nodes of IZAR (https://www.epfl.ch/research/facilities/scitas/hardware/izar/). Each node has 2 Xeon-Gold processors running at 2.1 GHz, with 20 cores each, with 2 NVIDIA V100 PCIe 32 GB GPUs. 


