import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import sys
import csv
from matplotlib import cm

file1 = sys.argv[1]
file2 = sys.argv[2]

df1 = pd.read_csv(file1, header=None, delimiter="\s+")
df2 = pd.read_csv(file2, header=None, delimiter=r"\s+")


ratio = df1.values / df2.values
percent_diff = ( (df1.values - df2.values) / df1.values ) * 100

np.savetxt('ratio_of_block_files.dat', ratio)
np.savetxt('percent_diff_of_block_files.dat', percent_diff)

plt.imshow(ratio, interpolation='nearest')
plt.colorbar()
plt.title("Ratio of file 1 to file 2")
plt.show()

plt.imshow(percent_diff, interpolation='nearest')
plt.colorbar()
plt.title("Percent Difference file 1 to file 2")
plt.show()
