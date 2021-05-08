import time

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class QuickLinkedList:
    def __init__(self):
        self.alphabet = [0] * 26
        self.__head = Node(None)
        self.__english = "abcdefghijklmnopqrstuvwxyz"
        self.__count = 0

    def quick_search(self, question):
        in_dict = False
        alphabet = self.__english.index(question[0][0])

        if self.alphabet[alphabet] == 0:
            print("없네요")
            return in_dict, 0
        else:
            cur = self.alphabet[alphabet]
            search_time = time.time()

            while cur.link != None and question >= cur.data[0]:
                if question == cur.data[0]:
                    print(cur.data[1])
                    in_dict = True
                    break
                else:
                    cur = cur.link

            search_time = time.time() - search_time

            return in_dict, search_time        

    def quick_initialize(self, elem):
        elem[0] = elem[0].lower()

        #알파벳의 index
        alphabet = self.__english.index(elem[0][0])
        before = self.__head

        while before.link != None:
            if before.link.data[0] > elem[0]:
                break
            before = before.link

        before.link = Node(elem, before.link)

        if self.alphabet[alphabet] == 0:
            self.alphabet[alphabet] = before.link
        else:
            if self.alphabet[alphabet].data[0] > before.link.data[0]:
                self.alphabet[alphabet] = before.link

        self.__count += 1

    def quick_insert(self, question):
        print("찾을 수 없는 단어입니다. 뜻을 추가하세요(추가하지 않으려면 공백)")
        meaning = input("> ")

        insert_time = time.time()
        if meaning == "":
            print("추가하지 않습니다.")
        else:
            self.quick_initialize([question, meaning])
            print("%s %s 가 추가되었습니다.(총 %d개 단어)" % (question, meaning, len(self)))
        insert_time = time.time() - insert_time

        return insert_time

    def display(self):
        node = self.__head
        while node.link != None:
            print(node.link.data)
            node = node.link

    def __len__(self):
        return self.__count



class LinkedList:
    def __init__(self):
        self.__head = Node(None)
        self.__count = 0

    def search(self, question):
        in_dict = False
        cur = self.__head

        search_time = time.time()

        while cur.link != None and question >= cur.link.data[0]:
            if question == cur.link.data[0]:
                print(cur.link.data[1])
                in_dict = True
                break
            else:
                cur = cur.link

        search_time = time.time() - search_time

        return in_dict, search_time

    def insert(self, question):

        print("찾을 수 없는 단어입니다. 뜻을 추가하세요(추가하지 않으려면 공백)")
        meaning = input("> ")

        insert_time = time.time()
        if meaning == "":
            print("추가하지 않습니다.")
        else:
            self.initialize([question, meaning])
            print("%s %s 가 추가되었습니다.(총 %d개 단어)" % (question, meaning, len(self)))
        insert_time = time.time() - insert_time

        return insert_time
    
    def initialize(self, elem):
        elem[0] = elem[0].lower()

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


randdict_search = QuickLinkedList()
randdict_quick_search = QuickLinkedList()

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
            randdict_search.quick_initialize(line)
            #randdict_quick_search.insert(line)

        #print(line)
        if i == 40:
            break
        else:
            i += 1

#for debugging
randdict_search.display()

print()

for line in randdict_search.alphabet:
    if line != 0:
        print(line.data[0])
#randdict_quick_search.display()

while True:
    question = input(">> ")

    #일반적인 search
    in_dict, randdict_search_time = randdict_search.quick_search(question)

    if not in_dict:
        randdict_insert_time = randdict_search.quick_insert(question)

    #빠르게 개선한 search
    # randdict_quick_search_time = time.time()
    # randdict_quick_search.search(question)
    # randdict_quick_search_time = time.time() - randdict_quick_search_time

    #print("randdict search time", randdict_search_time)
    #print("randdict quick search time", randdict_quick_search_time)


    for line in randdict_search.alphabet:
        if line != 0:
            print(line.data[0])