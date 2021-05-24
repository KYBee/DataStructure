import random

class Node :
    def __init__(self, item, left=None, right=None) :
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return self.item

#이진 탐색 트리
class TreeA :
    def __init__(self):
        self.root = None

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

    #item을 트리에 이진 탐색 트리의 특성에 맞도록 추가하는 메서드
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.__insert_node(self.root, item)
    
    #insert메서드에서 단어를 추가하는데 사용하는 메서드
    def __insert_node(self, cur, item):
        #root에 있는 단어의 값이 크면 왼쪽으로
        if cur.item[0] >= item[0]:
            if cur.left is not None:
                self.__insert_node(cur.left, item)
            else:
                cur.left = Node(item)
        #root에 있는 단어의 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__insert_node(cur.right, item)
            else:
                cur.right = Node(item)
    
    #트리의 높이를 구하는 메서드
    def calc_height(self, n=None):
        if n is None: return 0
        return 1 + max(self.calc_height(n.left), self.calc_height(n.right))

    # 총 몇개의 노드가 있는지를 구하는 메서드
    def get_total_count(self, n):
        if n is None: return 0
        return 1 + self.get_total_count(n.left) + self.get_total_count(n.right)


#스스로 균형을 잡는 이진 탐색 트리
class TreeB :
    def __init__(self):
        self.root = None

    #중위 순위를 하면서 트리의 모든 단어를 정렬된 상태로 출력해주는 메서드
    #디버깅을 위해서 구현
    @classmethod
    def print(cls, n):
        if n != None :
            cls.print(n.left)
            print(n.item, end=" ")
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

    #item을 트리에 이진 탐색 트리의 특성에 맞도록 추가하는 메서드
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.root = self.__insert_node(self.root, item)

    #insert메서드에서 단어를 추가하는데 사용하는 메서드
    def __insert_node(self, cur, item):
        #root에 있는 단어의 값이 크면 왼쪽으로
        if cur.item[0] >= item[0]:
            if cur.left is not None:
                cur.left = self.__insert_node(cur.left, item)
            else:
                cur.left = Node(item)
        #root에 있는 단어의 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                cur.right = self.__insert_node(cur.right, item)
            else:
                cur.right = Node(item)

        #만약의 트리가 편향 트리가 되었다면 다시 균형을 맞추어주기 위해 실행한다.
        return self.rebalance(cur)

    #트리의 균형을 맞추기 위한 메서드
    def rebalance(self, cur):

        left_height = self.calc_height(cur.left)
        right_height = self.calc_height(cur.right)

        if left_height - right_height <= -2:
            if self.calc_height(cur.right.left) - self.calc_height(cur.right.right) < 0:
                cur = self.rrrotate(cur)
            else:
                cur = self.rlrotate(cur)
        elif left_height - right_height >= 2:
            if self.calc_height(cur.left.left) - self.calc_height(cur.left.right) < 0:
                cur = self.lrrotate(cur)
            else:
                cur = self.llrotate(cur)
        return cur

    def llrotate(self, cur):
        B = cur.left
        cur.left = B.right
        B.right = cur
        return B

    def rrrotate(self, cur):
        B = cur.right
        cur.right = B.left
        B.left = cur
        return B

    def rlrotate(self, cur):
        B = cur.right
        cur.right = self.llrotate(B)
        return self.rrrotate(cur)

    def lrrotate(self,cur):
        B = cur.left
        cur.left = self.rrrotate(B)
        return self.llrotate(cur)

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
        print(word, end=" ")
    print()
    
    for word in search_list:
        result, level = tree.search(word)
        print("%s %s (레벨 %d)" % (result.item[0], result.item[1], level))

#몇 개의 단어를 랜덤하게 뽑을지 지정하는 변수
DATA_SIZE = 10

#파일을 열어서 단어를 읽어온다.
with open('./randdict_utf8.TXT', 'r', encoding="utf-8") as f:  
    
    # i 는 디버깅을 위한 변수
    #i = 0
    treeA = TreeA()
    treeB = TreeB()
    
    #word_list는 단어를 랜덤하게 선택하기 위해 저장해두는 리스트
    word_list = list()

    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #형식에 맞지 않으면 tree와 전체 word_list에 추가하지 않는다.
        if line[1] == "":
            continue
        else:
            treeA.insert(line)
            treeB.insert(line)
            word_list.append(line[0])
            
            #아래 2줄은 디버깅을 위한 코드
            #print(i, line)
            #i+=1

#랜덤으로 DATA_SIZE만큼의 단어를 선택함
search_list = random.sample(word_list, DATA_SIZE)

#treeA와 treeB의 결과 출력
print_result(treeA, search_list)
print()
print_result(treeB, search_list)