import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def f(y, x):
    return  (y[1], 4 * y[1] - 9 * y[0])

y0 = [0, -8]
x = np.linspace(0, 2,99999)
u = odeint(f, y0, x)
y = u[:,0]
plt.plot(x, y)
plt.show()
ans=[]
for i in range(len(y)):
    if (y[i]<0 and y[i+1]>0):
        ans.append(i)
        ans.append(i+1)
    if y[i]==0:
        ans0=i
x0=[]
x0.append(x[ans0])
x0.append((x[ans[0]]+x[ans[1]])/2)
print(x0)