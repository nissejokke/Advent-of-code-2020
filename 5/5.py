input = open("5.txt", "r").read()

# input = """
# FBFBBFFRLR
# BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL
# """
# FFFBBBFRRR
# BBFFBBFRLL

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
            
        # if char == "L" or char == "R":
        #     print(char, l, u, m)
    
def getSeatId(row, col):
    return row * 8 + col

ids = []
for line in lines:
    row = parseRow(line)
    col = parseCol(line)
    seatId = getSeatId(row, col)
    ids.append(seatId)

ids.sort()
print(ids[-1])