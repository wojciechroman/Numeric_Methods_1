import numpy as np
import matplotlib.pyplot as plt

x = [1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7]

y = [6.008,15.722,27.13,33.772,5.257,9.549,11.098,28.828]

line = np.polyfit(x,y, 1)
newline = np.poly1d(line)

line2 = np.polyfit(x,y, 2)
newline2 = np.poly1d(line2)

newx = np.linspace(1,3.7,2000)
fig, axs = plt.subplots(3)
fig.suptitle("Lepiej dopasowana jest funkcja kwadratowa")
axs[0].plot(x,y,"go")
for x in newx:
    axs[1].plot(x, newline(x), "go")
    axs[2].plot(x, newline2(x),"go")

plt.show()

