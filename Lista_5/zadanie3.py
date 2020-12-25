from scipy.interpolate import UnivariateSpline

import numpy as np
import matplotlib.pyplot as plt

Re = [0.2,2,20,200,2000,20000]

Cd = [103,13.9,2.72,0.8,0.401,0.433]

spline = UnivariateSpline(Re, Cd)

NewRe = np.linspace(0,21000,100000)
plt.plot(NewRe, spline(NewRe))
plt.show()