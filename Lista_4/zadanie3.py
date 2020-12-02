import numpy as np

u = 2510
M0 = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81

def v(t):
    return u * np.log(M0/(M0 - (m*t))) - g*t
t=0
while v(t) <= 335:
         t=t+0.01
print("Czas wymagany do osiągnięcia zadanej prędkości to:", t)
