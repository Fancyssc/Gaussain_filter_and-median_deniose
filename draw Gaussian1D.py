import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots()
x = np.linspace(-10,10,1000)
y1 = 1/np.sqrt(np.pi*2*1**2)*np.exp(-x**2/(2*1**2))
y2 = 1/np.sqrt(np.pi*2*2**2)*np.exp(-x**2/(2*2**2))
y3 = 1/np.sqrt(np.pi*2*3**2)*np.exp(-x**2/(2*3**2))
ax.plot(x, y1, label='sigma=1')
ax.plot(x, y2, label='sigma=2')
ax.plot(x, y3, label='sigma=3')
ax.set_title('Gaussian Distribution with different sigmas') #设置图名为Simple Plot
ax.legend()
plt.savefig("Gaussian Distribution with different sigmas.jpg")
plt.show()

