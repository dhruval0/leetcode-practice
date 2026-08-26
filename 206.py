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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        current = head

        while current is not None:
            
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous



# -----------------------------
# VS Code testing setup
# -----------------------------

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Connect nodes
node1.next = node2
node2.next = node3

# Currently:
# 1 → 2 → 3 → None

# head of the linked list
head = node1

# Run your solution
solution = Solution()
result = solution.reverseList(head)

print(result)