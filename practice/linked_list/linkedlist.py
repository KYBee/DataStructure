class Node :
  def __init__(self, data, next=None):
      self.data = data
      self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.next
            pos -= 1
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node=Node(elem, before.next)
            before.next = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before is None:
            removed = self.head
            self.head = self.head.next
        else :
            removed = before.next
            before.next = before.next.next
        del removed

    def display(self):
        node = self.head
        while node is not None:
            print(node.data, end="->")
            node = node.next
        print()

s = LinkedList()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.display()