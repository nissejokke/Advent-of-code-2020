input = open("13/input.txt", "r").read()

# input = """
# 939
# 7,13,x,x,59,x,31,19
# """

lines = input.strip().split("\n")

timestamp = int(lines[0])
rawlines = lines[1].split(",")
buslines = []
for line in rawlines:
    if line != "x":
        buslines.append(int(line))

waits = []
for busline in buslines:
    div = (timestamp / busline)
    val = round((1 - (div - int(div))) * busline)
    waits.append((busline, val))

result = sorted(waits, key=lambda x: x[1])
print(result[0][0] * result[0][1])

