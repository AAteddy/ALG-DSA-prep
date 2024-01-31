# demonstration of Flip/Invert Binary Tree problem solution
# Given the root of a binary tree, invert the tree, and return its root.
# Example:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Implementation technique: recursion approach


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root):
        if not root:
            return None
        # flipping the tree by swapping left and right subtrees
        root.left, root.right = root.right, root.left
        # recursively calling function to invert the rest of the tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    t = TreeNode(1, 2, 3)
    print(t.invertTree(1))
