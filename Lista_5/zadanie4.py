from scipy.interpolate import lagrange

import numpy as np
import matplotlib.pyplot as plt

Re = [0.2,2,20,200,2000,20000]

Cd = [103,13.9,2.72,0.8,0.401,0.433]


poly = lagrange(Re, Cd)
newx = np.linspace(0.15,21000,5000)

plt.plot(newx,poly(newx))
plt.show()
print(poly(5.50),poly(5000))
