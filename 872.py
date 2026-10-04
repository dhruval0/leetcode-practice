from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:

        leaves1 = []
        leaves2 = []
        return self.dfs(root1, leaves1) == self.dfs(root2, leaves2)

    def dfs(self, node, leaves):

        if node is None:
            return leaves

        if node.left is None and node.right is None:
            leaves.append(node.val)

        if node.left is not None:
            self.dfs(node.left, leaves)

        if node.right is not None:
            self.dfs(node.right, leaves)

        return leaves


# Create tree
root1 = TreeNode(3)

root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)


root2 = TreeNode(3)

root2.left = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)

root2.right = TreeNode(1)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)


# Test
solution = Solution()

result = solution.leafSimilar(root1, root2)

print(result)