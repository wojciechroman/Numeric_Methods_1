from math import e

in0 = 1

for n in range(2, 20):
    in1 = e - (n + 1) * in0
    print(in1)
    in0 = in1