from scipy.interpolate import lagrange

import numpy as np
import matplotlib.pyplot as plt

x = [1,1.25,1.5,1.75,2,2.25,2.5,2.75,3]

y = [-0.5403,-0.0104,0.9423,1.7445,1.3073,-0.7718,-2.4986,-0.7903,2.7334]


poly = lagrange(x, y)
newx = np.linspace(0.8,3.2,1000)

plt.plot(newx,poly(newx))
plt.show()
