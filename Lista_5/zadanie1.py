from scipy.interpolate import lagrange

x = [0,3,6]
y = [1.225, 0.905, 0.652]

poly = lagrange(x, y)

print(poly)