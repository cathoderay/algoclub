# problem: https://leetcode.com/problems/balanced-binary-tree/
# space: O(1) | time: O(n)


def is_balanced(root):
    balanced = True
      
    def dfs(root):
        nonlocal balanced
        if root is None: return 0
          
        left = dfs(root.left)
        right = dfs(root.right)

        if abs(left - right) > 1: 
            balanced = False
        return 1 + max(left, right)

    dfs(root)
    return balanced
