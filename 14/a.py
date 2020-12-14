input = open("14/input.txt", "r").read()

# input = """
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# """

lines = input.strip().split("\n")
mem = dict()
mask = ""
for line in lines:
    key,value = line.split(" = ")
    key = key.replace("mem[", "").replace("]", "")
    if key != "mask":
        value = int(value)
        mem[key] = value 
        mem[key] |= int(mask.replace("X", "0"), 2)
        mem[key] &= int(mask.replace("X", "1"), 2)
    else:
        mask = value

# print(mem)
print(sum(mem.values()))



