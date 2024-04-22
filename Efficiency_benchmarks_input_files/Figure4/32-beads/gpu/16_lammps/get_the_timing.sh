
echo '# t/step [s]'  > timing_ipi.out ;  for i in 1  ; do cd $i'_mpi' ;grep 't/step' log.ipi | tail -n +4 | head -n -1 | awk 'BEGINIG{c=0;m=0}{c+=1 ; m+=$9}END{print '$i', m/c}'>> ../timing_ipi.out ; cd .. ; done 
