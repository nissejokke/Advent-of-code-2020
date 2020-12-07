input = open("7/input.txt", "r").read()

# input = """
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """

lines = input.strip().split("\n")
rules = []
for line in lines:
    words = line.split(" ")
    parentbag = " ".join(words[0:2])
    rest = " ".join(words[4:])
    childstrings = rest.split(", ")
    for childstr in childstrings:
        childwords = childstr.split(" ")
        if childwords[0] == "no":
            childcount = 0
        else:
            childcount = int(childwords[0])
            childbag = " ".join(childwords[1:3])

            rules.append({ "parent": parentbag, "count": childcount, "child": childbag })

matches = set()

def find_bag(bag: str, parentMultiplier: int = 1):
    count = 0
    for rule in rules:
        if rule["parent"] == bag:
            mul = parentMultiplier * rule["count"]
            count += mul
            count += find_bag(rule["child"], mul)
    return count

count = find_bag("shiny gold")
print(count)