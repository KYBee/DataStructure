class Node:

    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link



class LinkedStack:

    def __init__(self):
        self.top = None


    def is_empty(self):
        return self.top == None

    def clear(self):
        self.top = None
        #되도록이면 del 해주는 것도 좋음