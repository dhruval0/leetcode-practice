r"""
Stacks and Queues in Python — Lesson 1
======================================

Both are just "a list where you are only allowed to touch the ends".
The difference is WHICH end.

    STACK   push and pop at the SAME end   -> LIFO (Last In, First Out)
    QUEUE   add at one end, remove at the other -> FIFO (First In, First Out)

That is the whole concept. The rest of this file is about doing it
efficiently in Python, and the interview problems that use them.
"""

import time
from collections import deque


# ===========================================================================
# PART 1 — STACK
# ===========================================================================

# ---------------------------------------------------------------------------
# 1a. The Pythonic stack: just use a list
# ---------------------------------------------------------------------------
# A Python list IS a stack. append() and pop() both work on the END, which
# is O(1) amortised. In an interview, this is the correct answer unless they
# explicitly ask you to build one from scratch.

def list_as_stack_demo():
    stack = []
    stack.append(10)          # push
    stack.append(20)
    stack.append(30)
    print("   stack     ", stack)
    print("   pop ->    ", stack.pop())      # 30, the LAST one in
    print("   peek ->   ", stack[-1])        # 20, without removing
    print("   after     ", stack)
    print("   empty?    ", len(stack) == 0)


# ---------------------------------------------------------------------------
# 1b. A Stack class, so the LIFO rule is enforced
# ---------------------------------------------------------------------------
# The point of a class here is not speed, it is *restriction*. A list lets
# you do stack[0] or insert in the middle. A Stack does not.

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)              # O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()              # O(1)

    def peek(self):
        """Look at the top without removing it."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack(bottom -> top: {self._items})"


# ---------------------------------------------------------------------------
# 1c. Stack built on a linked list
# ---------------------------------------------------------------------------
# Remember prepend() from the linked list lesson? Adding at the head is
# O(1). A stack is literally just prepend + remove-head. This is why the
# two topics belong next to each other.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """head of the list == top of the stack"""

    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.head      # new node points at the old top
        self.head = node           # top moves to the new node
        self._size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        data = self.head.data
        self.head = self.head.next   # just move head down one
        self._size -= 1
        return data

    def peek(self):
        if self.head is None:
            raise IndexError("peek at empty stack")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self._size


# ===========================================================================
# PART 2 — QUEUE
# ===========================================================================

# ---------------------------------------------------------------------------
# 2a. THE TRAP: do not use a list as a queue
# ---------------------------------------------------------------------------
# list.pop(0) removes from the FRONT, which forces Python to shift every
# remaining element left by one. That is O(n) per operation, so draining a
# queue of n items costs O(n^2).
#
# collections.deque is a doubly linked list under the hood, so both ends
# are O(1). Always use deque.

def why_not_a_list(n=60000):
    slow = list(range(n))
    t0 = time.perf_counter()
    while slow:
        slow.pop(0)                      # O(n) each time  -> O(n^2) total
    list_time = time.perf_counter() - t0

    fast = deque(range(n))
    t0 = time.perf_counter()
    while fast:
        fast.popleft()                   # O(1) each time  -> O(n) total
    deque_time = time.perf_counter() - t0

    print(f"   list.pop(0)     {list_time:.4f}s")
    print(f"   deque.popleft() {deque_time:.4f}s")
    print(f"   deque is ~{list_time / deque_time:.0f}x faster at n={n}")


# ---------------------------------------------------------------------------
# 2b. The Pythonic queue: collections.deque
# ---------------------------------------------------------------------------

def deque_as_queue_demo():
    q = deque()
    q.append(10)              # enqueue at the rear
    q.append(20)
    q.append(30)
    print("   queue     ", list(q))
    print("   dequeue ->", q.popleft())   # 10, the FIRST one in
    print("   front ->  ", q[0])
    print("   after     ", list(q))


# ---------------------------------------------------------------------------
# 2c. A Queue class
# ---------------------------------------------------------------------------

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)          # O(1) at the rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()      # O(1) at the front

    def front(self):
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue(front -> rear: {list(self._items)})"


# ---------------------------------------------------------------------------
# 2d. Classic interview question: a queue using two stacks
# ---------------------------------------------------------------------------
# Two LIFOs make a FIFO. Push onto `inbox`. When you need to dequeue, tip
# the whole inbox into `outbox` — that reverses the order — then pop.
#
# Amortised O(1): each item is moved between stacks at most once, even
# though a single dequeue can cost O(n).

class QueueFromTwoStacks:
    def __init__(self):
        self._inbox = []
        self._outbox = []

    def enqueue(self, item):
        self._inbox.append(item)

    def dequeue(self):
        if not self._outbox:                 # only refill when empty
            while self._inbox:
                self._outbox.append(self._inbox.pop())   # reverses order
        if not self._outbox:
            raise IndexError("dequeue from empty queue")
        return self._outbox.pop()

    def is_empty(self):
        return not self._inbox and not self._outbox


# ===========================================================================
# PART 3 — WHAT THEY ARE ACTUALLY FOR
# ===========================================================================

# ---------------------------------------------------------------------------
# 3a. Stack: balanced brackets  (LeetCode 20 — asked everywhere)
# ---------------------------------------------------------------------------
# The pattern: whenever you see an opener, remember it. Whenever you see a
# closer, it must match the MOST RECENT unmatched opener. "Most recent" is
# the word that tells you to use a stack.

def is_balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack          # leftover openers means unbalanced


# ---------------------------------------------------------------------------
# 3b. Stack: reverse anything
# ---------------------------------------------------------------------------

def reverse_with_stack(items):
    stack = list(items)
    return [stack.pop() for _ in range(len(stack))]


# ---------------------------------------------------------------------------
# 3c. Queue: BFS on a graph  (shortest path in an unweighted graph)
# ---------------------------------------------------------------------------
# This is the single most valuable use of a queue in interviews. Level-order
# tree traversal from the binary tree lesson is the same algorithm.

def bfs_shortest_path(graph, start, goal):
    """Returns the shortest path as a list, or None."""
    if start == goal:
        return [start]
    visited = {start}
    q = deque([[start]])                 # queue of PATHS
    while q:
        path = q.popleft()
        for neighbour in graph.get(path[-1], []):
            if neighbour in visited:
                continue
            if neighbour == goal:
                return path + [neighbour]
            visited.add(neighbour)
            q.append(path + [neighbour])
    return None


# ---------------------------------------------------------------------------
# Your turn — exercises
# ---------------------------------------------------------------------------
# 1. min_stack
#    A stack with push, pop, and get_min() all in O(1).
#    Hint: keep a SECOND stack of minimums alongside the main one.
#
# 2. next_greater_element(nums)
#    For each element, find the next element to its right that is bigger.
#    Hint: monotonic stack. This pattern shows up constantly.
#
# 3. stack_from_two_queues
#    The mirror image of QueueFromTwoStacks.
#
# 4. sliding_window_maximum(nums, k)
#    Max of every window of size k, in O(n).
#    Hint: a deque holding indices, kept in decreasing order of value.
#    This one is genuinely hard and genuinely common.


# ===========================================================================
# Run it
# ===========================================================================

if __name__ == "__main__":
    print("=== 1a. list as a stack ===")
    list_as_stack_demo()

    print("\n=== 1b. Stack class ===")
    s = Stack()
    for v in [1, 2, 3]:
        s.push(v)
    print("  ", s)
    print("   pop ->", s.pop(), " peek ->", s.peek(), " len ->", len(s))

    print("\n=== 1c. Stack on a linked list ===")
    ls = LinkedStack()
    for v in ["a", "b", "c"]:
        ls.push(v)
    print("   pops:", [ls.pop() for _ in range(3)], "<- reversed, as expected")

    print("\n=== 2a. why list.pop(0) is a trap ===")
    why_not_a_list()

    print("\n=== 2b. deque as a queue ===")
    deque_as_queue_demo()

    print("\n=== 2c. Queue class ===")
    q = Queue()
    for v in [1, 2, 3]:
        q.enqueue(v)
    print("  ", q)
    print("   dequeue ->", q.dequeue(), " front ->", q.front())

    print("\n=== 2d. queue from two stacks ===")
    q2 = QueueFromTwoStacks()
    for v in [1, 2, 3]:
        q2.enqueue(v)
    print("   dequeue x3:", [q2.dequeue() for _ in range(3)], "<- FIFO order")

    print("\n=== 3a. balanced brackets ===")
    for test in ["()[]{}", "([{}])", "(]", "([)]", "(("]:
        print(f"   {test:<8} -> {is_balanced(test)}")

    print("\n=== 3b. reverse with a stack ===")
    print("   ", reverse_with_stack([1, 2, 3, 4, 5]))

    print("\n=== 3c. BFS shortest path ===")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D", "E"],
        "D": ["B", "C", "F"],
        "E": ["C", "F"],
        "F": ["D", "E"],
    }
    print("   A -> F:", bfs_shortest_path(graph, "A", "F"))
    print("   A -> E:", bfs_shortest_path(graph, "A", "E"))
