input = open("5.txt", "r").read()

lines = list(filter(lambda val: len(val) > 0, input.strip().split("\n")))

def parseRow(line: str):
    l = 0
    u = 128
    m = 128
    for char in line:
        if char == "B":
            # upper
            if m == 2:
                return max(l,u-1)

            m /= 2
            l += m
            
        elif char == "F":
            # lower
            if m == 2:
                return min(l,u-1)

            m /= 2
            u -= m
            
        # print(char, l, u, m)

def parseCol(line: str):
    l = 0
    u = 8
    m = 8

    for char in line:
        if char == "R":
            # upper
            if m == 2:
                return max(l,u-1)

            m /= 2
            l += m
        elif char == "L":
            # lower
            if m == 2:
                return min(l,u-1)

            m /= 2
            u -= m
    
def getSeatId(row, col):
    return row * 8 + col

ids = []
for line in lines:
    row = parseRow(line)
    col = parseCol(line)
    seatId = getSeatId(row, col)

    ids.append(seatId)

ids.sort()

# visual inspection of which one is missing:

i = 13
for id in ids:
    print(i, id)
    i += 1