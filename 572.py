from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False

        return (
            self.sameTree(root, subRoot)
            or
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, node, subRoot):

        if node is None and subRoot is None:
            return True

        if node is None or subRoot is None:
            return False
        
        if node.val != subRoot.val:
            return False

        left_child = self.sameTree(node.left, subRoot.left)
        right_child = self.sameTree(node.right, subRoot.right)
        
        return left_child and right_child

# Create tree
root1 = TreeNode(3)

root1.left = TreeNode(4)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)

root1.right = TreeNode(5)

# Create tree
root2 = TreeNode(4)

root2.left = TreeNode(1)

root2.right = TreeNode(2)
# root2.right.right = TreeNode(0)

# Test
solution = Solution()
result = solution.isSubtree(root1, root2)

print(result)