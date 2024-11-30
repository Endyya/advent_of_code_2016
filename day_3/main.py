import numpy as np

with open('input') as f:
    data = np.genfromtxt(f, dtype = np.int32)

check_first = data[:, 1] + data[:, 2] > data[:, 0]
check_second = data[:, 0] + data[:, 2] > data[:, 1]
check_third = data[:, 0] + data[:, 1] > data[:, 2]



print('part 1 :', sum(check_first * check_second * check_third))
