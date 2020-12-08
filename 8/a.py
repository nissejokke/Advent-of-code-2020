input = open("8/input.txt", "r").read()

# input = """
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# """

lines = input.strip().split("\n")

instructions = []
for line in lines:
    intr = line[0:3]
    arg = int(line[4:])

    instructions.append((intr, arg))
    
acc = 0
index = 0
visited = dict()
while True:
    if visited.get(index) != None:
        break

    visited[index] = True

    instruction = instructions[index]
    instr = instruction[0]
    arg = instruction[1]

    if instr == "acc":
        acc += arg
        index += 1
    if instr == "jmp":
        index += arg
    if instr == "nop":
        index += 1

print(acc)