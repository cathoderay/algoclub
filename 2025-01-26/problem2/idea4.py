def is_balanced(root):
    def dfs(root, height):
        if root is None: return height, True
      
        left, balanced = dfs(root.left, height + 1)
        if not balanced: return height, False

        right, balanced = dfs(root.right, height + 1)
        if not balanced: return height, False

        if abs(left - right) <= 1:
            return max(left, right), True
        return height, False
    return dfs(root, 0)[1]
