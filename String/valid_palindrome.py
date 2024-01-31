# demonstration of Valid Palindrome problem solution
# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Problem: Given a string s, return true if it is a palindrome, or false otherwise.
# Example:
# Input: "A man, a plan, a canal: Panama"
# Output: True

# Explanation: The deficiencies of this approach are
# 1. dependability and usage of builtin functions (e.g: isalnum())
# 2. Extra memory usage. We needed to create two new strings from original one (newStr and its reverse).


def isPalindrome(s) -> bool:
    newStr = ""

    for char in s:
        #  Check if character is alphanumeric
        if char.isalnum():
            # Convert to lower case and store it in a variable
            newStr += char.lower()
    #  Compare the stored string with its reverse
    return newStr == newStr[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    s = "race a car"
    print(isPalindrome(s))
