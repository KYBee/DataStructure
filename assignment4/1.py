class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):

        #alphabet pointer 
        #a, d, g, j, m, p, s, v, y
        self.alphabet = [
            Node(0), Node(3), Node(6), Node(9), Node(12), Node(15), Node(18), Node(21), Node(24)
        ]
        self.head = self.alphabet[0]

        self.english = "abcdefghijklmnopqrstuvwxyz"
        self.__count = 0
    
    def getNode(self, pos):
        #이때 넘어오는 pos는 사용자가 입력한 pos 값에서 -1 해준 값임
        if pos < 0:
            return None
        
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        
        return node
    
    def insert(self, elem):
        elem[0] = elem[0].lower()

        alphabet = self.english.index(elem[0][1])
        print("alphabet", alphabet)

        before = self.alphabet[alphabet]

        while before.link != None:
            if before.link.data[0] > elem[0]:
                break
            before = before.link

        before.link = Node(elem, before.link)
        self.__count += 1
    
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
        node = self.head
        while node.link != None:
            print(node.link.data)
            node = node.link

    def __len__(self):
        return self.__count


randdict = LinkedList()

# Get randdict
with open('randdict_utf8.TXT', 'r') as f:  
    #for debugging
    i = 0

    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #TODO 올바르지 않은 형식의 사전 데이터 삭제
        randdict.insert(line)

        #print(line)

        if i == 40:
            break
        else:
            i += 1

#for debugging
randdict.display()

while True:
    question = input(">> ")

    cur = randdict.head.link
    in_dict = False

    while question >= cur.data[0]:
        if question == cur.data[0]:
            print(cur.data[1])
            in_dict = True
            break
        else:
            cur = cur.link

    if not in_dict:
        print("찾을 수 없는 단어입니다. 뜻을 추가하세요(추가하지 않으려면 공백)")
        meaning = input("> ")

        if meaning == "":
            print("추가하지 않습니다.")
        else:
            randdict.insert([question, meaning])
            print("%s %s 가 추가되었습니다.(총 %d개 단어)" % (question, meaning, len(randdict)))