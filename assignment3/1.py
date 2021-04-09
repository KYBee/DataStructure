import random
import string
#학번 8자리 출력

#O(n)
random_id = random.sample(range(10000000, 100000000), 10)
print(random_id)

final_list = list()

for r in random_id:
    #TODO 이름, 전화번호
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
    phone_number = "010" + str(format(random.randint(0, 100000000), "08")) 
    final_list.append([r, name, phone_number])

print(final_list)