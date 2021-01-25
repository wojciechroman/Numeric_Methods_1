from scipy import misc
import numpy as np

def f(x):
    return np.log(np.tanh(x / (x * x + 1)))

point = 0.2

d1 = misc.derivative(f, 0.2, 1e-4, 1)
print("Pochodna 1 rzędu",d1)
d2 = misc.derivative(f, 0.2, 1e-4, 2)
print("Pochodna 2 rzędu",d2)
d3 = misc.derivative(f, 0.2, 1e-4, 3, order=9)
print("Pochodna 3 rzędu",d3)
