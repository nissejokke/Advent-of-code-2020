f = open("3.txt", "r")
input = f.read()

# input = """
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# """

lines = list(filter(lambda val: len(val) > 0, input.split("\n")))

def getSlopes(dx, dy):
    x = 0
    y = 0
    trees = 0
    while y < len(lines):
        if lines[y][x % len(lines[1])] == "#":
            trees += 1
        x += dx
        y += dy
    return trees

print(getSlopes(1, 1) * getSlopes(3, 1) * getSlopes(5, 1) * getSlopes(7, 1) * getSlopes(1, 2))