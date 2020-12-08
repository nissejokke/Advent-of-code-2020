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
    
def run(instructions) -> (int, bool):
    acc = 0
    index = 0
    visited = set()
    normal_termination = True
    while index < len(instructions):
        if index in visited:
            normal_termination = False
            break

        visited.add(index)

        try:
            instruction = instructions[index]
        except:
            normal_termination = False
            break

        instr = instruction[0]
        arg = instruction[1]

        if instr == "acc":
            acc += arg
            index += 1
        if instr == "jmp":
            index += arg
        if instr == "nop":
            index += 1

    return (acc, normal_termination)

def mutate(instructions, index):
    if instructions[index][0] == "acc":
        return instructions

    instructions = instructions.copy()
    instruction = instructions[index]
    if instruction[0] == "nop":
        instruction = ("jmp", instruction[1])
    elif instruction[0] == "jmp":
        instruction = ("nop", instruction[1])

    instructions[index] = instruction
    return instructions

for i in range(len(instructions)):
    mutated_instructions = mutate(instructions, i)
    res = run(mutated_instructions)

    if res[1] == True:
        print(res[0])
        break
