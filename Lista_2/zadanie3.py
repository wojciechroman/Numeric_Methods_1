from math import sqrt

for n in range(2, 24, 2):
    x = 2**(-n)
    y1 = sqrt(x**2 + 1) - 1
    y2 = (x**2)/(sqrt(x**2 + 1)+1)
    print(y1)
    print(y2)

    #bardziej dokładna jest druga wersja równania
