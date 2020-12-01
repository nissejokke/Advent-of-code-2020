f = open("1b.txt", "r")
input = f.read()

cleaned_list = list(filter(lambda val: len(val) > 0, input.split("\n")))
vals = list(map(lambda str: int(str), cleaned_list))

for x in range(len(vals)):
    for y in range(len(vals)):
        for z in range(len(vals)):
            if x != y and x != z:
                sum = vals[x] + vals[y] + vals[z]
                if sum == 2020:
                    print(vals[x] * vals[y] * vals[z])
                    break
        else:
            continue
        break
    else:
        continue
    break