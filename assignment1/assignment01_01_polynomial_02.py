class polynomial():
    def __init__(self, coef):
        self.coef = coef
        self.num = len(coef)

    def print_poly(self):
        for coef in self.coef:
            print(f"{coef[0]} {coef[1]}", end=" ")

    def substitute(self, x):
        result = 0
        for c in self.coef:
            result += c[0]*x**c[1]
        return result


def poly_add(e_01, e_02):
    pos_01 = 0
    pos_02 = 0
    result = []

    while pos_01 < e_01.num and pos_02 < e_02.num:
        coef_degree_01 = e_01.coef[pos_01]
        coef_degree_02 = e_02.coef[pos_02]

        # 더 큰 차수가 먼저 확인되기 때문에 자동 정렬
        if coef_degree_01[1] > coef_degree_02[1]:
            result.append(coef_degree_01)
            pos_01 += 1
        elif coef_degree_01[1] < coef_degree_02[1]:
            result.append(coef_degree_02)
            pos_02 += 1
        else:
            result.append(
                [coef_degree_01[0]+coef_degree_02[0], coef_degree_01[1]])
            pos_01 += 1
            pos_02 += 1

    return polynomial(result)


def poly_multiply(e_01, e_02):
    result = dict()
    for e1 in e_01.coef:
        for e2 in e_02.coef:

            if e1[1] + e2[1] in result.keys():
                result[e1[1] + e2[1]] += e1[0]*e2[0]
            else:
                result[e1[1] + e2[1]] = e1[0]*e2[0]

    # 차수기준 내림차순으로 정렬
    result = sorted(result.items(), key=lambda x: x[0], reverse=True)

    coef = list()
    for r in result:
        coef.append([r[1], r[0]])

    return polynomial(coef)


def get_equation(n):
    equation = input(f"수식 {n+1}을 입력하세요 :")
    coef = [int(c) for c in equation.split(' ')]
    result = [coef[i:i+2] for i in range(0, len(coef), 2)]
    return polynomial(result)


poly_list = list()
for n in range(2):
    poly_list.append(get_equation(n))
poly_list.append(poly_add(poly_list[0], poly_list[1]))
poly_list.append(poly_multiply(poly_list[0], poly_list[1]))
# 1 4 1 2 1 0
# 11 5 1 4 1 1
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
