
class Node:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.stack = list()

    def preorder_not_recursive(self, node):
        self.stack.append(node)
        while len(self.stack) != 0:
            root = self.stack.pop()
            print(root.data)
            if root.right:
                self.stack.append(root.right)
            if root.left:
                self.stack.append(root.left)



    def inorder_not_recursive(self, node):
        while True:
            while node != None:
                self.stack.append(node)
                node = node.left

            if len(self.stack) == 0:
                break

            node = self.stack.pop()

            print(node.data)
            node = node.right


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6

a = Tree()

a.head = n1


print("preordering")
a.preorder_not_recursive(a.head)
print()

print("inordering")
a.inorder_not_recursive(a.head)
print()

print("postordering")
a.postorder_not_recursive(a.head)
print()

