import time

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        #더미 노드를 사용하기 위해서 head 변수에 None값이 저장된 Node를 할당했다.
        self.__head = Node(None)
        self.__count = 0

        #더 빠른 search를 위한 메서드
        self.alphabet = {}
        self.__english = "abcdefghijklmnopqrstuvwxyz"

    # 구현한 더 빠른 Search 방법
    def quick_search(self, question):
        in_dict = False

        #사전에 질의하는 단어의 맨 앞글자를 확인한다.
        alphabet = self.__english.index(question[0])

        """
        만약 해당 alphabet이 alphabet 인덱스에 존재하지 않는다면
        사전에 존재하지 않는다고 판단하고 in_dict를 false로 return 한다.
        이때 alphabet이 self.alphabet에 key 값으로 존재하는지의 여부는 파이썬 딕셔너리의 특성상 O(1)이다.
        """
        if alphabet not in self.alphabet:
            return in_dict, 0
        else:
            #만약 사전에 해당 알파벳으로 시작하는 인덱스가 존재한다면 해당 인덱스의 시작 노드부터 비교를 한다.
            cur = self.alphabet[alphabet]
            search_time = time.time()

            while cur != None and question >= cur.data[0]:
                if question == cur.data[0]:
                    print(cur.data[1])
                    in_dict = True
                    break
                else:
                    cur = cur.link

            search_time = time.time() - search_time

            return in_dict, search_time     

    def search(self, question):
        in_dict = False
        #무조건 맨 앞의 head 노드에서부터 search를 진행한다.
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
        if meaning == "":
            print("추가하지 않습니다.")
        else:
            #적절한 단어와 meaning이 들어온다면 initialize 메서드를 호출하여 적절한 위치를 찾고 사전에 추가되게 한다.
            self.initialize([question, meaning])
            print("%s %s 가 추가되었습니다.(총 %d개 단어)" % (question, meaning, len(self)))
    
    def initialize(self, elem):
        elem[0] = elem[0].lower()

        before = self.__head
        while before.link != None:
            if before.link.data[0] > elem[0]:
                break
            before = before.link
        before.link = Node(elem, before.link)

        """
        더 빠른 Search를 위한 개선 사항이다.
        이미 Node는 추가되어 있는 상태이지만, 나중에 Search를 더 빠르게 해주기 위해서 선언한 self.alphabet을
        필요하다면 Update 시켜줘야 sel.alphabet이 가장 최신의 상태를 유지할 수 있다.

        따라서 self.alphabet에 해당 알파벳으로 시작하는 인덱스가 있는지를 먼저 확인하고 존재하지 않는다면
        새로운 key value 쌍을 등록한다.

        만약 존재한다면 두 글자를 비교하여 업데이트 시킬 필요가 있다면 self.alphabet을 업데이트 시킨다.
        """
        alphabet = self.__english.index(elem[0][0])
        if alphabet not in self.alphabet:
            self.alphabet[alphabet] = before.link
        else:
            if self.alphabet[alphabet].data[0] > before.link.data[0]:
                self.alphabet[alphabet] = before.link
        self.__count += 1
    
    def display(self):
        node = self.__head
        while node.link != None:
            print(node.link.data)
            node = node.link

    def __len__(self):
        return self.__count

# 사전의 역할을 할 randdict 선언 후 LinkedList인스턴스를 할당했다.
randdict= LinkedList()

with open('assignment4/randdict_utf8.TXT', 'r', encoding="utf-8") as f:  
    i = 0
    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #형식에 맞지 않으면 randdict에 추가하지 않는다.
        if line[1] == "":
            continue
        else:
            randdict.initialize(line)
        
        if i == 1000:
            break
        i += 1

randdict.display()

while True:
    question = input(">> ")

    #일반적인 search
    in_dict, randdict_time = randdict.search(question)

    #개선한 quick_search
    in_dict, randdict_quick_search_time = randdict.quick_search(question)

    #만약 검색 내용이 사전에 없다면 새로 추가함
    if not in_dict:
        randdict.insert(question)
    
    #search와 quick_search 2개의 시간 비교를 위한 함수
    print("randdict search time:       %.10f" % randdict_time)
    print("randdict quick search time: %.10f" % randdict_quick_search_time, end="\n\n")

    #새로 값을 추가할 때 self.alphabet이 update되는지를 확인하기 위한 디버그 코드 
    #for name in randdict.alphabet.keys():
    #    print(randdict.alphabet[name].data[0])