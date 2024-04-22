echo '# t/step [s]'  > timing_lammps.out ;  for i in 1 2 4 8 16 32 72 144 288 ; do cd $i'_mpi' ;grep 'timesteps/s' dp.out | awk '{print '$i', 1./$6}' >> ../timing_lammps.out ; cd .. ; done
