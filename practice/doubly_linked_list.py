class Node:
    def __init__(self, elem, llink = None, rlink = None):
        self.data = elem
        self.llink = llink
        self.rlink = rlink
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_pos(self, pos):
        
        if pos < 0: return None
        
        node = self.head
        
        while pos > 0 and node != None:
            node = node.rlink

        return node

    
    def insert(self, pos, elem):
        before = self.get_pos(pos - 1)
        if before == None:
            node = Node(elem, self.head, self.tail)
            self.head = node
            self.tail = node
        else:
            node = Node(elem, before, before.rlink)
            before.rlink.llink = node
            before.rlink = node
        
    def print(self):
        if self.head == None:
            return None
        
        node = self.head
        while node != None:
            print(node.data, end = " ")
            node = node.rlink
    
    def print_reverse(self):
        if self.tail == None:
            return None
        
        node = self.tail
        while node != None:
            print(node.data, end = " ")
            node = node.llink
        

dl = DoublyLinkedList()
dl.insert(0, 3)
dl.insert(1, 2)
dl.insert(1, 5)

dl.print()
print()
print(dl.head.data)