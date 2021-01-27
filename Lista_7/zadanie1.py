
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y,t):
    dydt = np.sin(t*y)
    return dydt

# time points
t = np.linspace(0,6)

# solve ODEs

y1 = odeint(model,2,t)
y2 = odeint(model,2.5,t)
y3 = odeint(model,3,t)
y4 = odeint(model,3.5,t)
# plot results
plt.plot(t,y1, label="y=2")
plt.plot(t,y2, label="y=2.5")
plt.plot(t,y3, label="y=3")
plt.plot(t,y4, label="y=3.5")
plt.legend()
plt.show()