class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class CircularLinkedQueue:

    def __init__(self):
        #head 가 아니라 tail 인 이유 -> tail을 사용해야 front rear에 접근이 쉬움
        self.tail = None

    def isEmpty(self):
        return self.tail == None
    
    def clear(self):
        self.tail = None

    def peak(self):
        if not self.isEmpty():
            return self.tail.link.data

    def enqueue(self, elem):
        node = Node(elem, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if self.isEmpty():
            return None
        elif self.tail == self.tail.link:
            removed = self.tail.link
            data = removed.data
            self.tail = None
            del(removed)
            return data
        else:
            removed = self.tail.link
            self.tail.link = removed.link
            data = removed.data
            del(removed)
            return data
            

    def print(self):
        if self.tail == None:
            print("Empty")
        else:
            node = self.tail.link
            while node != self.tail:
                print(node.data, end=" ")
                node = node.link
            print(node.data)
            


cq = CircularLinkedQueue()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.print()
print("Start Dequeue")
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
