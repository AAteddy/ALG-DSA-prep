# demonstration of Valid Anagram problem solution
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
# Problem:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true

#  Approach: Hash map technique


from collections import Counter


def isAnagram(s, t):
    # hash_table = {}

    # # Iterate through first string 's' and store each character in the hash_table dictionary with its count as value
    # for char in s:
    #     if char not in hash_table:
    #         hash_table[char] = 1
    #     else:
    #         hash_table[char] += 1

    # # Now we need to check whether second string 't' is found in the hash_table dictionary
    # for char in t:
    #     if char not in hash_table:
    #         return False
    #     else:
    #         hash_table[char] -= 1

    # # If any value is non-zero then ith character of both strings are not same
    # for key in hash_table.values():
    #     if key != 0:
    #         return False
    # return True
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    s = "rat"
    t = "car"
    print(isAnagram(s, t))
