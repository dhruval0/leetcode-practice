class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#       1
#     /   \
#    2     3
#   / \
#  4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("root            :", root.data)
print("root.left       :", root.left.data)
print("root.right      :", root.right.data)
print("root.left.left  :", root.left.left.data)
print("root.left.right :", root.left.right.data)
print("root.right.left :", root.right.left)


def show(node):
    if node is None:
        return
    show(node.left)
    print(node.data, end=" ")
    show(node.right)


print("\ninorder         :", end=" ")
show(root)
print()
