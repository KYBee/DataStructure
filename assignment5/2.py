import random

class Node :
    def __init__(self, item, left=None, right=None) :
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return self.item

class TreeA :
    def __init__(self):
        self.root = None

    def get_total_count(self, n):
        if n is None: return 0
        return 1 + self.get_total_count(n.left) + self.get_total_count(n.right)

    @classmethod
    def print(cls, n):
        if n != None :
            cls.print(n.left)
            print(n.item)
            cls.print(n.right)

    @classmethod
    def print_pre(cls, n):
        if n != None :
            print(n.item, end=" ")
            cls.print(n.left)
            cls.print(n.right)

    def search(self, item):
        if self.root is None:
            return None
        else:
            return self.__search_node(self.root, item, level = 0)

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

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.__insert_node(self.root, item)
        
    def __insert_node(self, cur, item):
        #head 값이 크면 왼쪽으로
        if cur.item[0] >= item[0]:
            if cur.left is not None:
                self.__insert_node(cur.left, item)
            else:
                cur.left = Node(item)
        #head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__insert_node(cur.right, item)
            else:
                cur.right = Node(item)
        
    def calc_height(self, n=None):
        if n is None: return 0
        return 1 + max(self.calc_height(n.left), self.calc_height(n.right))


class TreeB :
    def __init__(self):
        self.root = None

    @classmethod
    def print(cls, n):
        if n != None :
            cls.print(n.left)
            print(n.item, end=" ")
            cls.print(n.right)

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.__insert_node(self.root, item)
        
    def __insert_node(self, cur, item):
        #head 값이 크면 왼쪽으로
        if cur.item >= item:
            if cur.left is not None:
                self.__insert_node(cur.left, item)
            else:
                cur.left = Node(item)
        #head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__insert_node(cur.right, item)
            else:
                cur.right = Node(item)

    def calc_height(self, n=None):
        if n is None: return 0
        return 1 + max(self.calc_height(n.left), self.calc_height(n.right))


#print_result
def print_result(tree, search_list):
    print("사전 파일을 모두 읽었습니다. %d개의 단어가 있습니다." % tree.get_total_count(tree.root))
    print("트리의 전체 높이는 %d 입니다." % tree.calc_height(treeA.root))
    print("랜덤하게 선택된 단어 %d개 : " % len(search_list), end="")
    for word in search_list:
        print(word, end=" ")
    print()
    
    for word in search_list:
        result, level = tree.search(word)
        print("%s %s (레벨 %d)" % (result.item[0], result.item[1], level))


#read word list
with open('./assignment5/randdict_utf8.TXT', 'r', encoding="utf-8") as f:  
    
    i = 0
    treeA = TreeA()
    treeB = TreeB()
    word_list = list()

    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #형식에 맞지 않으면 randdict에 추가하지 않는다.
        if line[1] == "":
            continue
        else:
            treeA.insert(line)
            treeB.insert(line)
            word_list.append(line[0])
            #print(line)

        if i == 10:
            break
        else:
            i += 1


treeA.print(treeA.root)

# print result
DATA_SIZE = 3
search_list = random.sample(word_list, DATA_SIZE)
print_result(treeA, search_list)


