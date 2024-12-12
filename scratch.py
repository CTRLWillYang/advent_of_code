line = [7, 5, 1, 2, 4]
dir = 1 if line[-1] > line[0] else -1

prev = line[0]
for i in line[dir::dir]:
    print(i)