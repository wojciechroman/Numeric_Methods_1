import matplotlib.pyplot as plt
import numpy as np

x = [0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150]
y = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]

f = np.polyfit(x,y,2)
newf = np.poly1d(f)

newx = np.linspace(0,15,2000)
plt.plot(newx, newf(newx))
plt.show()

d = newf(10.5)
print(d)