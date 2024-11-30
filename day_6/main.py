import numpy as np
data = []

with open('input') as f:

    for line in f:
        data.append(line.rstrip('\n'))
data  = [list(line) for line in data]
data = np.array(data)
data = data.transpose()

def find_most_common(line, invert = False):
    counting = {}
    for char in line:
        if char not in counting.keys():
            counting[char] = 1
        else:
            counting[char] += 1

    sort_count = sorted(counting.items(),
                        key = lambda item: item[1],
                        reverse = True)
    if invert:
        return sort_count[-1][0]
    else:
        return sort_count[0][0]

corrected = ''
corrected2 = ''

for i in range(data.shape[0]):
    line = ''.join(data[i, :])
    corrected += find_most_common(line)
    corrected2 += find_most_common(line, invert = True)

print('part 1 :', corrected)
print('part 2 :', corrected2)
