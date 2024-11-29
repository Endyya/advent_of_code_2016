def find_distance(line):
    current_dir = 'N'
    current_coord = [0, 0]
    for inst in line.split(', '):
        dir_inst = inst[0]
        step_number = int(inst[1:])

        if ((current_dir == 'N' and dir_inst == 'L')
            or (current_dir == 'S' and dir_inst == 'R')):
            current_dir = 'W'
            current_coord[0] -= step_number
        elif ((current_dir == 'N' and dir_inst == 'R')
            or (current_dir == 'S' and dir_inst == 'L')):
            current_dir = 'E'
            current_coord[0] += step_number
        elif ((current_dir == 'W' and dir_inst == 'R')
            or (current_dir == 'E' and dir_inst == 'L')):
            current_dir = 'N'
            current_coord[1] += step_number
        elif ((current_dir == 'W' and dir_inst == 'L')
            or (current_dir == 'E' and dir_inst == 'R')):
            current_dir = 'S'
            current_coord[1] -= step_number            

    return abs(current_coord[0]) + abs(current_coord[1])



# open the input file
with open("input") as f:

    line = f.readline()

print("part 1 answer :", find_distance(line))
print("part 2 answer :", 0)
