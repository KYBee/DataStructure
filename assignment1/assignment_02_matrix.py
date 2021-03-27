class matrix():
    def __init__(self, size, data):
        self.size = size
        self.data = data

    def print_normal(self):
        for i in range(0, self.size**2, self.size):
            for n in range(self.size):
                print(self.data[i+n], end=' ')
            print()

    def print_sparse(self):
        for l in self.data:
            for d in l:
                print(d, end=' ')
            print()


def get_normal(i):
    raw = input(f"행렬 {i}의 데이터를 입력하세요. ")
    data = [int(d) for d in raw.split(' ')]
    return data


def add_normal(s, m1, m2):
    return [m1.data[i] + m2.data[i] for i in range(s**2)]


def multiply_normal(s, m1, m2):
    size = s ** 2
    d1 = m1.data
    d2 = m2.data
    result = list()
    for j in range(0, size, s):
        for i in range(s):
            n = j
            sum_n = 0
            for m in range(i, size, s):
                sum_n += d1[n]*d2[m]
                n += 1
            result.append(sum_n)
    return result


def get_sparse(i, s):
    normal = matrixes[i].data
    result = [[index//s, index % s, datum]
              for index, datum in enumerate(normal) if datum]
    return result


def compare_same(i, d1, d2):
    if d1[i] < d2[i]:
        return 0
    elif d1[i] > d2[i]:
        return 1
    elif d1[i+1] == d2[i+1]:
        return 2
    else:
        return compare_same(i+1, d1, d2)


def add_sparse(s, m1, m2):
    data1 = m1.data
    data2 = m2.data
    result = list()
    a = b = 0
    while True:
        d = [data1[a], data2[b]]
        r = compare_same(0, d[0], d[1])
        if r == 2:
            result.append([d[0][0], d[0][1], d[0][2]+d[1][2]])
            a += 1
            b += 1
        else:
            result.append(d[r])
            if r:
                b += 1
            else:
                a += 1

        if a == len(data1):
            for d in data2[b:]:
                result.append(d)
            break
        elif b == len(data2):
            for d in data1[a:]:
                result.append(d)
            break
    return result


def multiply_sparse(s, m1, m2):
    data1 = m1.data
    data2 = m2.data
    p1 = p2 = 0

    result = list()
    for i in range(s):
        for j in range(s):
            sum_n = 0
            for d1 in data1:
                if d1[0] == i:
                    for d2 in data2:
                        if d2[1] == j and d1[1] == d2[0]:
                            sum_n += d1[2]*d2[2]
            if sum_n:
                result.append([i, j, sum_n])
    return result


s = int(input("행렬의 규격을 입력하세요. "))
size = s**2

print('방식 1:')
matrixes = [matrix(s, get_normal(i)) for i in range(1, 3)]
for i in range(0, 2):
    print(f'행렬 {i+1}({size})')
    matrixes[i].print_normal()

d = add_normal(s, matrixes[0], matrixes[1])
matrixes.append(matrix(s, d))
d = multiply_normal(s, matrixes[0], matrixes[1])
matrixes.append(matrix(s, d))

print(f'행렬1+2({size})')
matrixes[2].print_normal()

print(f'행렬 1*2({size})')
matrixes[3].print_normal()

print('\n방식 2:')
for i in range(2):
    d = get_sparse(i, s)
    matrixes.append(matrix(3*len(d), d))

print(f'행렬 3({matrixes[4].size}개)')
matrixes[4].print_sparse()

print(f'행렬 4({matrixes[5].size}개)')
matrixes[5].print_sparse()

d = add_sparse(s, matrixes[4], matrixes[5])
matrixes.append(matrix(3*len(d), d))
d = multiply_sparse(s, matrixes[4], matrixes[5])
matrixes.append(matrix(3*len(d), d))

print(f'행렬 3+4({matrixes[6].size}개)')
matrixes[6].print_sparse()

print(f'행렬 3*4({matrixes[7].size}개)')
matrixes[7].print_sparse()
