#Queue는 Queue의 역할을 할 수 있도록 간단하게만 구현함.
class Queue():
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            print("Nothing in Queue")
        else:
            target = self.items[0]
            self.items = self.items[1:]
            return target

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
    def preorder(cls, n):
        if n != None :
            print(n.item,end=" ")
            cls.preorder(n.left)
            cls.preorder(n.right)
        
    @classmethod
    def inorder(cls, n):
        if n != None :
            cls.inorder(n.left)
            print(n.item, end=" ")
            cls.inorder(n.right)
    
    @classmethod
    def postorder(cls, n):
        if n != None :
            cls.postorder(n.left)
            cls.postorder(n.right)
            print(n.item, end=" ")

    @classmethod
    def levelorder(cls, n):
        if n != None:
            queue = Queue()
            queue.enqueue(n)
            while not queue.isEmpty():
                n = queue.dequeue()
                if n is not None:
                    print(n.item, end=" ")
                    queue.enqueue(n.left)
                    queue.enqueue(n.right)
        
class Calculator :
    def __init__(self):
        self.tree = Tree()
        self.equation = None
        self.operator = "+-*/"
        self.value = 0

    def get_equation(self):
        self.equation = input("수식을 입력하세요 : ").strip()

    def get_tree(self):
        i = 1
        while i < len(self.equation) - 1:
            if self.tree.root == None:
                sub_tree = self.get_sub_tree(Node(self.equation[i - 1]), Node(self.equation[i]), Node(self.equation[i + 1]))
                self.tree.root = sub_tree
            elif self.operator.index(self.tree.root.item) // 2 < self.operator.index(self.equation[i])// 2:
                self.tree.root.right = self.get_sub_tree(self.tree.root.right, Node(self.equation[i]), Node(self.equation[i + 1]))
            else:
                self.tree.root = self.get_sub_tree(self.tree.root, Node(self.equation[i]), Node(self.equation[i + 1]))
            i += 2

    def get_sub_tree(self, left, root, right):
        root.left = left
        root.right = right
        return root

    def print_result(self):
        print("전위 순회 : ", end="")
        self.tree.preorder(self.tree.root)
        print("\n중위 순회 : ", end="")
        self.tree.inorder(self.tree.root)
        print("\n후위 순회 : ", end="")
        self.tree.postorder(self.tree.root)
        print("\n레벨 순회 : ", end="")
        self.tree.levelorder(self.tree.root)
        self.get_value()

    def get_value(self):
        self.value = self.postorder_calculate(self.tree.root)
        print("\n계산 결과 :", self.value)

        #initialize
        self.value = 0
        self.equation = None
        self.tree.root = None

    def postorder_calculate(self, n):
        if n != None :
            left = self.postorder_calculate(n.left)
            op = (n.item)
            right = self.postorder_calculate(n.right)

            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            elif op == "/":
                return left / right
            else:
                return int(op)

    def run(self):
        self.get_equation()
        self.get_tree()
        self.print_result()
        
c = Calculator()
while True:
    c.run()