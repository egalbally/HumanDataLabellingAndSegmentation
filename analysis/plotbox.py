"""
Make box plot to visualize labelling success for each primitive

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sys

# medianprops = dict(linestyle='-', linewidth=3.0)#, color='firebrick')
rc('text',usetex=True)
dat = np.genfromtxt(sys.argv[1])
print(dat)
# plt.boxplot(dat,vert=False,patch_artist=True,medianprops=medianprops)
# plt.boxplot(dat,vert=False)
# plt.xlabel('Success')
# plt.savefig('boxplot.png',dpi=600)
# plt.show()
print("mean: ", np.mean(dat))
print("stdev: ", np.std(dat))

