from collections import Counter


def word_search(input, target, d):
    visited = set()

    def bfs(cords, x, y, dir=None):
        if cords and tuple(cords) in visited:
            return 0

        word = ''.join(input[x][y] for x, y in cords)
        if word == target:
            visited.add(tuple(cords))
            # print(cords)
            return 1

        if len(word) > 4:
            return 0

        for dx in d:
            for dy in d:
                if dx == 0 and dy == 0:
                    continue

                if x + dx < 0 or x + dx >= len(input) or y + dy < 0 or y + dy >= len(input[0]):
                    continue

                if dir and (dx, dy) != dir:
                    continue

                cord = (x + dx, y + dy)
                cords.append(cord)
                bfs(cords, cord[0], cord[1], (dx, dy))
                cords.remove(cord)

    for x in range(len(input)):
        for y in range(len(input[0])):
            bfs([(x, y)], x, y)

    return visited


with open('inputs/day_04.txt', 'r') as f:
    lines = f.readlines()
    print(len(word_search(lines, "XMAS", [-1, 0, 1])))
    res2 = [tup[1] for tup in word_search(lines, "MAS", [-1, 1])]
    counter = Counter(res2)
    print(sum(1 for num in counter if counter[num] == 2))
