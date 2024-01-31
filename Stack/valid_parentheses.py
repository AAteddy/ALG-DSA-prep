# demonstration for Valid Parentheses problem solution
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Example:
# Input: s = "()[]{}"  Output: true
# Input: s = "(]"  Output: false


def isValid(s) -> bool:
    stack = []
    str_dic = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # check if char is an open parenthesis if so append to stack
        if char in str_dic.values():
            stack.append(char)
        elif char in str_dic.keys():  # check if char is closing parenthesis
            # if stack is empty or last element in stack isn't corresponding opening bracket return False
            if not stack or stack[-1] != str_dic[char]:
                return False
            else:
                # remove last element from stack as it is now fully processed
                stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    s = "()[]{}"
    print(isValid(s))  # should output True
    s = "(]"
    print(isValid(s))  # should output False
