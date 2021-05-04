class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
    
    def getNode(self, pos):
        if pos < 0:
            return None
        
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        
        return node
    
    def insert(self, elem):
        #before = self.getNode(pos - 1)

        if self.head is None:
            #텅 빈 연결 리스트 이므로
            self.head = Node(elem, self.head)
            #self.head = Node(elem)
        
        else:
            before = self.head
            while before.link is not None:
                print('for debugging')
                print(before.data[0], elem[0])
                if before.data[0] > elem[0]:
                    break
                before = before.link

            print("final before", before.data)
            before.link = Node(elem, before)
        
    
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


linked_dict = LinkedList()

with open('./assignment4/randdict_utf8.TXT', encoding="utf-8") as f:

    i = 0
    for line in f:
        line = line.strip().split(":")
        
        line = list(map(lambda x: x.strip(), line))

        linked_dict.insert(line)

        linked_dict.display()
        print()

        if i == 4:
            break
        else:
            i += 1


    linked_dict.display()
