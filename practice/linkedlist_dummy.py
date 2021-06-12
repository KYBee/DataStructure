class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()


    def getNode(self, pos):
        if pos < 0: return self.head
        node = self.head.next #dummy 더미 노드의 뒤쪽부터 찾겠다.
        while pos > 0 and node != None:
            node = node.next
            pos -= 1

        return node

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        before.next = Node(elem, before.next)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        removed = before.next
        before.next = before.next.next
        del removed

    def display(self):
        node = self.head.next
        while node is not None:
            print(node.data, end="->")
            node = node.next
        print()


s = LinkedList()
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.display()