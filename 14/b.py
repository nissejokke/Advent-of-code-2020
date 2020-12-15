input = open("14/input.txt", "r").read()

# input = """
# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# """

import itertools

lines = input.strip().split("\n")
mem = dict()
mask = ""

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

for line in lines:
    key,value = line.split(" = ")
    strkey = key.replace("mem[", "").replace("]", "")
    key = strkey
    if key == "mask":
        mask = value
    else:
        key = int(key)
        value = int(value)

        floats = mask.count("X")
        combs = list(itertools.product('01', repeat=floats))

        temp = key
        for comb in combs:
            index = 0
            for i in range(len(mask)):
                mask_char = mask[-i-1]
                if mask_char == "X":
                    if comb[-index-1] == "1":
                        temp = set_bit(temp, i)
                    else:
                        temp = clear_bit(temp, i)
                    index += 1
                elif mask_char == "1":
                    temp = set_bit(temp, i)
            mem[temp] = value

print(sum(mem.values()))
