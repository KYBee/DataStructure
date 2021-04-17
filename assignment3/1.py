import random
import string
import time

#Define Data Size
DATA_SIZE = 50000

#학번 8자리 출력
#O(n)

#stack
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



#implementing Heap-sort
def adjust(a, i, size):
    while 2 * i + 1 <= size:
    #node의 왼쪽 index를 저장, root에는 root node의 index 저장
        child = i * 2 + 1
        root = i

        # 해당 depth에서 왼쪽과 오른쪽 child node 중 더 큰 수를 indexing 하는 역할
        if child < size and a[child][1] < a[child + 1][1]:
            child += 1

        # 이미 root node에 가장 큰 Data가 있는 경우엔 break
        if a[root][1] >= a[child][1]:
            break
        # 그렇지 않은 경우에는 위에서 비교했던 child node 중 큰 것과 변경 
        a[root], a[child] = a[child], a[root]
        i = child

def heap_sort(a):
    hsize = len(a) - 1   
    #initializing
    for i in reversed(range((hsize + 1)//2)):
        adjust(a, i, hsize)

    #sorting
    for i in range(hsize):
        a[0], a[hsize] = a[hsize], a[0]
        adjust(a, 0, hsize-1)
        hsize -= 1
    
    return a



#Quick Sort with no recursive
def partition(a, start, end):
    pivot = a[start][1]
    left = start + 1
    right = end
    while True:
        while left <= right and a[left][1] <= pivot:
            left += 1
        while left <= right and a[right][1] > pivot:
            right -= 1

        if right < left:
            break
        else: 
            a[left], a[right] = a[right], a[left]
    
    a[start], a[right] = a[right], a[start]
    return right

def quicksort_without_recursive(a):
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


#quicksort with recursive
def quicksort_recursive(a):
    if len(a) <= 1:
        return a
    
    pivot = a[0]
    tail = a[1:]

    left = [x for x in tail if x[1] <= pivot[1]]
    right = [x for x in tail if x[1] > pivot[1]]

    return quicksort_recursive(left) + [pivot] + quicksort_recursive(right)




#Make Data
random_id = random.sample(range(10000000, 100000000), DATA_SIZE)
original_data = list()
for r in random_id:
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
    phone_number = "010" + str(format(random.randint(0, 100000000), "08")) 
    original_data.append([r, name, phone_number])


#Producing original data
print("Original Data")
#for student in original_data:
#    print(student)

selection_sorting_data = original_data.copy()
quick_sorting_without_recursive_data = original_data.copy()
quick_sorting_with_recursive_data = original_data.copy()
heap_sorting_data = original_data.copy()



#Sorting by Python inherited method
#Sorted는 정렬 대상이 되는 Data를 받아 정렬한 리스트를 리턴하기 때문에 기존의 데이터는 변화가 없다.
python_inherited_sorting_time = time.time()
python_inherited_sorting = sorted(original_data, key=lambda name: name[1])
python_inherited_sorting_time = time.time() - python_inherited_sorting_time

#Python inherited sorting result
print('\nPython inherited sorting')
#for student in python_inherited_sorting:
#    print(student)
print(python_inherited_sorting_time)


#Sorting by Heap-sorting
heap_sorting_time = time.time()
heap_sort(heap_sorting_data)
heap_sorting_time = time.time() - heap_sorting_time

#Heap sorting result
print('\nHeap-sorting')
#for student in heap_sorting_data:
#    print(student)
print(heap_sorting_time)






#Sorting by Quick-sorting withtout recursive
quick_sorting_without_recursive_time = time.time()
quicksort_without_recursive(quick_sorting_without_recursive_data)
quick_sorting_without_recursive_time = time.time() - quick_sorting_without_recursive_time

#Quick sorting without recursive result
print('\nQuick-sorting without recursive')
#for student in quick_sorting_without_recursive_data:
#    print(student)
print(quick_sorting_without_recursive_time)






#Sorting by Quick-sorting with recursive
quick_sorting_with_recursive_time = time.time()
quick_sorting_with_recursive_data = quicksort_recursive(quick_sorting_with_recursive_data)
quick_sorting_with_recursive_time = time.time() - quick_sorting_with_recursive_time

#Quick sorting with recursive result
print('\nQuick-sorting with recursive')
#for student in quick_sorting_with_recursive_data:
#    print(student)
print(quick_sorting_with_recursive_time)