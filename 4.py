f = open("4.txt", "r")
input = f.read()

# input = """
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# """

import re

lines = list(filter(lambda val: len(val) > 0, input.strip().split("\n\n")))

count = 0
for passport in lines:
    matches = re.findall("\w+:[\S]+", passport.replace("\n", " "))
    keys = set()
    for match in matches:
        key = match.split(":")[0]
        keys.add(key)
    keys.add("cid")

    if len(keys) == 8:
        count += 1
print(count)