from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        # Both nodes are empty
        if p is None and q is None:
            return True

        # Only one node is empty
        if p is None or q is None:
            return False

        # Current node values must match
        if p.val != q.val:
            return False

        # Compare opposite child nodes
        return (
            self.isMirror(p.left, q.right)
            and self.isMirror(p.right, q.left)
        )


# Create tree
root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# root = TreeNode(1)

# root.left = TreeNode(2)
# root.left.right = TreeNode(3)

# root.right = TreeNode(2)
# root.right.right = TreeNode(3)

# root = TreeNode(1)

# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)

# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)

# Test
solution = Solution()

result = solution.isSymmetric(root)

print(result)