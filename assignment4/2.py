import random
import string

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.num_link = link
        self.name_link = link

class LinkedList:
    def __init__(self):
        #학번을 기준으로 하는 head -> num_head
        #이름을 기준으로 하는 head -> name_head
        self.__num_head = Node(None)
        self.__name_head = Node(None)
    
    def insert(self, student):
        #student의 Node를 먼저 만들고 num_head와 name_head를 조절해주면서
        #결과적으로 하나의 리스트를 2개의 리스트와 같이 사용할 수 있다.
        student = Node(student)

        #학번 순 정렬을 구현한 코드이다.
        before = self.__num_head
        while before.num_link != None:
            if before.num_link.data[0] > student.data[0]:
                break
            before = before.num_link
        before.num_link, student.num_link = student, before.num_link

        #이름 순 정렬을 구현한 코드이다.
        before = self.__name_head
        while before.name_link != None:
            if before.name_link.data[1] > student.data[1]:
                break
            before = before.name_link
        before.name_link, student.name_link = student, before.name_link

    #학번 or 이름을 옵션으로 받아서 입력받은 옵션에 해당하는 head를 기준으로 결과를 출력한다.
    #결과는 100명당 1번씩 출력했다.
    def display(self, op):
        if op == "1":
            cnt = 0
            node = self.__num_head
            while node.num_link != None:
                cnt += 1
                if cnt % 100 == 0:
                    print("%5d번 학생: 학번 -> %s, 이름 -> %s, 전화번호 -> %s" % (cnt, node.num_link.data[0], node.num_link.data[1], node.num_link.data[2]))
                node = node.num_link
        elif op == "2":
            cnt = 0
            node = self.__name_head
            while node.name_link != None:
                cnt += 1
                if cnt % 100 == 0:
                    print("%5d번 학생: 학번 -> %s, 이름 -> %s, 전화번호 -> %s" % (cnt, node.name_link.data[0], node.name_link.data[1], node.name_link.data[2]))
                node = node.name_link
        else:
            print("잘못된 입력입니다.")
            return

DATA_SIZE = 10000
student_data = LinkedList()

#random한 10000개의 학생 데이터를 만든다.
random_id = random.sample(range(20130000, 20220000), DATA_SIZE)
for r in random_id:
    name_len = random.randint(1, 10)
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(name_len))
    phone_number = "010" + str(format(random.randint(0, 100000000), "08")) 
    student_data.insert([r, name, phone_number])

while True:
    print("\n(1) 학번순\n(2) 이름순")
    op = input("메뉴 선택(0 : 종료) : ")
    if op == '0':
        print("종료")
        break
    else:
        student_data.display(op)