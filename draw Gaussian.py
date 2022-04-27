import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

start=-1
end=1
mean_x = 0
mean_y = 0
sigma=1#设定均值和方差
X = np.linspace(start, end,100)
Y = np.linspace(start, end,100)



fig = plt.figure()
ax = fig.gca(projection='3d')

x,y=np.meshgrid(X,Y)
R = 1/(2*np.pi*sigma**2)*np.exp(-((x-mean_x)**2+(y-mean_y)**2)/(2*sigma**2))

# Plot the surface.
surf = ax.plot_surface(x, y, R, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gaussian Distribution mu=0 sigma=1")
plt.savefig("GDsigma=1(1).jpg")
plt.show()
