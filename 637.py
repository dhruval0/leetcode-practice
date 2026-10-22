from collections import deque
from typing import Optional
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result


# GO code

# /**
#  * Definition for a binary tree node.
#  * type TreeNode struct {
#  *     Val   int
#  *     Left  *TreeNode
#  *     Right *TreeNode
#  * }
#  */

# func averageOfLevels(root *TreeNode) []float64 {
#     if root == nil {
#         return []float64{}
#     }

#     queue := []*TreeNode{root}
#     result := []float64{}

#     for len(queue) > 0 {
#         levelSize := len(queue)
#         levelSum := 0

#         for i := 0; i < levelSize; i++ {
#             node := queue[0]
#             queue = queue[1:]

#             levelSum += node.Val

#             if node.Left != nil {
#                 queue = append(queue, node.Left)
#             }

#             if node.Right != nil {
#                 queue = append(queue, node.Right)
#             }
#         }

#         average := float64(levelSum) / float64(levelSize)
#         result = append(result, average)
#     }

#     return result
# }
