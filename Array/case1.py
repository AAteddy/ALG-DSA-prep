# Find the maximum or minimum sum of all subarrays of a fixed size.
# Use Sliding Window technique


def subarray_sum(arr, k):
    maxsum = 0
    windowsum = 0

    for i in range(0, k):
        windowsum += arr[i]

    maxsum = windowsum
    j = k
    length = len(arr)
    for j in range(k, length):
        windowsum += arr[j] - arr[j - k]
        maxsum = max(maxsum, windowsum)

    return maxsum


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Maximum Sum Subarray:", subarray_sum(arr, k))
