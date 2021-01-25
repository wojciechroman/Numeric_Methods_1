from scipy.interpolate import lagrange
import numpy as np

x = [0.0, 0.1, 0.2, 0.3, 0.4]
y = [0.0, 0.078348, 0.13891, 0.192916, 0.244981]

poly = lagrange(x, y)
polyder = np.polyder(poly)

print("Wartosc pochodnej w x = 0.2, to", polyder(0.2))