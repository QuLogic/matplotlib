#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as mwidgets

x = np.arange(0, 7, 0.001)
y = np.arange(-2.0, 5.0, 0.001)

fig = plt.figure(layout='constrained')
top, bottom = fig.subfigures(2, 1)

ax = top.subplots(subplot_kw={'polar': True, 'facecolor': 'red'})
ax.plot(x, y)
ax.set_title('Title')

ax.set_rmin(-1.5)
ax.set_rmax(2.5)
ax.set_rorigin(-5)
ax.set_thetamin(0)
ax.set_thetamax(135)
ax.set_theta_direction('counterclockwise')

ax.xaxis.set_tick_params(label2On=True)
ax.yaxis.set_tick_params(label2On=True)
ax.tick_params(direction='out')
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')


def update_dir(val):
    if val == 'CCW':
        ax.set_theta_direction('counterclockwise')
    else:
        ax.set_theta_direction('clockwise')


radios, sliders = bottom.subfigures(2, 1)

axdir, axoffs = radios.subplots(1, 2)
axdir.axis('off')
axoffs.axis('off')
axrmax, axrmin, axrorigin, axtmax, axtmin = sliders.subplots(5, 1)

stmin = mwidgets.Slider(axtmin, 'thetamin', 0, 360, valinit=ax.get_thetamin(),
                        closedmax=False)
stmax = mwidgets.Slider(axtmax, 'thetamax', 0, 360, valinit=ax.get_thetamax(),
                        closedmin=False, slidermin=stmin)
stmin.slidermax = stmax
stmin.on_changed(ax.set_thetamin)
stmax.on_changed(ax.set_thetamax)

srorigin = mwidgets.Slider(axrorigin, 'rorigin', -5, 5,
                           valinit=ax.get_rorigin(), closedmax=False)
srmin = mwidgets.Slider(axrmin, 'rmin', -5, 5, valinit=ax.get_rmin(),
                        closedmax=False)
srmax = mwidgets.Slider(axrmax, 'rmax', -5, 5, valinit=ax.get_rmax(),
                        closedmin=False, slidermin=srmin)
srmin.slidermax = srmax
srorigin.on_changed(ax.set_rorigin)
srmin.on_changed(ax.set_rmin)
srmax.on_changed(ax.set_rmax)

rdir = mwidgets.RadioButtons(axdir, ('CCW', 'CW'), active=0)
rdir.on_clicked(update_dir)

roffs = mwidgets.RadioButtons(axoffs, ('E', 'N', 'W', 'S'), active=0)
roffs.on_clicked(ax.set_theta_zero_location)

plt.show()
