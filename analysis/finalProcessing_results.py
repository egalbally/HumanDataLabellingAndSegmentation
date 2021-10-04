"""======================================================================================
 finalProcessing_results.py
 
 Input: runs you want to run and num of Tmatrix updates    
 Output: 
 	- Plots segmented data both manual and automatic
 	- Computes success rate as the similarity between demonstrated and labelled primitive sequences

 *note -> likelihood plots are created and saved inside 
       the expectation_step called by train and test in gmm.py
 
Last update, Fall 2020
======================================================================================"""
import imageio
import matplotlib.animation as ani
import matplotlib.cm as cmx
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
import enum
import sys
import bisect
import random
import collections
import os

from matplotlib.patches import Ellipse
from PIL import Image
from sklearn import datasets
from sklearn.cluster import KMeans

from matplotlib.pyplot import figure, show
from matplotlib.ticker import MaxNLocator

from read_data import read_data1
from plot_data import getlabels, plot_file , compute_success_rate

from difflib import SequenceMatcher

# # latex formatting
# rc('text',usetex=True)
# rcParams['axes.titlesize'] = 'x-large'
# rcParams['axes.labelsize'] = 'large'
# rcParams['xtick.labelsize'] = 'x-large'
# rcParams['ytick.labelsize'] = 'x-large'


###############################################
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# compute primtive sequence similarity
# cap: avg success 0.88
NUM_RUNS = 20
totalsuccess = 0
for run_number in range(1,NUM_RUNS): 
	if run_number == 11 or run_number == 16:
			continue
	trueSequence = np.genfromtxt("../data/medium_cap/raw_medium_cap/run{0:d}_prmlabels".format(run_number),dtype=str)
	autoSequence = np.genfromtxt("past_results/stateEstimation/results/run{0:d}_prmlabels_T0".format(run_number),dtype=str)
	success = similar(trueSequence, autoSequence)
	totalsuccess += success
	print("run {0:d}: {1:f}".format(run_number, success))
avg_success = totalsuccess/(NUM_RUNS-3)
print("avg_success: {0:f}".format(avg_success))

# #################################################################################
# # numTMatrixUpdates = 1 
# # lastT = numTMatrixUpdates - 1
# # trans2plot = [0,lastT]
# print(">>>> Pato dibujando")

# # run2plot = [2, 6, 18]
# run2plot = 20

# """
# CAP

# """
# # ----------------------------------
# # Plot sensor data of labelled run 
# #   - for initial and final transition matrix
# #   - for run2 (really good) and run12 (sucks)
# #   - 4 plots     
# # run2plot = [2, 12]
# # for i in range(2): 
# #     for t in range(2):
# #         plot_file('../data/medium_cap/raw_medium_cap/run{0:d}'.format(run2plot[i]),
# #             tlabelfile="results/run{0:d}_tlabels_T{1:d}".format(run2plot[i],trans2plot[t]),
# #             prlabelfile="results/run{0:d}_prmlabels_T{1:d}".format(run2plot[i],trans2plot[t]),
# #             tlabelfileTruth='../data/medium_cap/raw_medium_cap/run{0:d}_tlabels'.format(run2plot[i]),
# #             prlabelfileTruth='../data/medium_cap/raw_medium_cap/run{0:d}_prmlabels'.format(run2plot[i])
# #             )
# #         plt.savefig("figures/labelled_run{0:d}_T{1:d}.png".format(run2plot[i],trans2plot[t]),dpi=600)
# #         # plt.show()
# #         plt.close()


# """
# PIPE

# """     
# trans2plot = 0

# # for i in range(2): 
# #     plot_file('../data/pipe/raw_pipe/run{0:d}'.format(run2plot[i]),
# #         tlabelfile="results/run{0:d}_tlabels_T{1:d}".format(run2plot[i],trans2plot),
# #         prlabelfile="results/run{0:d}_prmlabels_T{1:d}".format(run2plot[i],trans2plot)
# # #       tlabelfileTruth='../data/pipe/raw_pipe/run{0:d}_tlabels'.format(run2plot[i]),
# # #       prlabelfileTruth='../data/pipe/raw_pipe/run{0:d}_prmlabels'.format(run2plot[i])
# #         )
# #     plt.savefig("figures/labelled_run{0:d}_T{1:d}.png".format(run2plot[i],trans2plot),dpi=600)
# #     plt.close()

# for i in range(1,20): 
# 	print("run {0:d}".format(i))
# 	plot_file('../data/pipe/raw_pipe/run{0:d}'.format(i), 
#     	tlabelfile="results/run{0:d}_tlabels_T{1:d}".format(i,trans2plot), 
#     	prlabelfile="results/run{0:d}_prmlabels_T{1:d}".format(i,trans2plot))
# 	#       tlabelfileTruth='../data/pipe/raw_pipe/run{0:d}_tlabels'.format(i),
# 	#       prlabelfileTruth='../data/pipe/raw_pipe/run{0:d}_prmlabels'.format(i)
# 	plt.savefig("figures/labelled_run{0:d}_T{1:d}.png".format(i,trans2plot),dpi=600)
# 	plt.title('Pipe Demonstration \#{0:d}'.format(i))
# 	plt.close()

# print(">>>> Pato ha terminado de dibujar")