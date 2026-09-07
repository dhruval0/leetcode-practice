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
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy_node = ListNode("7987")
        dummy_node.next = head

        slow_pointer = dummy_node
        fast_pointer = dummy_node

        for _ in range(n):
            fast_pointer = fast_pointer.next

        while fast_pointer.next is not None:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

        slow_pointer.next = slow_pointer.next.next

        return dummy_node.next

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
result = solution.removeNthFromEnd(head, 2)

print(result)