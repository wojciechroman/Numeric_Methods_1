import numpy as np
from scipy import integrate

def f(x):
    return np.cos(2 * np.cos(x) ** (-1))

x = np.linspace(-1, 1, 3)
r = integrate.simpson(f(x), x)
print("Wynik całki dla 3 węzłów = ", r)

x = np.linspace(-1, 1, 5)
r = integrate.simpson(f(x), x)
print("Wynik całki dla 5 węzłów = ", r)

x = np.linspace(-1, 1, 7)
r = integrate.simpson(f(x), x)
print("Wynik całki dla 7 węzłów = ", r)

#Wolfram Alpha podaje wynik całki jako -1.3655444514186058076541992211137823367015... co sugerowałoby, że im wyższy węzeł tym bardziej dokładny wynik otrzymamy