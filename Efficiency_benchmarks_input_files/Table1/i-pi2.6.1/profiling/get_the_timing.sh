
for j in classical_md_gas       classical_npsvr_noff  classical_svr_noff  pimd-32_npt_noff-threads  pimd_npt_noff    remd_scpimd_noff classical_md_gas_inet  classical_npt_noff   pimd_npt_gas  classical_md_noff      classical_nvt_noff    pimd-32_npt_noff    pimd_npt_gas_inet         remd_scpimd_gas ; do echo $j ; cd $j ; echo '# n_atoms  t/s ' > timing-ipi.log ; for i in 8 1024 8192 65536 ; do grep 't/step'  test-$i.log | tail -n +2 | awk 'BEGIN{c=0 ; m=0}{m+=$9 ; c+=1}END{print '$i', m/c}' >> timing-ipi.log ; done; cd .. ; done


