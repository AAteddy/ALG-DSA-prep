# demonstration of Binary Search problem solution
#
# Problem:
# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
# Example:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4


def search(nums, target):
    left = 0
    right = len(nums) - 1
    mid = 0
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
