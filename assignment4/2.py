import random
import string

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.num_link = link
        self.name_link = link

class LinkedList:
    def __init__(self):
        self.num_head = Node(None)
        self.name_head = Node(None)
    
    def insert(self, student):
        student = Node(student)

        before = self.num_head
        while before.num_link != None:
            if before.num_link.data[0] > student.data[0]:
                break
            before = before.num_link
        before.num_link, student.num_link = student, before.num_link

        before = self.name_head
        while before.name_link != None:
            if before.name_link.data[1] > student.data[1]:
                break
            before = before.name_link
        before.name_link, student.name_link = student, before.name_link

    def display(self, op):
        if op == "1":
            cnt = 0
            node = self.num_head
            while node.num_link != None:
                cnt += 1
                if cnt % 100 == 0:
                    print("%5d번 학생: 학번 -> %s, 이름 -> %s, 전화번호 -> %s" % (cnt, node.num_link.data[0], node.num_link.data[1], node.num_link.data[2]))
                node = node.num_link
        elif op == "2":
            cnt = 0
            node = self.name_head
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