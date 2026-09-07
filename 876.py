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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        count = 1
        if current is not None:
            while current.next is not None:

                count += 1
                current = current.next

            middle_of_ll = count // 2
            move_again = 0
            current = head

            while middle_of_ll != move_again:
                move_again += 1
                current = current.next

            return current



# -----------------------------
# VS Code testing setup
# -----------------------------

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Currently:
# 1 → 2 → 3 → None

# head of the linked list
head = node1

# Run your solution
solution = Solution()
result = solution.middleNode(head)

print(result)