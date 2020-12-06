input = open("input.txt", "r").read()

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

lines = list(input.strip().split("\n\n"))

sum = 0
for line in lines:
    answers = line.replace("\n", "")
    s = set()
    for ans in answers:
        s.add(ans)
    sum += len(s)
    print(s)
print(sum)