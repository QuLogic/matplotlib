#!/usr/bin/env python

"""
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#plt.rcParams['toolbar'] = 'toolmanager'


r = np.arange(0, 3.0, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, polar=True, facecolor='b')
ax.plot(theta, r, color='r', linewidth=3)
ax.set_rmax(2.0)
#ax.set_thetamin(100)
#ax.set_thetamax(180)
ax.grid(True)
ax.set_rmin(-1)
ax.set_rorigin(-2)
ax.set_theta_direction('clockwise')
ax.set_theta_zero_location('N')

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
plt.savefig('output.png')
