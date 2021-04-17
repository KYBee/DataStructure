import random
import string
import time

#Define Data Size
DATA_SIZE = 50000

#학번 8자리 출력
#O(n)
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


#Sorting by Python inherited method
#Sorted는 정렬 대상이 되는 Data를 받아 정렬한 리스트를 리턴하기 때문에 기존의 데이터는 변화가 없다.
python_inherited_sorting_time = time.time()
python_inherited_sorting = sorted(original_data, key=lambda name: name[1])
python_inherited_sorting_time = time.time() - python_inherited_sorting_time

print(python_inherited_sorting_time)

print('\nPython inherited sorting')
#for student in python_inherited_sorting:
#    print(student)
