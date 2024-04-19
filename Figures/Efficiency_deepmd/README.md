Data and scripts to generate figures related to Efficiency of large-scale simulations carried out with DeepMD

- `timing_ipi_[cpu,gpu].out` contains the timing for a step in seconds, for a simple MD calculation with i-pi in NVT and svr thermostat with 1 beads on CPU or GPU
- `timing_lammps_[cpu,gpu].out` contains the timing for a step in seconds, for a simple MD calculation with lammps in NVT and svr thermostat with 1 beads on CPU or GPU
- `timing_ipi-32_beads-[i]_lammps_[cpu,gpu].out` contains the timing for a step in seconds, for a PIMD calculation with i-pi in NVT and svr thermostat with 32 beads and i-number of lammps instances on CPU or GPU
- `graph.py` is a simple `python` script to generate the figure. 

In all the files the first column is the number of mpi process (so number of cpu/gpu allocated) per instances.

All the files are taken from the timing in `../../Efficiency_benchmarks_input_files/Figure3`
