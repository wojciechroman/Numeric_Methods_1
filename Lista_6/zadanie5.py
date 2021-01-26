import numpy as np
from scipy import integrate

def f(x1, x2):
    return 1 / np.sqrt(1 - np.sin(x1 / 2) ** 2 * np.sin(x2) ** 2)

x = np.linspace(0, np.pi/2, 7)
y = f(np.radians(15), x)
r = integrate.simpson(y, x)
print("Wartość h(15)=",r)

y = f(np.radians(30), x)
r = integrate.simpson(y, x)
print("Wartość h(30)=",r)

y = f(np.radians(45), x)
r = integrate.simpson(y, x)
print("Wartość h(45)=",r)

y = f(np.radians(0), x)
r = integrate.simpson(y, x)
print("Wartość h(0)=",r)

print("Wartość pi/2:", np.pi/2)