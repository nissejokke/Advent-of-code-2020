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

x = 0
y = 0
lines = list(filter(lambda val: len(val) > 0, input.split("\n")))

trees = 0
while y < len(lines):
    if lines[y][x % len(lines[1])] == "#":
        trees += 1
    x += 3
    y += 1
print(trees)