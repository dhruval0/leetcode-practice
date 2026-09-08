r"""
Doubly Linked Lists in Python — Lesson 1
========================================

A singly linked list node had ONE tag: next.
A doubly linked list node has TWO: prev and next.

    None <- [prev|10|next] <-> [prev|20|next] <-> [prev|30|next] -> None
             ^head                                   ^tail

You pay one extra reference per node. What you buy:

    1. Walk backwards as well as forwards.
    2. Delete a node in O(1) when you already hold it.
       (In a singly list you must first walk from the head to find its
        predecessor, which is O(n).)

Point 2 is the whole reason this structure exists, and the reason an LRU
cache needs it. Part 3 of this file builds one.
"""


# ---------------------------------------------------------------------------
# Step 1 — the Node
# ---------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None       # tag to the previous node, or None if first
        self.next = None       # tag to the next node, or None if last

    def __repr__(self):
        return f"Node({self.data})"


# ---------------------------------------------------------------------------
# Step 2 — build one by hand
# ---------------------------------------------------------------------------
# Every link has to be set from BOTH sides. Forgetting one direction is the
# single most common bug in this whole topic.

def manual_demo():
    a, b, c = Node(10), Node(20), Node(30)

    a.next = b
    b.prev = a        # <-- the line people forget

    b.next = c
    c.prev = b        # <-- and this one

    print("   forward: ", end="")
    cur = a
    while cur:
        print(cur.data, end=" ")
        cur = cur.next

    print("\n   backward:", end=" ")
    cur = c                      # start at the TAIL to go backwards
    while cur:
        print(cur.data, end=" ")
        cur = cur.prev
    print()


# ---------------------------------------------------------------------------
# Step 3 — the class
# ---------------------------------------------------------------------------
# Keeping a `tail` reference alongside `head` is what makes append O(1).
# A singly linked list without a tail pointer needs O(n) to append.

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # -- adding ------------------------------------------------------------

    def append(self, data):
        """Add at the end. O(1), because we track the tail."""
        node = Node(data)
        if self.tail is None:              # empty list
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1
        return node

    def prepend(self, data):
        """Add at the front. O(1)."""
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1
        return node

    def insert_after(self, node, data):
        """Insert directly after a node we already hold. O(1)."""
        if node is self.tail:
            return self.append(data)
        new = Node(data)
        new.prev = node
        new.next = node.next
        node.next.prev = new               # safe: node is not the tail
        node.next = new
        self._size += 1
        return new

    # -- removing ----------------------------------------------------------

    def remove(self, node):
        """Unlink a node we already hold. O(1) — the headline feature.

        Four cases collapse into this: the node may be the head, the tail,
        both (single-element list), or in the middle. Handling prev and next
        independently covers all four without an if-tree.
        """
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next          # node was the head

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev          # node was the tail

        node.prev = node.next = None       # detach it fully
        self._size -= 1
        return node.data

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        return self.remove(self.head)

    def pop_back(self):
        if self.tail is None:
            raise IndexError("pop from empty list")
        return self.remove(self.tail)

    # -- reading -----------------------------------------------------------

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def to_list_reversed(self):
        out, cur = [], self.tail
        while cur:
            out.append(cur.data)
            cur = cur.prev
        return out

    def find(self, target):
        """Still O(n) — two-way links do not help you search."""
        cur = self.head
        while cur:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def __len__(self):
        return self._size

    def __repr__(self):
        return "None <-> " + " <-> ".join(map(str, self.to_list())) + " <-> None"


# ---------------------------------------------------------------------------
# Step 4 — proving the O(1) delete claim
# ---------------------------------------------------------------------------

def singly_delete_cost_note():
    """
    Singly linked list, deleting node X:

        head -> A -> B -> X -> C
                     ^
        You need B, because B.next must be rewired to C.
        Holding X gives you no way to reach B.
        So you walk from head until you find the node whose next is X.
        That is O(n).

    Doubly linked list, deleting node X:

        X.prev.next = X.next
        X.next.prev = X.prev

        Two lines. O(1). X told you who its neighbours are.
    """
    print(singly_delete_cost_note.__doc__)


# ===========================================================================
# PART 3 — LRU CACHE
# ===========================================================================
# This is the payoff, and it is Amazon's favourite question.
#
# Requirement: get(key) and put(key, value) both in O(1), and when the
# cache is full, evict the least recently used entry.
#
# Neither structure can do it alone:
#   - a hash map finds any key in O(1) but has no concept of order
#   - a doubly linked list maintains order and reorders in O(1) but
#     cannot find a key without scanning
#
# So you use both, and the map's values are POINTERS INTO THE LIST.
#
# Convention here: head = most recently used, tail = least recently used.
#
# Implementation note: real code uses two sentinel (dummy) nodes for head
# and tail so there is never a None to special-case. That is the trick
# worth showing in an interview.

class LRUNode:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.map = {}                       # key -> LRUNode

        # Sentinels. They are never removed, so prev/next are never None
        # for a real node, which removes every edge case.
        self.head = LRUNode()               # most recent side
        self.tail = LRUNode()               # least recent side
        self.head.next = self.tail
        self.tail.prev = self.head

    # -- internal list surgery, both O(1) ----------------------------------

    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _touch(self, node):
        """Mark as most recently used."""
        self._unlink(node)
        self._push_front(node)

    # -- public API --------------------------------------------------------

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return -1                       # LeetCode's convention
        self._touch(node)
        return node.value

    def put(self, key, value):
        node = self.map.get(key)
        if node is not None:
            node.value = value
            self._touch(node)
            return

        if len(self.map) >= self.capacity:
            lru = self.tail.prev            # the node just before the tail
            self._unlink(lru)
            del self.map[lru.key]           # this is why nodes store key

        node = LRUNode(key, value)
        self.map[key] = node
        self._push_front(node)

    def keys_mru_first(self):
        out, cur = [], self.head.next
        while cur is not self.tail:
            out.append(cur.key)
            cur = cur.next
        return out


# ---------------------------------------------------------------------------
# Your turn — exercises
# ---------------------------------------------------------------------------
# 1. reverse() on DoublyLinkedList
#    Swap prev and next on every node, then swap head and tail.
#
# 2. Circular doubly linked list
#    tail.next points to head, head.prev points to tail. No None anywhere.
#    Careful: your traversal loop condition has to change or it never ends.
#
# 3. LFU cache
#    Evict the LEAST FREQUENTLY used instead. Much harder than LRU;
#    needs a map of frequency -> doubly linked list.
#
# 4. Explain out loud why LRUCache stores `key` inside the node.
#    (Answer: eviction starts from the node, and you need the key to
#     delete the matching entry from the map.)


# ===========================================================================
# Run it
# ===========================================================================

if __name__ == "__main__":
    print("=== 2. built by hand ===")
    manual_demo()

    print("\n=== 3. the class ===")
    dll = DoublyLinkedList()
    for v in [20, 30]:
        dll.append(v)
    dll.prepend(10)
    print("  ", dll)
    print("   forward  ", dll.to_list())
    print("   backward ", dll.to_list_reversed())
    print("   length   ", len(dll))

    n20 = dll.find(20)
    dll.insert_after(n20, 25)
    print("   after insert_after(20, 25):", dll.to_list())

    dll.remove(n20)
    print("   after remove(node 20):     ", dll.to_list())
    print("   backward still consistent: ", dll.to_list_reversed())

    print("   pop_front ->", dll.pop_front(), " pop_back ->", dll.pop_back())
    print("   now:", dll, " len:", len(dll))

    print("\n=== 4. why doubly, not singly ===")
    singly_delete_cost_note()

    print("=== 5. LRU cache, capacity 3 ===")
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print("   after a,b,c        ", cache.keys_mru_first())

    print("   get('a') ->", cache.get("a"))
    print("   'a' is now newest  ", cache.keys_mru_first())

    cache.put("d", 4)
    print("   put('d') evicts LRU", cache.keys_mru_first())
    print("   get('b') ->", cache.get("b"), "<- -1, it was evicted")

    cache.put("c", 33)
    print("   put('c',33) updates", cache.keys_mru_first())
    print("   get('c') ->", cache.get("c"))
