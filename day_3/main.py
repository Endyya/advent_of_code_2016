import numpy as np

with open('input') as f:
    data = np.genfromtxt(f, dtype = np.int32)

check_first = data[:, 1] + data[:, 2] > data[:, 0]
check_second = data[:, 0] + data[:, 2] > data[:, 1]
check_third = data[:, 0] + data[:, 1] > data[:, 2]



print('part 1 :', sum(check_first * check_second * check_third))

with open('input') as f:
    data = np.genfromtxt(f, dtype = np.int32)

for i in range(data.shape[0] // 3):
    data[3 * i:3 * i + 3, :] = data[3 * i:3 * i + 3, :].transpose()



check_first = data[:, 1] + data[:, 2] > data[:, 0]
check_second = data[:, 0] + data[:, 2] > data[:, 1]
check_third = data[:, 0] + data[:, 1] > data[:, 2]

print('part 2 :', sum(check_first * check_second * check_third))
