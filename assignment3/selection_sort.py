def selection_sort(a):
    l = len(a)
    for i in range(l - 1):
        least = i
        for j in range(i + 1, l):
            if a[j] < a[least]:
                least = j
        
        a[i], a[least] = a[least], a[i]

a = [3, 4, 5, 2, 10, 22, 34, 1]
selection_sort(a)
print(a)