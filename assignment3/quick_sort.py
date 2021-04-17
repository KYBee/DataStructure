#with recursive
def quicksort(a):
    if len(a) <= 1:
        return a
    
    pivot = a[0]
    tail = a[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)



class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

    def peak(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

#with no recursive
def partition(a, start, end):
    pivot = a[start]
    left = start + 1
    right = end
    while True:
        while left <= right and a[left] <= pivot:
            left += 1
        while left <= right and a[right] > pivot:
            right -= 1

        if right < left:
            break
        else: 
            a[left], a[right] = a[right], a[left]
    
    a[start], a[right] = a[right], a[start]
    return right
        

def quick_sort(a):
    num_stack = Stack()
    num_stack.push(0)
    num_stack.push(len(a) - 1)

    while not num_stack.isEmpty():
        end = num_stack.pop()
        start = num_stack.pop()
        pivot = partition(a, start, end)

        if pivot - 1 > start:
            num_stack.push(start)
            num_stack.push(pivot - 1)
        
        if pivot + 1 < end:
            num_stack.push(pivot + 1)
            num_stack.push(end)
    
    return a
    

a = [3, 4, 5, 2, 10, 22, 34, 1]
print(quicksort(a))
print(quick_sort(a))