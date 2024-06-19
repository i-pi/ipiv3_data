import numpy

def parse_lmp_output(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'Loop time' in line:
                columns = line.split()
                if len(columns) >= 9:  # Ensure there are enough columns
                    # Convert the fourth and ninth columns to floats and divide
                    result = float(columns[3]) / float(columns[8])
                    return result

for mode in ['Pn_Tn', 'Py_Tn', 'Pn_Ty', 'Py_Ty']:

  nmols = []
  timings = []
  for nmol in [8, 64, 512, 4096, 32768]:

      filename = str(nmol).zfill(5) + '_' + mode + '/log.lmp'
      nmols.append(nmol)
      timings.append(parse_lmp_output(filename))

  numpy.savetxt(mode + '.txt', numpy.c_[nmols, timings], header = '# number_of_molecules # time_per_MD_step')
