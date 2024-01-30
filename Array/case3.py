# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# Problem Set-up:
#  Array - nums :[2, 7, 11, 15]
#  Target Value - target = 9

# Solution: Using hash map technique


def two_sum(nums, target):
    prevMap = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in prevMap:
            return [prevMap[complement], i]
        else:
            prevMap[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
