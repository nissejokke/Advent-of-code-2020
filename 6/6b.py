input = open("6/input.txt", "r").read()

# input = """
# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b
# """

groups = list(input.strip().split("\n\n"))

sum = 0
for group in groups:
    lines = group.split("\n")
    result = set(lines[0])
    for line in lines:
        result = result & set(line)
    sum += len(result)
    
print(sum)
