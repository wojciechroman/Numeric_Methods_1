from numpy import linalg
from scipy.linalg import hilbert

m5c=linalg.cond(hilbert(5))
m5n=linalg.norm(hilbert(5))
m10c=linalg.cond(hilbert(10))
m10n=linalg.norm(hilbert(10))
m15c=linalg.cond(hilbert(15))
m15n=linalg.norm(hilbert(15))
print("Wskaźnik unormowania macierzy: ", m5c, "norma: ", m5n)
print("Wskaźnik unormowania macierzy: ", m10c, "norma: ", m10n)
print("Wskaźnik unormowania macierzy: ", m15c, "norma: ", m15n)
