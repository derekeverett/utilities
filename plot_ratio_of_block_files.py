import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import sys
import csv

file1 = sys.argv[1]
file2 = sys.argv[2]

#with open(file1, 'r') as csvfile:
#    file1_data = csv.reader(csvfile, delimiter=' ')
#    for row in file1_data:
#        vals1.append(float(row[0]))

df1 = pd.read_csv(file1, header=None, delimiter="\s+")

df2 = pd.read_csv(file2, header=None, delimiter=r"\s+")

#print(df1.values)

ratio = df1.values / df2.values

percent_diff = (df1.values - df2.values) / df1.values

np.savetxt('ratio_of_block_files.dat', ratio)

np.savetxt('percent_diff_of_block_files.dat', percent_diff)
