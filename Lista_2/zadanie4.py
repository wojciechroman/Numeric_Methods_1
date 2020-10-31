from math import sqrt

for n in range(2, 24, 2):
    x = 2**(-n)
    y = (x**4)/(sqrt(x**4 + 4) + 2)
    print(y)
