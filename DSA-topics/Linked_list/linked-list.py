"""
Linked Lists in Python — Lesson 1
=================================

A linked list is a chain of nodes. Each node stores a value and a reference
to the next node. Unlike a Python list, the elements are NOT stored side by
side in memory, so there is no index math — you walk the chain.

    head
     |
     v
  [10|next] -> [20|next] -> [30|next] -> None
"""


# ---------------------------------------------------------------------------
# Step 1 — the Node
# ---------------------------------------------------------------------------
# This is the entire building block. Two attributes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None      # points to the next Node, or None if last


# ---------------------------------------------------------------------------
# Step 2 — chaining them manually
# ---------------------------------------------------------------------------
# Do it by hand once so the pointers feel real.

def manual_chain_demo():
    a = Node(10)
    b = Node(20)
    c = Node(30)

    a.next = b
    b.next = c

    head = a                  # we only keep a reference to the first node

    current = head
    while current is not None:
        print(current.data)
        current = current.next    # step forward

    # Output: 10 20 30


# THE linked list pattern:
#   start at head  ->  move with current = current.next  ->  stop at None
# Almost every operation you write is some variation of this loop.


# ---------------------------------------------------------------------------
# Step 3 — wrapping it in a class
# ---------------------------------------------------------------------------

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end. O(n) — we must walk to the last node."""
        new_node = Node(data)

        if self.head is None:                  # empty list, nothing to attach to
            self.head = new_node
            return

        current = self.head
        while current.next is not None:        # walk to the LAST node
            current = current.next
        current.next = new_node

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        print(" -> ".join(map(str, values)), "-> None")


# Two things worth noticing in append():
#
#   1. The empty-list case needs special handling — there is no node to
#      attach the new node to, so we just make it the head.
#
#   2. The loop condition is `current.next is not None`, NOT
#      `current is not None`. With the latter, current ends up as None and
#      you crash on None.next. That off-by-one is the classic beginner bug.


# ---------------------------------------------------------------------------
# Your turn — exercise
# ---------------------------------------------------------------------------
# Write prepend(data): add a node at the FRONT of the list.
# It is only two lines, and it is O(1) while append() is O(n) — the first
# real insight into why this structure exists.
#
#     def prepend(self, data):
#         ...
#         ...


# ---------------------------------------------------------------------------
# Run it
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("--- manual chain ---")
    manual_chain_demo()

    print("\n--- LinkedList class ---")
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()          # 10 -> 20 -> 30 -> None