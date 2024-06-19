echo '# t/step [s]'  > timing_ipi.out ;  for i in 1 2 4 8  ; do cd $i'_mpi' ;grep 't/step' log.ipi | awk 'BEGINIG{c=0;m=0}{c+=1 ; m+=$9}END{print '$i', m/c}'>> ../timing_ipi.out ; cd .. ; done
