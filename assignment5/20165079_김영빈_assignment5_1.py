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
        #tree의 root 노드를 pointing 할 변수
        self.root = None

    #preorder를 위한 class method
    @classmethod
    def preorder(cls, n):
        if n != None :
            print(n.item,end=" ")
            cls.preorder(n.left)
            cls.preorder(n.right)
    
    #inorder를 위한 class method
    @classmethod
    def inorder(cls, n):
        if n != None :
            cls.inorder(n.left)
            print(n.item, end=" ")
            cls.inorder(n.right)
    
    #postorder를 위한 class method
    @classmethod
    def postorder(cls, n):
        if n != None :
            cls.postorder(n.left)
            cls.postorder(n.right)
            print(n.item, end=" ")

    #levelorder를 위한 class method
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
        
#위에서 구현한 tree를 이용하여 만든 계산기 class
class Calculator :
    def __init__(self):
        #사용할 tree 인스턴스 변수
        self.tree = Tree()
        #사용자에게 입력받은 식을 저장할 인스턴스 변수
        self.equation = None
        #operator weight를 계산할 토큰
        self.operator = "+-*/"
        #식의 값을 저장할 인스턴스 변수
        self.value = 0

    #사용자에게 식을 입력받는 메서드
    def get_equation(self):
        self.equation = input("수식을 입력하세요 : ").strip()

    #사용자에게 입력받은 식으로 트리를 구성하는 메서드
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

    #2개의 피연산자와 1개의 연산자를 이용하여 서브 트리를 만드는 메서드
    def get_sub_tree(self, left, root, right):
        root.left = left
        root.right = right
        return root

    #결과를 프린트해주는 메서드
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

    #결과값을 출력하고 초기화 하는 메서드
    def get_value(self):
        self.value = self.postorder_calculate(self.tree.root)
        print("\n계산 결과 :", self.value)

        #Calculator의 run 메서드를 무한반복으로 실행했기 때문에 다음 run이 실행되기 전에 3개의 인스턴스 변수를 초기화 시켜줌
        self.value = 0
        self.equation = None
        self.tree.root = None

    #후위 계산으로 결과 값을 구하는 메서드
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

    #계산기를 실행하는 메서드
    def run(self):
        self.get_equation()
        self.get_tree()
        self.print_result()

c = Calculator()
while True:
    c.run()