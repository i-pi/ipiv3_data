echo '# n_atoms  t/s ' > timing-ipi.log ; for i in 8 1024 8192 65536 ; do grep 't/step'  test-$i.log | tail -n +2 | head -n -1 | awk 'BEGIN{c=0 ; m=0}{m+=$9 ; c+=1}END{print '$i', m/c}' >> timing-ipi.log ; done
[tisi@jed classical_md_gas]$ cat timing-ipi.log 
