input = open("9/input.txt", "r").read()

# input = """
# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# """

nums = [int(x) for x in input.strip().split("\n")]

def is_valid(index: int, size: int) -> bool:
    lower = max(index-size, 0)
    num = nums[index]
    numbers = nums[lower:index]
    for xi,x in enumerate(numbers):
        for yi,y in enumerate(numbers):
            if xi != yi:
                if x + y == num:
                    return True
    return False

size = 25
for i in range(size, len(nums)):
    result = is_valid(i, size)
    if result == False:
        print(nums[i])
        break

