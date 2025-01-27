# problem: https://leetcode.com/problems/balanced-binary-tree/
# space: O(1) | time: O(n)


def height(root):
    if root is None: return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    if root is None: return True
    return is_balanced(root.left) and \
           is_balanced(root.right) and \
           abs(height(root.left) - height(root.right)) <= 1
