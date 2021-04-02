import time

MAX_QSIZE = 21

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE
    
    def clear(self):
        self.front = self.rear
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
        
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
        
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("QUEUE=%s (%d)" % ("".join(out), len(out)))


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("시스템이 시작됩니다.")
system = Queue()
queue_input_index = 0

while True:
    start_time = time.time()

    user_input = int(input(">>> "))
    interrupt_time = time.time()

    queue_input_time = int(interrupt_time - start_time)
    queue_input_index %= 26

    if not(system.isFull()):
        #TODO 큐가 꽉 찼을 때 controlling
        for i in range(queue_input_time):
            print("(SYSTEM) ADDQUEUE(%s)  F=%d R=%d" % (ALPHABET[queue_input_index], system.front, system.rear))
            system.enqueue(ALPHABET[queue_input_index])
            queue_input_index += 1

    for i in range(user_input):
        print("DELETEQUEUE() = %s, F=%d, R=%d" % (system.dequeue(), system.front, system.rear))

    system.display()