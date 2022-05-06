from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

def evalFunc(x, y):
    return (1-x)**2 + 100*(y-(x**2))**2

#x = arange(-10.0, 10.1, 0.1)
#y = arange(-10.0, 10.1, 0.1)

x = arange(-10, 10, 1)
y = arange(-10, 10, 1)
X, Y = meshgrid(x, y) # grid of point
Z = evalFunc(X, Y) # evaluation of the function on the grid
print(Z)

im = imshow(Z,cmap=cm.RdBu) # drawing the function
colorbar(im) # adding the colobar on the right

show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from numpy import sin,sqrt

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

ax.scatter(0, 0, 0, s=100)

plt.show