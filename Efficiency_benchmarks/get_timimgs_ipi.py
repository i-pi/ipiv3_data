import numpy

def parse_ipi_output(file_path):
    final_column_values = []

    with open(file_path, 'r') as file:
        for line in file:
            if "MD" in line:
                columns = line.split()
                if columns:  # Check if the line is not empty
                    # Append the last column value to the list, converting it to the appropriate type
                    final_column_values.append(float(columns[-1]))

    return numpy.array(final_column_values)



for mode in ['Pn_Tn', 'Py_Tn', 'Pn_Ty', 'Py_Ty']:

  nmols = []
  timings = []
  for nmol in [8, 64, 512, 4096, 32768]:

      filename = str(nmol).zfill(5) + '_' + mode + '/log.i-pi'
      nmols.append(nmol)
      timings.append(parse_ipi_output(filename).mean())

  numpy.savetxt(mode + '.txt', numpy.c_[nmols, timings], header = '# number_of_molecules # time_per_MD_step')
