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

    @classmethod
    def print(cls, n):
        if n != None :
            cls.print(n.left)
            print(n.item, end=" ")
            cls.print(n.right)

    @classmethod
    def print_pre(cls, n):
        if n != None:
            print(n.item, end="")
            cls.print(n.left)
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
    

class TreeB :
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    @classmethod
    def print(cls, n):
        if n != None :
            cls.print(n.left)
            print(n.item, end=" ")
            cls.print(n.right)

    @classmethod
    def print_pre(cls, n):
        if n != None:
            print(n.item, end="")
            cls.print(n.left)
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
            
        #TODO Do something for balancing
        self.rebalance()

    def rebalance(self):
        #TODO if unbalanced -> make it balanced
        #TODO decide where to rotate
        pass

    def rrotate(self):
        A = self.root
        B = self.root.left
        T = B.right

        self.root = B
        B.right = A
        A.left = T

    def lrotate(self):
        A = self.root
        B = self.root.right
        T = B.left

        self.root = B
        B.left = A
        A.right = T

    def calc_height(self, n=None):
        if n is None: return 0
        return 1 + max(self.calc_height(n.left), self.calc_height(n.right))

    

f = [["apple"], ["zebra"], ["banana"], ["water"], ["game"]]

treeA = TreeA()
treeB = TreeB()

i = 0
for line in f:
    #형식에 맞지 않으면 randdict에 추가하지 않는다.
    if line[0] == "":
        continue
    else:
        treeA.insert(line)
        treeB.insert(line)
        print(line)

print()
treeA.print(treeA.root)
print()
treeB.print(treeB.root)

print()
treeA.print_pre(treeA.root)
print()
treeB.print_pre(treeB.root)

print("\n\n")
print(treeA.calc_height(treeA.root))
print(treeB.calc_height(treeB.root))

    