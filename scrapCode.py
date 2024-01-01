# __doc__ = "sample file for ploting method \
#            baed on \
#            https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

# #based on
# #source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

# #required imports
# import matplotlib.pyplot as plt
# # import numpy as np

# #================================================
# def exec_sample_plot_(file_name_out):
#   exec_sample_plot_.__doc__ = "sample call to mathplotlib"

#   #define figure
#   fig = plt.figure()
#   #add one plot
#   ax1 = fig.add_subplot(111)

#   #data
#   t = (1,2,3,4,5)
#   s = (2,2,4,5,8)
#   #define plots
#   ax1.plot(t, s, color ="green", lw = 2)

#   #add axis label
#   ax1.set_xlabel("time")
#   ax1.set_ylabel("sin (2 pi t)")

#   #add plot label
#   fig.suptitle("Plot Sample\n\n", fontweight ="bold")

#   #export as PDF
#   plt.savefig(file_name_out)
  
#   plt.show()



# import math
# from math import atan, sin, pi
import os
os.system('clear')
for x in range(5):
    print("hello world")