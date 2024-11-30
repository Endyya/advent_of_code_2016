
def find_distance(line, part = 1):
    current_dir = 'N'
    current_coord = [0, 0]
    traj = [current_coord[::]]
    for inst in line.split(', '):
        dir_inst = inst[0]
        step_number = int(inst[1:])

        if ((current_dir == 'N' and dir_inst == 'L')
            or (current_dir == 'S' and dir_inst == 'R')):
            current_dir = 'W'
            for _ in range(step_number):
                current_coord[0] -= 1
                if current_coord in traj and part == 2:
                    return abs(current_coord[0]) + abs(current_coord[1])
                traj.append(current_coord[::])

        elif ((current_dir == 'N' and dir_inst == 'R')
            or (current_dir == 'S' and dir_inst == 'L')):
            current_dir = 'E'
            for _ in range(step_number):
                current_coord[0] += 1
                if current_coord in traj and part == 2:
                    return abs(current_coord[0]) + abs(current_coord[1])
                traj.append(current_coord[::])

        elif ((current_dir == 'W' and dir_inst == 'R')
            or (current_dir == 'E' and dir_inst == 'L')):
            current_dir = 'N'
            for _ in range(step_number):
                current_coord[1] += 1
                if current_coord in traj and part == 2:
                    return abs(current_coord[0]) + abs(current_coord[1])
                traj.append(current_coord[::])            

        elif ((current_dir == 'W' and dir_inst == 'L')
            or (current_dir == 'E' and dir_inst == 'R')):
            current_dir = 'S'
            for _ in range(step_number):
                current_coord[1] -= 1
                if current_coord in traj and part == 2:
                    return abs(current_coord[0]) + abs(current_coord[1])
                traj.append(current_coord[::])



        
    return abs(current_coord[0]) + abs(current_coord[1])

        



# open the input file
with open("input") as f:

    line = f.readline()

print("part 1 answer :", find_distance(line))
print("part 2 answer :", find_distance(line, part = 2))
