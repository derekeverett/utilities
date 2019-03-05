import numpy as np
import matplotlib.pyplot as plt

#read in the ascii file
ed = np.loadtxt('ed_ascii.dat')


#check the array
print( "Shape of array : " + str(ed.shape) )
plt.imshow(ed, cmap='hot', interpolation='nearest')
plt.show()

ed.tofile('ed.dat')
