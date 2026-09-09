from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root




# Create tree
root = TreeNode(4)

root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)

root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


# Test
solution = Solution()

result = solution.invertTree(root)

print(result)