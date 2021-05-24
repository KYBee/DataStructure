class Node :
    def __init__(self, item, left=None, right=None) :
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return self.item

class Tree :
    def __init__(self):
        self.root = None

    @classmethod
    def inorder(cls, n):
        if n != None :
            cls.inorder(n.left)
            print(n.item, end=" ")
            cls.inorder(n.right)

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
    
with open('./assignment5/randdict_utf8.TXT', 'r', encoding="utf-8") as f:  
    
    i = 0
    tree = Tree()
    for line in f:
        line = line.strip().split(":")
        line = list(map(lambda x: x.strip(), line))

        #형식에 맞지 않으면 randdict에 추가하지 않는다.
        if line[1] == "":
            continue
        else:
            tree.insert(line)
            print(line)

        if i == 100:
            break
        else:
            i += 1

tree.inorder(tree.root)

    