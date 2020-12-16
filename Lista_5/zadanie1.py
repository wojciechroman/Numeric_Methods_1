from scipy import optimize
import numpy as np
import math as m

list_x = [0,3,6]
list_y = [1.225,0.905,0,652]
def f(parameters):
    parameters = [a,b,c,x]
    y = a*x*x+b*x+c
    return y

if __name__ == "__main__":
    ans=list()
    i = 0
    for x in list_x:
        for a in np.arange(0.1, 20, 0.1):
            for b in np.arange(0.1, 20, 0.1):
                for c in np.arange(0.1, 20, 0.1):
                    root = optimize.fsolve(f, [a, b, c, x])
                    if root == list_y[i]:
                        ans.append(root)
        i=i+1

print(ans)

