# demonstration of Hash Table technique to solve problems.
# Problem:
# Given two strings ransomNote and magazine, return true
# if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example:
# Input:  ransomNote = "aa", magazine = "aab"


def canConstruct(ransomNote, magazine):
    # Create a hash table to store frequency of characters in magazine.
    hash_map = {}
    for char in magazine:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    # Now iterate through each character in ransomNote and check its availability in
    for char in ransomNote:
        if char in hash_map and hash_map[char] > 0:
            hash_map[char] -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))
