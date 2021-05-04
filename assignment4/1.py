class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
    
    def getNode(self, pos):
        #이때 넘어오는 pos는 사용자가 입력한 pos 값에서 -1 해준 값임

        if pos < 0:
            return None
        
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        
        return node
    
    def insert(self, pos, elem):
        before = self.getNode(pos - 1)

        if before is None:
            #텅 빈 연결 리스트 이므로
            self.head = Node(elem, self.head)
            #self.head = Node(elem)
        
        else:
            before.link = Node(elem, before.link)
        
    
    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before is None:
            removed = self.head
            self.head = self.head.link
        else:
            removed = before.link
            before.link = removed.link
        del removed
    
    def display(self):
        if self.head == None:
            print("empty")
        node = self.head
        while node != None:
            print(node.data)
            node = node.link


