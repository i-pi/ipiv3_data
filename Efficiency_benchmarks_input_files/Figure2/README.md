# Benchmarks 
Inputs, scripts, and model information necessary to reproduce benchmark runs present in the main text.

This directory includes 3 types of i-pi simulations

npt-i-pi-no-interface: i-pi simulations for an ideal gas by not calling the forcefield socket.

npt-i-pi-ideal-gas-interface: i-pi simulations for an ideal gas via a UNIX socket communicating with i-pi's driver within the ideal gas mode (-m gas).

npt-i-pi-lmp-interface: i-pi similations for boxes of water molecules using the Behlar-Parrinello neural network potential from Ravindra, P., Advincula, X. R., Schran, C., Michaelides, A., & Kapil, V. (2023). A quasi-one-dimensional hydrogen-bonded monolayer ice phase. https://doi.org/10.48550/ARXIV.2312.01340

It contains one type of LAMMPS simulations

npt-lmp-ideal-gas: LAMMPS simulations for an ideal gas (without any pair_style)

It also includes

structures: a directory containing simulation water molecule boxes with icreasing system sizes. 

.py: python scripts to extract timings of i-pi and LAMMPS simulations. 

nnp: The Behlar-Parrinello neural network potential files from Ravindra, P., Advincula, X. R., Schran, C., Michaelides, A., & Kapil, V. (2023). A quasi-one-dimensional hydrogen-bonded monolayer ice phase. https://doi.org/10.48550/ARXIV.2312.01340

The figure present in the main text can be found in the ../Figures/Efficiency folder
