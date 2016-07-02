#!/usr/bin/env python

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


r = np.arange(0, 3.0, 0.01)
theta = 2*np.pi*r

theta_mins = np.arange(15.0, 361.0, 90.0)
theta_maxs = np.arange(50.0, 361.0, 90.0)

fig, axes = plt.subplots(len(theta_mins), len(theta_maxs),
                         subplot_kw={'polar': True},
                         figsize=(16, 12))

for i, start in enumerate(theta_mins):
    for j, end in enumerate(theta_maxs):
        ax = axes[i, j]
        ax.name = '%d, %d' % (i, j)
        if start < end:
            ax.plot(theta, r)
            ax.set_thetamin(start)
            ax.set_thetamax(end)
        else:
            ax.set_visible(False)

plt.show()
