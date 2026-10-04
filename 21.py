from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(
        self,
        list1: ListNode | None,
        list2: ListNode | None
    ) -> ListNode | None:

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

# Create nodes
list1_node1 = ListNode(1)
list1_node2 = ListNode(2)
list1_node3 = ListNode(4)

# Connect nodes
list1_node1.next = list1_node2
list1_node2.next = list1_node3

# Currently:
# 1 → 2 → 4 → None

# head of the linked list
list1_head = list1_node1

# Create nodes
list2_node1 = ListNode(1)
list2_node2 = ListNode(3)
list2_node3 = ListNode(4)

# Connect nodes
list2_node1.next = list2_node2
list2_node2.next = list2_node3

# Currently:
# 1 → 2 → 4 → None
list2_head = list2_node1

# Run your solution
solution = Solution()
result = solution.mergeTwoLists(list1_head, list2_head)

print(result)