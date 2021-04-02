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

    def top(self):
        try:
            return self.items[-1]
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


def get_postfix(equation):
    postfix_equation = list()
    Operator_stack = Stack()

    operators = {"(": 0, ")": 0, "+": 1, "-": 1,
                 "*": 2, "/": 2, "%": 2, "^": 3}
    temp = ""
    for e in equation:
        # 후위식으로 바꾸기
        if e not in operators.keys():  # 숫자를 만난 경우
            temp += e
        else:
            if temp:
                postfix_equation.append(temp)
                temp = ""

            if Operator_stack.isEmpty() or e == "(":
                Operator_stack.push(e)
            else:

                if operators[Operator_stack.peak()] < operators[e]:
                    Operator_stack.push(e)
                elif e == ")":
                    while True:
                        if Operator_stack.peak() == "(":
                            Operator_stack.pop()
                            break
                        postfix_equation.append(Operator_stack.pop())
                else:
                    postfix_equation.append(Operator_stack.pop())
                    while not(Operator_stack.isEmpty()) and operators[Operator_stack.peak()] >= operators[e]:
                        postfix_equation.append(Operator_stack.pop())
                    Operator_stack.push(e)
    if temp:
        postfix_equation.append(temp)

    while not Operator_stack.isEmpty():
        postfix_equation.append(Operator_stack.pop())

    return(postfix_equation)


def get_value(equation):

    postfix = get_postfix(equation)

    operator = {"+": 1, "-": 1, "*": 2, "%": 2, "^": 3}

    calculating_stack = Stack()

    for token in postfix:
        if token in operator.keys():
            n2 = calculating_stack.pop()
            n1 = calculating_stack.pop()

            if token == "+":
                result = int(n1) + int(n2)
            elif token == "-":
                result = int(n1) - int(n2)
            elif token == "*":
                result = int(n1) * int(n2)
            elif token == "%":
                result = int(n1) % int(n2)
            elif token == "^":
                result = int(n1) ** int(n2)

            calculating_stack.push(result)

        else:
            calculating_stack.push(token)

    return(calculating_stack.pop())


def print_error(space):
    print(" " * space + "^ 이 위치에 오류가 있습니다.")
    return True


while True:
    equation = input("")
    operator = {"+": 1, "-": 1, "*": 2, "%": 2, "^": 3}
    errored = False

    if not equation[0].isnumeric():
        errored = print_error(space)
    elif equation[-1] in operator.keys():
        print(' ' * (len(equation)-1), end="")
        errored = print_error(space)
    else:
        flag = [0, 0]  # isnum, braket_opened
        space = 0
        for e in equation:

            if e.isnumeric():
                space += 1
                flag = [1, flag[1]]
            elif e not in operator.keys():
                errored = print_error(space)
                break
            elif e == "(":
                if flag[0] == 1:
                    errored = print_error(space)
                    break
                flag[1] = 1
                space += 1
            elif e == ")":
                if not flag[1]:
                    errored = print_error(space)
                    break
                else:
                    flag[1] = 0
                    space += 1
            else:
                if not flag[0]:
                    errored = print_error(space)
                    break
                space += 1
                flag = [0, flag[1]]
        else:
            if flag[1]:
                errored = print_error(space)

    if not errored:
        print(f"= {get_value(equation)}")
