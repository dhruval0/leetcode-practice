r"""
Binary Trees in Python — Lesson 1
=================================

A linked list node had ONE tag (next). A binary tree node has TWO: left and
right. That single change is the whole difference.

The tree used throughout this file:

              1
            /   \
           2     3
          / \   / \
         4   5 6   7

Traversal answers for this tree (memorise the shape, not the numbers):

    inorder     4 2 5 1 6 3 7
    preorder    1 2 4 5 3 6 7
    postorder   4 5 2 6 7 3 1
    level order 1 2 3 4 5 6 7
"""

from collections import deque


# ---------------------------------------------------------------------------
# Step 1 — the Node
# ---------------------------------------------------------------------------
# Same idea as the linked list Node, but with two tags instead of one.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None       # tag to the left child, or None
        self.right = None      # tag to the right child, or None

    def __repr__(self):
        return f"Node({self.data})"


# ---------------------------------------------------------------------------
# Step 2 — build the tree by hand
# ---------------------------------------------------------------------------
# Do it manually once so the left/right wiring feels real.

def build_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root


# ---------------------------------------------------------------------------
# Step 3 — the three depth-first traversals (recursive)
# ---------------------------------------------------------------------------
# These three functions are IDENTICAL except for where the visit line sits.
# That is the whole trick. Everything else is copy-paste.

def inorder(node, out=None):
    """left -> node -> right.  On a BST this yields sorted order."""
    if out is None:
        out = []
    if node is None:                 # base case: fell off the tree
        return out
    inorder(node.left, out)
    out.append(node.data)            # <-- visit in the MIDDLE
    inorder(node.right, out)
    return out


def preorder(node, out=None):
    """node -> left -> right.  Good for copying/serialising a tree."""
    if out is None:
        out = []
    if node is None:
        return out
    out.append(node.data)            # <-- visit FIRST
    preorder(node.left, out)
    preorder(node.right, out)
    return out


def postorder(node, out=None):
    """left -> right -> node.  Good for deleting, or bottom-up sizing."""
    if out is None:
        out = []
    if node is None:
        return out
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.data)            # <-- visit LAST
    return out


# ---------------------------------------------------------------------------
# Step 4 — inorder without recursion (explicit stack)
# ---------------------------------------------------------------------------
# Interviewers ask for this to check you understand what recursion actually
# does. The stack IS the call stack, written out by hand.

def inorder_iterative(root):
    out, stack, current = [], [], root
    while stack or current is not None:
        while current is not None:       # dive left as far as possible
            stack.append(current)
            current = current.left
        current = stack.pop()            # nothing left of us, so visit
        out.append(current.data)
        current = current.right          # then go right and repeat
    return out


# ---------------------------------------------------------------------------
# Step 5 — level order / BFS (a queue, not a stack)
# ---------------------------------------------------------------------------
# Depth-first uses a stack. Breadth-first uses a queue. That is the only
# structural difference between the two families.

def level_order(root):
    """Flat list, row by row."""
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()               # popleft = FIFO = queue
        out.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


def level_order_by_rows(root):
    """Grouped per level: [[1], [2, 3], [4, 5, 6, 7]].

    The trick is to record len(q) BEFORE the inner loop — that is exactly
    how many nodes are on the current level.
    """
    if root is None:
        return []
    rows, q = [], deque([root])
    while q:
        level_size = len(q)
        row = []
        for _ in range(level_size):
            node = q.popleft()
            row.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Step 6 — the recursion template that solves half of all tree problems
# ---------------------------------------------------------------------------
# Ask the two children for their answer, then combine. Notice how similar
# these three functions look.

def height(node):
    """Edges on the longest root-to-leaf path. Empty tree = -1."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def search(node, target):
    """Plain binary tree: no ordering, so we must check everywhere. O(n)."""
    if node is None:
        return False
    if node.data == target:
        return True
    return search(node.left, target) or search(node.right, target)


# ---------------------------------------------------------------------------
# Step 7 — Binary SEARCH Tree (BST)
# ---------------------------------------------------------------------------
# A BST adds one rule:  everything left  <  node  <  everything right.
# That rule lets you throw away half the tree at every step -> O(log n).
#
# A BST is a binary tree. A binary tree is NOT necessarily a BST.

def bst_insert(root, data):
    """Returns the (possibly new) root. Standard interview signature."""
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = bst_insert(root.left, data)
    elif data > root.data:
        root.right = bst_insert(root.right, data)
    # equal -> ignore duplicates
    return root


def bst_search(root, target):
    """O(log n) on a balanced BST, O(n) on a degenerate one."""
    current = root
    while current is not None:
        if target == current.data:
            return True
        current = current.left if target < current.data else current.right
    return False


def is_bst(node, low=float("-inf"), high=float("inf")):
    """Validate a BST.

    THE classic trap: checking only node vs its two children is WRONG.
    A node deep in the left subtree can still be too large for the root.
    You must carry down a valid (low, high) range.
    """
    if node is None:
        return True
    if not (low < node.data < high):
        return False
    return (is_bst(node.left, low, node.data)
            and is_bst(node.right, node.data, high))


# ---------------------------------------------------------------------------
# Step 8 — printing a tree sideways so you can actually see it
# ---------------------------------------------------------------------------
# Rotate your head 90 degrees left. Root is at the far left.

def print_tree(node, depth=0):
    if node is None:
        return
    print_tree(node.right, depth + 1)
    print("    " * depth + str(node.data))
    print_tree(node.left, depth + 1)


# ---------------------------------------------------------------------------
# Your turn — exercises
# ---------------------------------------------------------------------------
# 1. invert(node)
#    Swap left and right everywhere. Two lines plus recursion.
#
# 2. is_balanced(node)
#    True if, for EVERY node, the two subtree heights differ by at most 1.
#    Naive version is O(n^2). Can you do it in one pass?
#
# 3. lowest_common_ancestor(root, a, b)
#    The deepest node that has both a and b below it.
#    Hint: recurse; if left and right both return something, you are it.
#
# 4. max_depth without recursion
#    Use level_order_by_rows and count the rows.


# ---------------------------------------------------------------------------
# Run it
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    root = build_sample_tree()

    print("--- the tree, printed sideways ---")
    print_tree(root)

    print("\n--- depth-first traversals ---")
    print("inorder    ", inorder(root))
    print("preorder   ", preorder(root))
    print("postorder  ", postorder(root))
    print("inorder it.", inorder_iterative(root))

    print("\n--- breadth-first traversal ---")
    print("level order", level_order(root))
    print("by rows    ", level_order_by_rows(root))

    print("\n--- measurements ---")
    print("height     ", height(root))
    print("node count ", count_nodes(root))
    print("leaf count ", count_leaves(root))
    print("search(6)  ", search(root, 6))
    print("search(99) ", search(root, 99))

    print("\n--- BST ---")
    bst = None
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst = bst_insert(bst, v)
    print("bst inorder", inorder(bst), "<- sorted, always")
    print("bst_search(40)", bst_search(bst, 40))
    print("bst_search(45)", bst_search(bst, 45))
    print("is_bst(bst)   ", is_bst(bst))
    print("is_bst(sample)", is_bst(root), "<- 1,2,3.. is not a valid BST")

    print("\n--- why 'check only your children' fails ---")
    # 10 -> left 5 -> right 20.  20 > 5 so the local check passes,
    # but 20 sits in 10's LEFT subtree, so the tree is not a BST.
    tricky = Node(10)
    tricky.left = Node(5)
    tricky.left.right = Node(20)
    print("is_bst(tricky)", is_bst(tricky), "<- correctly False")
