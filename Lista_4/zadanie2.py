from scipy import optimize

def newton(x, n):
    y = lambda x, a: x ** n - a
    dy = lambda x, a: n * x ** (n - 1)
    return optimize.newton(y, 3, fprime=dy, args=(x,))
#x to podstawa potęgi
#n to wykładnik potęgi
x = 16
n = 2
print(newton(x, n))