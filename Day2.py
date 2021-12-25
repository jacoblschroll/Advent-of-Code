hx = 0
depth = 0
aim = 0

action_list = []

def parse_input(file, action_list):
    with open(file, 'r') as f:
        for line in f:
            action_list.append((line.replace('\n', '')).replace(' ', ''))

def run_depth(action_list):
    temp = 0
    for action in action_list:
        if action[0] == 'u':
            temp = temp - int(action[2])
        if action[0] == 'd':
            temp = temp + int(action[4])
    return temp

def run_x(action_list):
    temp_hx = 0
    for action in action_list:
        if action[0] == 'f':
                temp_hx = temp_hx + int(action[7])
    return temp_hx

def run_aim(action_list):
    depth = 0
    aim = 0
    for action in action_list:
        if action[0] == 'u':
            aim = aim - int(action[2])
        if action[0] == 'd':
            aim = aim + int(action[4])
        if action[0] == 'f':
            depth = depth + (aim * int(action[7]))
    return depth

parse_input('day2input.txt', action_list)

depth = run_depth(action_list)
hx = run_x(action_list)

aim = run_aim(action_list)

print(hx)
print(depth)
print(aim)

print(hx * depth)

print(hx * aim)