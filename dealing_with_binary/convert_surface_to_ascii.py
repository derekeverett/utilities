import numpy as np
import matplotlib.pyplot as plt

#the surface format
dt = np.dtype( [ ("t", np.float64), ("x", np.float64), ("y", np.float64), ("dst", np.float64), ("dsx", np.float64), ("dsy", np.float64), ("vx", np.float64), ("vy", np.float64), ("pitt", np.float64), ("pitx", np.float64), ("pity", np.float64), ("pixx", np.float64), ("pixy", np.float64), ("piyy", np.float64), ("pizz", np.float64), ("Pi", np.float64) ] )
#read in the binary file
surf = np.fromfile('surface.dat', dtype=dt)

t = surf["t"].tolist()
x = surf["x"].tolist()
y = surf["y"].tolist()

dst = surf["dst"].tolist()
dsx = surf["dsx"].tolist()
dsy = surf["dsy"].tolist()

vx = surf["vx"].tolist()
vy = surf["vy"].tolist()

pitt = surf["pitt"].tolist()
pitx = surf["pitx"].tolist()
pity = surf["pity"].tolist()
pixx = surf["pixx"].tolist()
pixy = surf["pixy"].tolist()
piyy = surf["piyy"].tolist()
pizz = surf["pizz"].tolist()

Pi = surf["Pi"].tolist()

#shape
#rint("shape of t is : " + str(t.shape) )

#write an ascii file
surf.tofile('surface_ascii.dat', sep='\t')

with open('surface_ascii.dat','w') as f:
    lis=[t, x, y, dst, dsx, dsy, vx, vy, pitt, pitx, pity, pixx, pixy, piyy, pizz, Pi]
    for x in zip(*lis):
        f.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\n".format(*x))
