'''
=================
3D wireframe plot
=================

A very basic demonstration of a wireframe plot.
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import random

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Grab some test data.
# X, Y, Z = axes3d.get_test_data(0.01)
#
# # Plot a basic wireframe.
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
def fun(x, y):
  return x**2 + y

def mesh_2d_3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = y = np.arange(-3.0, 3.0, 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)
    # Z = 5
    # X, Y, Z = axes3d.get_test_data(0.01)

    # Plot a basic wireframe.
    # ax.plot_wireframe(X, Y, 5, rstride=10, cstride=10)
    ax.plot_surface(X,Y,Z)

mesh_2d_3d()
plt.show()
