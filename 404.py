from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:


        return self.dfs(root)

    def dfs(self, node):

        if node is None:
            return 0

        if node.left is not None and node.left.left is None and node.left.right is None:
            return node.left.val + self.dfs(node.right)

        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)

        return left_sum + right_sum

# Create tree
root = TreeNode(3)

root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Test
solution = Solution()
result = solution.sumOfLeftLeaves(root)

print(result)