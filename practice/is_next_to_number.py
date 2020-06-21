"""
    Just a routine practice: The idea is to return True if 3 is next to the other.
"""


def is_next1(nums):
    for i in range(len(nums)):
        try:
            if nums[i] == 3 and nums[i+1] == 3:
                return True
        except IndexError:
            return False


def is_next2(nums):
    for x in range(0, len(nums)-1):
        if nums[x] == 3 and nums[x+1] == 3:
            return True
    return False


print("Test 1: {0}".format(is_next1([1, 3, 3])))
print("Test 2: {0}".format(is_next1([1, 3, 1, 3])))
print("Test 3: {0}".format(is_next1([3, 1, 3])))

print("Test 1: {0}".format(is_next2([1, 3, 3])))
print("Test 2: {0}".format(is_next2([1, 3, 1, 3])))
print("Test 3: {0}".format(is_next2([3, 1, 3])))

