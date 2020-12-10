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
ratings.append(0)
ratings.sort()
ratings.append(ratings[-1] + 3)

cache = dict()

def find_total_matches(index: int) -> int:
    org_val = ratings[index]
    if org_val in cache:
        return cache[org_val]
    val = org_val
    index += 1
    child_indices = []
    tot = 0
    while index < len(ratings):
        val = ratings[index]
        if val <= org_val + 3:
            child_indices.append(index)
        index += 1

    for ind in child_indices:
        tot += find_total_matches(ind)

    result = max(1, tot)
    cache[org_val] = result
    return result

tot = find_total_matches(0)
print(tot)
