f = open("4.txt", "r")
input = f.read()

# input = """
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# """

import re

lines = list(filter(lambda val: len(val) > 0, input.strip().split("\n\n")))

count = 0
for passport in lines:
    # print(passport)
    matches = re.findall("\w+:[\S]+", passport.replace("\n", " "))
    keys = set()
    for match in matches:
        vals = match.split(":")
        key = vals[0]
        value = vals[1]

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if key == "byr":
            v = int(value)
            if v >= 1920 and v <= 2002:
                keys.add(key)
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if key == "iyr":
            v = int(value)
            if v >= 2010 and v <= 2020:
                keys.add(key)
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if key == "eyr":
            v = int(value)
            if v >= 2020 and v <= 2030:
                keys.add(key)
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        if key == "hgt" and len(value) > 0:
            num = value[:-2]
            if len(num) > 0:
                h = int(num)
                suf = value[-2:]
                if suf == "cm" and h >= 150 and h <= 193:
                    keys.add(key)
                if suf == "in" and h >= 59 and h <= 76:
                    keys.add(key)
                    
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if key == "hcl":
            if re.search("#[a-f0-9]{6}", value):
                keys.add(key)
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if key == "ecl":
            if re.search("(amb|blu|brn|gry|grn|hzl|oth)", value):
                keys.add(key)  
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if key == "pid":
            if re.search("^[\d]{9}$", value):
                keys.add(key)  

    keys.add("cid")

    if len(keys) == 8:
        count += 1
        
print(count)