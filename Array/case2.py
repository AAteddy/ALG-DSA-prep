# demonstration of the two pointers technique for finding a pair of numbers in a sorted array that add up to a specific target.
# Two Pointers in a Single Array: Often used in problems involving a sorted array where you need to find a pair of elements that meet certain criteria. The pointers typically start at opposite ends of the array and move towards each other.
# This technique can simplify the logic and reduce the time complexity of certain problems.
# Problem: find a pair of numbers in a sorted array that add up to a specific target


def pairsum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return "none", "none"


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 1
    result = pairsum(nums, target)
    print("The two elements are {} and {}".format(*result))
