def is_balanced(root):
    balanced = True
      
    def dfs(root, height):
        nonlocal balanced
        if root is None: return height
          
        left = dfs(root.left, height + 1)
        right = dfs(root.right, height + 1)

        if abs(left - right) > 1: balanced = False
        return max(left, right)

    dfs(root, 0)
    return balanced
