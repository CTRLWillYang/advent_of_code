def check_safe_line(line):
    line = [int(x) for x in line]
    line = line if line[-1] > line[0] else line[::-1]
    # print([1 <= int(y) - int(x) <= 3 for x, y in zip(line[:-1], line[1:])])
    return all(1 <= y - x <= 3 for x, y in zip(line[:-1], line[1:]))


def check_safe_line_tolerate(line):
    line = [int(x) for x in line]
    line = line if line[-1] > line[0] else line[::-1]

    for i in range(1, len(line)):
        x, y = line[i - 1], line[i]
        if 1 <= y - x <= 3:
            continue
        if check_safe_line(line[:i] + line[i + 1:]) or check_safe_line(line[:i - 1] + line[i:]):
            continue

        return False

    return True

def check_safe(input, func):
    res = 0
    for line in input:
        if func(line.split()):
            # print(f'line:{line} TRUE')
            res += 1
        # else:
            # print(f'line:{line} FALSE')

    return res


with open('inputs/day_02.txt', 'r') as f:
    lines = f.readlines()
    print(check_safe(lines, check_safe_line))
    print(check_safe(lines, check_safe_line_tolerate))