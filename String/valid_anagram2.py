# demonstration of Valid Anagram problem solution
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
# Problem:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true

#  Approach: Sorting technique
# time:  O(nlogn) - sorting takes n log n time
# space: O(1)     - in-place sorting (does not count towards extra space because we are modifying input string directly)


def isAnagram(s, t):
    # Check if both strings have equal length, else they cannot be anagrams
    if len(s) != len(t):
        return False

    # sort both strings & Compare sorted strings
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    s = "rat"
    t = "car"
    print(isAnagram(s, t))
