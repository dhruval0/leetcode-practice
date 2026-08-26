from typing import Optional

# -----------------------------
# Linked List Node
# -----------------------------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# -----------------------------
# Your LeetCode solution
# -----------------------------
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()
        current = head

        if head is not None:
            while current.next is not None:

                if current.next in visited:
                    return True
                else:
                    visited.add(current)
                
                current = current.next
        
        return False


# -----------------------------
# VS Code testing setup
# -----------------------------

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

# Currently:
# 1 → 2 → 3 → 4 → None

# head of the linked list
head = node1

# Run your solution
solution = Solution()
result = solution.hasCycle(head)

print(result)