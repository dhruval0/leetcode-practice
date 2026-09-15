from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.dfs(root1, root2)

    def dfs(self, root1, root2):

        if root1 is None and root2 is None:
            return None

        if root1 is None:
            return root2
        
        if root2 is None:
            return root1
        
        new_root_val = root1.val + root2.val
        new_node = TreeNode(new_root_val)
        new_node.left = self.dfs(root1.left, root2.left)
        new_node.right = self.dfs(root1.right, root2.right)

        return new_node
        

# Create tree
root1 = TreeNode(1)

root1.left = TreeNode(3)
root1.left.left = TreeNode(5)

root1.right = TreeNode(2)

# Create tree
root2 = TreeNode(2)

root2.left = TreeNode(1)
root2.left.right = TreeNode(4)

root2.right = TreeNode(3)
root2.right.right = TreeNode(7)


# Test
solution = Solution()
result = solution.mergeTrees(root1, root2)

print(result)