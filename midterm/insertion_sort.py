def insertion_sort(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key > data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

a = [1, 2, 3, 4, 5]
insertion_sort(a)

print(a)