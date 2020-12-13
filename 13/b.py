input = open("13/input.txt", "r").read()

# input = """
# 939
# 7,13,x,x,59,x,31,19
# """

input = """
939
1789,37,47,1889
"""

lines = input.strip().split("\n")

timestamp = int(lines[0])
rawlines = lines[1].split(",")
buslines = []
i = 0
for line in rawlines:
    if line != "x":
        buslines.append((i, int(line)))
    i += 1
buslines = sorted(buslines, key=lambda x: x[1], reverse=True)
print(buslines)
t = 0
# for busline in buslines:
#     t*=busline[1]
# print(t)
while True:
    p = buslines[0]
    t += p[1] # 59
    off = p[0] # 4
    n = 0
    for i in range(1, len(buslines)):
        boff,bid = buslines[i]
        if (t + boff - off) % bid == 0:
            n += 1
        else:
            break
    if n == len(buslines) - 1:
        break
    # if t % 1000 == 0:
    #     print(t)
print(t - buslines[0][0])