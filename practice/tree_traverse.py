class Node:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node != None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)


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
a.preorder(a.head)
print()
print("inordering")
a.inorder(a.head)
print()
print("postordering")
a.postorder(a.head)
print()

