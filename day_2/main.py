
code = ''
current_number = 5

# open the input file
with open("input") as f:

    for line in f:
        print(line)
        for inst in line:
            if (inst == 'U' and current_number < 4
                or inst == 'D' and current_number > 6
                or inst == 'L' and current_number in [1, 4, 7]
                or inst == 'R' and current_number in [3, 6, 9]):
                pass
            elif inst == 'U':
                current_number -= 3
            elif inst == 'D':
                current_number += 3
            elif inst == 'L':
                current_number -= 1
            elif inst == 'R':
                current_number += 1
                



        code = code + str(current_number)

print("part 1 answer :", code)
print("part 2 answer :", code)
