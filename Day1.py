measurements = []

increases = 0
last = 0

window_list = []

with open('day1input.txt', "r") as f:
    for line in f:
        measurements.append(int(line.replace("\n", '')))

last = measurements[0]

for depth in measurements:
    if depth > last:
        increases = increases + 1
    last = depth

increases = 0

for i in range(0, len(measurements) + 1):
    if (i + 2) < len(measurements):
        window_list.append(measurements[i] + measurements[i + 1] + measurements[i + 2])

last = window_list[0]

for item in window_list:
    if item > last:
        increases = increases + 1
    last = item

print(increases)