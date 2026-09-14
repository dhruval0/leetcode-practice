from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        self.max_diame = 0
        self.dfs(root)

        return self.max_diame

    def dfs(self, node):

        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.max_diame = max(self.max_diame, left + right)
        return max(left, right) + 1

# Create tree
root = TreeNode(5)

root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


# Test
solution = Solution()
result = solution.diameterOfBinaryTree(root)

print(result)