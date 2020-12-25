from scipy.optimize import fsolve
import numpy as np

def func(parameters):
    x, y = parameters
    return [np.tan(x) - y - 1,
            np.cos(x) - 3 * np.sin(y)]

solution = list()

for x in np.arange(0, 1.5, 0.01):
    for y in np.arange(0, 1.5, 0.01):
        root = fsolve(func, [x, y])
        solution.append([root[0], root[1]])

print(solution)