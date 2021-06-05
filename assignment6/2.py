import random

class Node :
    def __init__(self, item, left=None, right=None) :
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return self.item

#트리
class TreeA :
    def __init__(self, word_list):
        self.root = self.initialize(word_list)

    #중위 순위를 하면서 트리의 모든 단어를 정렬된 상태로 출력해주는 메서드
    #디버깅을 위해서 구현
    @classmethod
    def print(cls, n):
        if n != None :
            cls.print(n.left)
            print(n.item)
            cls.print(n.right)

    #입력받은 item을 트리에서 찾아서 돌려주는 탐색 메서드
    def search(self, item):
        if self.root is None:
            return None
        else:
            return self.__search_node(self.root, item, level = 0)

    #search메서드에서 단어를 탐색하는데 사용하는 메서드
    def __search_node(self, cur, item, level):
        if cur is None:
            return None, None
        if cur.item[0] == item:
            return cur, level
        else:
            if cur.item[0] >= item:
                level += 1
                return self.__search_node(cur.left, item, level)
            else:
                level += 1
                return self.__search_node(cur.right, item, level)


    def initialize(self, word_list):
        data_length = len(word_list)

        if data_length < 4:
            if data_length <= 0:
                return None
            elif data_length <= 1:
                root = Node(word_list[0])
                return root
            elif data_length <= 3:
                root = Node(word_list[1])
                root.left = Node(word_list[0])
                if data_length == 3:
                    root.right = Node(word_list[2])
                return root
        else:
            root_num = len(word_list) // 2
            root = Node(word_list[root_num])
            root.left = self.initialize(word_list[:root_num])
            root.right = self.initialize(word_list[root_num + 1:])
            return root

    #트리의 높이를 구하는 메서드
    def calc_height(self, n=None):
        if n is None: return 0
        return 1 + max(self.calc_height(n.left), self.calc_height(n.right))

    # 총 몇개의 노드가 있는지를 구하는 메서드
    def get_total_count(self, n):
        if n is None: return 0
        return 1 + self.get_total_count(n.left) + self.get_total_count(n.right)

#결과를 출력하는 함수
def print_result(tree, search_list):
    print("사전 파일을 모두 읽었습니다. %d개의 단어가 있습니다." % tree.get_total_count(tree.root))
    print("트리의 전체 높이는 %d 입니다." % tree.calc_height(tree.root))
    print("랜덤하게 선택된 단어 %d개 : " % len(search_list), end="")
    for word in search_list:
        print(word[0], end=" ")
    print()
    
    for word in search_list:
        result, level = tree.search(word[0])
        print("%s %s (레벨 %d)" % (result.item[0], result.item[1], level))

#몇 개의 단어를 랜덤하게 뽑을지 지정하는 변수
DATA_SIZE = 10

#파일을 열어서 단어를 읽어온다.
with open('./randdict_utf8.TXT', 'r', encoding="utf-8") as f:  
    
    #word_list는 단어를 랜덤하게 선택하기 위해 저장해두는 리스트
    word_list = list()

    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #형식에 맞지 않으면 tree와 전체 word_list에 추가하지 않는다.
        if line[1] == "":
            continue
        else:
            word_list.append(line)

word_list = sorted(word_list, key=lambda word: word[0])

treeA = TreeA(word_list)

#랜덤으로 DATA_SIZE만큼의 단어를 선택함
search_list = random.sample(word_list, DATA_SIZE)

#treeA와 treeB의 결과 출력
print_result(treeA, search_list)
