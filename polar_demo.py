#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as mwidgets

x = np.arange(0, 7, 0.001)
y = np.arange(-2.0, 5.0, 0.001)

fig = plt.figure()

ax = fig.add_axes((0, 0.36, 1, 0.57), polar=True, facecolor='red')
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


def update_thetamin(val):
    ax.set_thetamin(val)
    fig.canvas.draw()


def update_thetamax(val):
    ax.set_thetamax(val)
    fig.canvas.draw()


def update_rorigin(val):
    ax.set_rorigin(val)
    fig.canvas.draw()


def update_rmin(val):
    ax.set_rmin(val)
    fig.canvas.draw()


def update_rmax(val):
    ax.set_rmax(val)
    fig.canvas.draw()


def update_dir(val):
    if val == 'CCW':
        ax.set_theta_direction('counterclockwise')
    else:
        ax.set_theta_direction('clockwise')
    fig.canvas.draw()


def update_offset(val):
    ax.set_theta_zero_location(val)
    fig.canvas.draw()


axtmin = fig.add_axes((0.15, 0.01, 0.75, 0.05))
axtmax = fig.add_axes((0.15, 0.06, 0.75, 0.05))
axrorigin = fig.add_axes((0.15, 0.11, 0.75, 0.05))
axrmin = fig.add_axes((0.15, 0.16, 0.75, 0.05))
axrmax = fig.add_axes((0.15, 0.21, 0.75, 0.05))
axdir = fig.add_axes((0.1, 0.26, 0.5, 0.1), facecolor='none')
axdir.axis('off')
axoffs = fig.add_axes((0.5, 0.26, 0.5, 0.1), facecolor='none')
axoffs.axis('off')

stmin = mwidgets.Slider(axtmin, 'thetamin', 0, 360, valinit=ax.get_thetamin(),
                        closedmax=False)
stmax = mwidgets.Slider(axtmax, 'thetamax', 0, 360, valinit=ax.get_thetamax(),
                        closedmin=False, slidermin=stmin)
stmin.slidermax = stmax
stmin.on_changed(update_thetamin)
stmax.on_changed(update_thetamax)

srorigin = mwidgets.Slider(axrorigin, 'rorigin', -5, 5,
                           valinit=ax.get_rorigin(), closedmax=False)
srmin = mwidgets.Slider(axrmin, 'rmin', -5, 5, valinit=ax.get_rmin(),
                        closedmax=False)
srmax = mwidgets.Slider(axrmax, 'rmax', -5, 5, valinit=ax.get_rmax(),
                        closedmin=False, slidermin=srmin)
srmin.slidermax = srmax
srorigin.on_changed(update_rorigin)
srmin.on_changed(update_rmin)
srmax.on_changed(update_rmax)

rdir = mwidgets.RadioButtons(axdir, ('CCW', 'CW'), active=0)
rdir.on_clicked(update_dir)

roffs = mwidgets.RadioButtons(axoffs, ('E', 'N', 'W', 'S'), active=0)
roffs.on_clicked(update_offset)

plt.show()
