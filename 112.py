from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False

        current_sum = root.val
        return self.dfs(root, current_sum, targetSum)

    def dfs(self, node, current_sum, targetSum):

        if node is None:
            return False

        if node.left is None and node.right is None:
            if current_sum == targetSum:
                return True
            return False
        
        left_result = False
        right_result = False

        if node.left is not None:
            left_sum = current_sum + node.left.val
            left_result = self.dfs(node.left, left_sum, targetSum)

        if node.right is not None:
            right_sum = current_sum + node.right.val
            right_result = self.dfs(node.right, right_sum, targetSum)
        
        return (left_result or right_result)

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
targetSum = 22
result = solution.hasPathSum(root, targetSum)

print(result)