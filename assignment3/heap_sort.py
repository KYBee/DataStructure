def adjust(a, i, size):
    while 2 * i + 1 <= size:
    #node의 왼쪽 index를 저장, root에는 root node의 index 저장
        child = i * 2 + 1
        root = i

        # 해당 depth에서 왼쪽과 오른쪽 child node 중 더 큰 수를 indexing 하는 역할
        if child < size and a[child] < a[child + 1]:
            child += 1

        # 이미 root node에 가장 큰 Data가 있는 경우엔 break
        if a[root] >= a[child]:
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
    

num_list = [3, 5, 1, 2, 4, 8, 9, 10, 111]

heap_sort(num_list)
print(num_list)