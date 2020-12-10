input = open("10/input.txt", "r").read()

# input = """
# 16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# """

# input = """
# 28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3
# """

ratings = [int(x) for x in input.strip().split("\n")]
ratings.sort()
ratings.append(ratings[-1] + 3)

prev_rating = 0
diffs = dict()
for rating in ratings:
    diff = rating - prev_rating
    prev_rating = rating
    if diff in diffs:
        diffs[diff] += 1
    else:
        diffs[diff] = 1

# print(diffs)
print(diffs[1]*diffs[3])