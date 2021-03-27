class polynomial():
    def __init__(self, coef):
        self.coef = coef
        self.degree = len(coef) - 1

    def print_poly(self):
        for coef in self.coef:
            print(coef, end=" ")

    def substitute(self, x):
        result = 0
        for i in range(self.degree+1):
            if not self.coef[i]:  # 계수가 0인 경우
                continue
            else:
                result += self.coef[i]*x**(self.degree-i)
        return result


def get_equation(n):
    equation = input(f"수식 {n+1}을 입력하세요 :")
    result = [int(e) for e in equation.split(' ')]
    return polynomial(result)


def poly_add(e_01, e_02):
    result = list()
    # 포인터 처럼 사용할 친구들 pos_01과 pos_02
    pos_01 = 0
    pos_02 = 0

    while pos_01 <= e_01.degree and pos_02 <= e_02.degree:
        index_01 = e_01.degree - pos_01
        index_02 = e_02.degree - pos_02

        # 더 큰 차수를 먼저 확인하고, 같은 차수는 계수끼리 더해서 추가
        if index_01 > index_02:
            result.append(e_01.coef[pos_01])
            pos_01 += 1
        elif index_01 < index_02:
            result.append(e_02.coef[pos_02])
            pos_02 += 1
        else:
            result.append(e_01.coef[pos_01] + e_02.coef[pos_02])
            pos_01 += 1
            pos_02 += 1

    return polynomial(result)


def poly_multiply(e_01, e_02):
    r = list()
    result = list()
    result_degree = e_02.degree + e_01.degree + 1

    for n, e1 in enumerate(e_01.coef):
        # 자리수에 맞추어 한 번에 더할 수 있게 빈 공간은 0으로 채우기
        i = result_degree
        l = list()
        for _ in range(n):
            l.append(0)
            i -= 1
        for e2 in e_02.coef:
            l.append(e1 * e2)
            i -= 1
        for _ in range(i):
            l.append(0)
        r.append(l)

    for i in range(result_degree):
        s = 0
        for l in range(len(r)):
            s += r[l][i]
        result.append(s)

    return polynomial(result)


poly_list = list()
for n in range(2):
    poly_list.append(get_equation(n))
poly_list.append(poly_add(poly_list[0], poly_list[1]))
poly_list.append(poly_multiply(poly_list[0], poly_list[1]))

print('수식 1 + 2는 ', end="")
poly_list[2].print_poly()
print()
print('수식 1 * 2는 ', end="")
poly_list[3].print_poly()
print()

while True:
    question = input("수식에 값을 넣으세요 ")

    if question == 'end':
        break
    question = question.split(" ")
    result = poly_list[int(question[0])-1].substitute(int(question[1]))
    print(f"결과값은 {result}")
