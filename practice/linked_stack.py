class Node:

    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link



class LinkedStack:

    def __init__(self):
        self.top = None

    def push(self, elem):
        n = Node(elem, self.top)
        self.top = n
    
    def pop(self):
        n = self.top
        self.top = n.link
        return self.top.data

    def is_empty(self):
        return self.top == None

    def clear(self):
        self.top = None
        #되도록이면 del 해주는 것도 좋음

    def print(self):
        if self.top == None:
            return self.top

        #n을 while문 조건에 넣어야 함
        n = self.top
        while n != None:
            print(n.data)

            n = n.link



st = LinkedStack()

print("Printing initial stack")
st.print()

st.push(10)
st.push(20)
st.push(30)

print("Printing after push")
st.print()

p1 = st.pop()
p2 = st.pop()

print("Printing after pop")
print("p1", p1)
print("p2", p2)
st.print()
