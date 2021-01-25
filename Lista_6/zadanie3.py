from scipy.interpolate import lagrange
import numpy as np

x = [-2.2, -0.3, 0.8, 1.9]
y = [-15.18, 10.962, 1.92, -2.04]

poly = lagrange(x, y)
polyder = np.polyder(poly)
print("Wartość pochodnej w x = 0, to", polyder(0))
polyder2 = np.polyder(polyder)
print("Wartość pochodnej w x = 0, to", polyder2(0))