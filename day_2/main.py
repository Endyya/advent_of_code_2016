
def get_number(start, inst, part = 1):
    current_number = start
    if part == 1:
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
        return current_number
    else:
        if (inst == 'U' and current_number in [5, 2, 1, 4, 9]
            or inst == 'D' and current_number in [5, 10, 13, 12, 9]
            or inst == 'L' and current_number in [1, 2, 5, 10, 13]
            or inst == 'R' and current_number in [1, 4, 9, 12, 13]):
            pass
        elif inst == 'U' and current_number in [6, 7, 8, 10, 11, 12]:
            current_number -= 4
        elif inst == 'U' and current_number in [3, 13]:
            current_number -= 2
        elif inst == 'D' and current_number in [2, 3, 4, 6, 7, 8]:
            current_number += 4
        elif inst == 'D' and current_number in [1, 11]:
            current_number += 2
        elif inst == 'L':
            current_number -= 1
        elif inst == 'R':
            current_number += 1
    return current_number
        
            

code1 = code2 = ''
current_number1 = current_number2 = 5

# open the input file
with open("input") as f:

    for line in f:
        for inst in line:
            current_number1 = get_number(current_number1, inst)
            current_number2 = get_number(current_number2, inst, part = 2)
                


            


        code1 = code1 + str(current_number1)
        if current_number2 > 9:
            letters = ['A', 'B', 'C', 'D']
            code2 = code2 + letters[current_number2 - 10]
        else:
            code2 = code2 + str(current_number2)

print("part 1 answer :", code1)
print("part 2 answer :", code2)
