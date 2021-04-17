import random
import string
import time

#Define Data Size
DATA_SIZE = 50000

#학번 8자리 출력
#O(n)

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

    return a

def heap_sort(a):
    hsize = len(a) - 1   
    #initializing
    for i in reversed(range((hsize + 1)//2)):
        a = adjust(a, i, hsize)

    #sorting
    for i in range(hsize):
        a[0], a[hsize] = a[hsize], a[0]
        a = adjust(a, 0, hsize-1)
        hsize -= 1
    
    return a



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
quick_sorting_data = original_data.copy()
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
heap_result = heap_sort(heap_sorting_data)
heap_sorting_time = time.time() - heap_sorting_time

#Python inherited sorting result
print('\nHeap-sorting')
#for student in heap_result:
#    print(student)
print(heap_sorting_time)