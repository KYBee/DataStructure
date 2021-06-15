class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()


    def getNode(self, pos):
        if pos < 0 or self.head.next == None: return self.head
        node = self.head.next #dummy 더미 노드의 뒤쪽부터 찾겠다.
        while pos > 0 and node != None:
            node = node.next
            pos -= 1

        return node

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        before.next = Node(elem, before.next)

    #완전 비어있는 연결 리스트에서 delete연산 수행 시 self.head.next.next가 None이라서 오류가 남
    #따라서 아래의 문장 추가 필요
    def delete(self, pos):
        before = self.getNode(pos - 1)
        removed = before.next
        if removed != None:
            before.next = before.next.next
            del removed

    def display(self):
        node = self.head.next
        while node is not None:
            print(node.data, end="->")
            node = node.next
        print()

    def search(self, data):
        node = self.head.next
        while node is not None:
            if node.data == data: break
            node = node.next

        return node


s = LinkedList()
s.delete(3)
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(2, 50)
print(s.search(10).data)
s.display()
s.delete(0)
s.display()