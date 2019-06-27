# https://www.codewars.com/kata/roboscript-number-2-implement-the-rs1-specification/train/python



# rotate robot
def execute(code):
    robot_direction = (0, 1)  # initial direction
    robot_path = [(0, 0), ]  # path coordinates

    def rotate(initial, direction):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # rotations
        if direction == 'L':
            idx = directions.index(initial) + 1
            return directions[idx if idx <= 3 else 0]
        elif direction == 'R':
            idx = directions.index(initial) - 1
            return directions[idx if idx >= 0 else 3]


    def action(cmd, direction, path):  # execute single action, L, R, F
        # global robot_direction, robot_path
        if cmd in ['L', 'R']:  # rotations
            direction = rotate(direction, cmd)
        elif cmd == 'F':  # move
            path.append((path[-1][0] + direction[0],
                         path[-1][1] + direction[1]))
        return [path, direction]


    last_action = ''  # last read action
    repeats = ''
    for step in code:
        if step.isalpha():  # rotation&movement
            if repeats:  # do previous action N times
                for i in range(int(repeats) - 1):
                    robot_path, robot_direction = action(last_action, robot_direction, robot_path)
                repeats = ''
                robot_path, robot_direction = action(step, robot_direction, robot_path)
            else:  # move once
                robot_path, robot_direction = action(step, robot_direction, robot_path)
            last_action = step
        else:  # number of repeats
            repeats += step
    # if lst command was repeat
    if repeats:  # do previous action N times
                for i in range(int(repeats) - 1):
                    robot_path, robot_direction = action(last_action, robot_direction, robot_path)
    # grafically interpret
    y, x = [i[0] for i in robot_path], [i[1] for i in robot_path]
    sizeX = max(x) - min(x) + 1
    sizeY = max(y) - min(y) + 1
    robot_map = [[' ' for i in range(sizeX)] for k in range(sizeY)]

    # set path
    for step in robot_path:
        robot_map[step[0]-min(y)][step[1]-min(x)] = '*'
    return '\r\n'.join([''.join(i) for i in robot_map])


print(execute("LF5RF3RF3RF7"))
