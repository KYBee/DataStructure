
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def get_pos(self, pos):
        if pos < 0: return None

        node = self.head

        while pos > 0 and node !=None:
            node = node.link
            pos -= 1

        return node

    def insert(self, pos, elem):
        before = self.get_pos(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            before.link = Node(elem, before.link)

    def delete(self, pos):
        if self.head == None:
            return

        before = self.get_pos(pos - 1)
        if before == None:
            removed = self.head
            self.head = self.head.link
        else:
            removed = before.link
            before.link = removed.link

        del(removed)

    def print(self):
        if self.head == None:
            print("Empty")

        n = self.head
        while n != None:
            print(n.data, end=" ")
            n = n.link
        
        print()

    def search(self, data):
        if self.head == None:
            return "There's no data"
        else:
            node = self.head
            while node != None:
                if node.data == data:
                    break
                node = node.link

            return node

    def merge(self, behind):
        if self.head == None:
            self.head = behind.head
        else:
            node = self.head
            while node.link != None:
                node = node.link
            
            node.link = behind.head

a = LinkedList()
a.print()
a.delete(3)
a.insert(4, 20)
a.print()

a.insert(0, 25)
a.print()

a.insert(1, 30)
a.print()

a.delete(0)
a.print()

b = LinkedList()
b.insert(0, -20)
b.insert(0, -30)

print("Searching")
print(a.search(10))

print("Merging")
b.print()
a.merge(b)

a.print()
