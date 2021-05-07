import time

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):

        #alphabet pointer 
        #a, d, g, j, m, p, s, v, y
        # self.alphabet = [
        #     Node(0), Node(3), Node(6), Node(9), Node(12), Node(15), Node(18), Node(21), Node(24)
        # ]
        #self.head = self.alphabet[0]

        self.__head = Node(None)
        self.__quick_head = Node(None)
        self.__english = "abcdefghijklmnopqrstuvwxyz"
        self.__count = 0

    def search(self, question):
        in_dict = False
        cur = self.__head

        while cur.link != None and question >= cur.link.data[0]:
            if question == cur.link.data[0]:
                print(cur.link.data[1])
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
                self.insert([question, meaning])
                print("%s %s 가 추가되었습니다.(총 %d개 단어)" % (question, meaning, len(self)))

    def quick_search(self, elem):
        pass
    
    def insert(self, elem):
        elem[0] = elem[0].lower()

        #alphabet = self.english.index(elem[0][1])
        #print("alphabet", alphabet)

        before = self.__head

        while before.link != None:
            if before.link.data[0] > elem[0]:
                break
            before = before.link

        before.link = Node(elem, before.link)
        self.__count += 1
    
    def display(self):
        node = self.__head
        while node.link != None:
            print(node.link.data)
            node = node.link

    def __len__(self):
        return self.__count


randdict = LinkedList()

# Get randdict
with open('assignment4/randdict_utf8.TXT', 'r', encoding="utf-8") as f:  
    #for debugging
    i = 0

    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #형식에 맞지 않으면 추가하지 않음
        if line[1] == "":
            continue
        else:
            randdict.insert(line)

        #print(line)
        if i == 10:
            break
        else:
            i += 1

#for debugging
randdict.display()

while True:
    question = input(">> ")
    randdict.search(question)
