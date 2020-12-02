from scipy import optimize

def f(x):
    return (2*x**4+24*x**3+61*x**2-16*x+1)

roots = optimize.ridder(f,-10,-6)
print(roots)
roots = optimize.ridder(f,-5,-3)
print(roots)
roots = optimize.ridder(f,0,0.122)
print(roots)
roots = optimize.ridder(f,0.122,5)
print(roots)