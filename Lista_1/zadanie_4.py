import scipy.linalg as sci


x = sci.hilbert(4)
y = sci.hilbert(8)

ix = sci.invhilbert(4)
iy = sci.invhilbert(8)

print(x,y,ix,iy)

n = 5

for i in range(15):
    print(sci.det(sci.hilbert(n)))
    n = n+1


