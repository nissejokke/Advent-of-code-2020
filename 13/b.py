input = open("13/input.txt", "r").read()
# 1890502625454599
#

# input = """
# 939
# 7,13,x,x,59,x,31,19
# """
# 1068781
# 3162341

# input = """
# 939
# 1789,37,47,1889
# """
# 1202161486
# 5465967480
# 5876813119

# input = """
# 111
# 17,x,13,19
# """

# input = """
# 111
# 13,17,19
# """
# 3417
# 2992
# 4199
t=2
13 2 (% 13)
1 * t = 2

2%13

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

n = 1
for busline in buslines:
    n*=busline[1]
print("upper:", n)

from datetime import datetime
time = datetime.now()

busline_count = len(buslines)
while True:
    p = buslines[0]
    t += p[1] # 59
    off = p[0] # 4
    n = 0
    for i in range(1, busline_count):
        boff,bid = buslines[i]
        if (t + boff - off) % bid == 0:
            n += 1
        else:
            break
    if n == busline_count - 1:
        break
    
    if (datetime.now() - time).seconds > 3:
        time = datetime.now()
        print(t)

print(t - buslines[0][0])