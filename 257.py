from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        if root is None:
            return None

        self.result = []
        self.dfs(root, [])

        return self.result

    def dfs(self, node, path):
        
        if path:
            new_path = path + "->" + str(node.val)
        else:
            new_path = str(node.val)

        if node.left is None and node.right is None:
            self.result.append(new_path)
            return

        if node.left is not None:
            self.dfs(node.left, new_path)
        
        if node.right is not None:
            self.dfs(node.right, new_path)


# Create tree
root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(5)

root.right = TreeNode(3)


# Test
solution = Solution()
result = solution.binaryTreePaths(root)

print(result)