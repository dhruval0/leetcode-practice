from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False

        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)
        if  left_subtree is True and right_subtree is True:
            return True

        return False


# Create first tree
p = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(7)

# Create first tree
q = TreeNode(4)
q.left = TreeNode(2)
q.right = TreeNode(7)

# Test
solution = Solution()

result = solution.isSameTree(p, q)

print(result)