from collections import Counter


def parse_lines(input):
    l1, l2 = [], []
    for line in input:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))

    return l1, l2


def sum_of_diff(input):
    l1,  l2 = parse_lines(input)
    return sum(abs(sorted(l1)[i] - sorted(l2)[i]) for i in range(len(l1)))

def calculate_similarity(input):
    l1, l2 = parse_lines(input)
    counter_2 = Counter(l2)
    return sum(i * counter_2[i] for i in l1)


with open('inputs/day_01.txt', 'r') as f:
    lines = f.readlines()
    print(sum_of_diff(lines))
    print(calculate_similarity(lines))