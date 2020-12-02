f = open("2.txt", "r")
input = f.read()

# input = """
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# """

lines = list(filter(lambda val: len(val) > 0, input.split("\n")))

objs = []
for line in lines:
    parts = line.split(" ")
    objs.append((parts[0].split("-"), parts[1].replace(":", ""), parts[2]))
    
matches = 0
for obj in objs:
    count = obj[2].count(obj[1])
    if count >= int(obj[0][0]) and count <= int(obj[0][1]):
        matches += 1

print(matches)
