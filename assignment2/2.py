class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
        self.call = 0

    def push(self, val):
        self.items.append(val)
        self.call += 1

    def pop(self):
        try:
            self.call += 1
            return self.items.pop()
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

    def how_many(self):
        return self.call

class Point:
    def __init__(self, row, col):
        #openned = 1, closed = 0
        self.top = 1
        self.right = 1
        self.bottom = 1
        self.left = 1
        self.__location = (row, col)
        self.icon = " "

    def get_location(self):
        return self.__location
    
    def set_location(self, location):
        self.__location = location

class Maze:
    maze_row = 12
    maze_col = 9
    commands = (
        #vertical, horizontal
        #in vertical -1 for top closed, 1 for bottom closed, 2 for all closed
        #in horizontal -1 for left closed, 1 for right closed, 2 for all closed
        ((-1, -1), (2, 0), (2, 0), (-1, 1), (2, -1), (2, 0), (-1, 0), (-1, 1), (-1, 2)),
        ((1, -1), (2, 0), (-1, 1), (0, 2), (-1, -1), (2, 0), (0, 1), (0, 2), (0, 2)),
        ((-1, -1), (2, 0), (0, 1), (1, -1), (1, 1), (-1, -1), (1, 1), (0, 2), (0, 2)),
        ((0, 2), (-1, 2), (1, 2), (-1, 2), (-1, 2), (1, 2), (-1, -1), (1, 0), (0, 1)),
        ((0, 2), (0, 2), (-1, -1), (0, 1), (1, -1), (2, 0), (1, 1), (-1, -1), (0, 1)),
        ((0, -1), (1, 1), (0, 2), (0, -1), (2, 0), (2, 1), (2, -1), (1, 1), (0, 2)),
        ((1, -1), (2, 0), (1, 1), (0, 2), (-1, -1), (2, 0), (2, 0), (-1, 0), (0, 1)),
        ((-1, 2), (-1, -1), (2, 0), (1, 1), (0, 2), (-1, -1), (2, 0), (1, 1), (1, 2)),
        ((0, 2), (1, -1), (2, 0), (-1, 0), (1, 1), (1, -1), (-1, 0), (2, 0), (-1, 1)),
        ((0, -1), (2, 0), (-1, 1), (0, -1), (-1, 1), (-1, 2), (1, 2), (-1, 2), (0, 2)),
        ((1, -1), (-1, 1), (0, 2), (0, 2), (0, 2), (0, -1), (2, 0), (1, 1), (0, 2)),
        ((2, -1), (1, 1), (1, -1), (1, 1), (1, -1), (1, 1), (2, -1), (2, 0), (1, 1)),
    )

    def __init__(self):
        #make empty 2 dimension list
        self.final_path = []
        self.composition = [[0 for col in range(self.maze_col)] for row in range(self.maze_row)]
        
        #assign Point class to each 2 dimension list
        for row in range(self.maze_row):
            for col in range(self.maze_col):
                self.composition[row][col] = Point(row, col)

        #setting Point class's information
        for row in range(self.maze_row):
            for col in range(self.maze_col):
                self.set_point(row, col, self.commands[row][col])

        #setting start and end Point
        self.start_point = self.composition[0][0]
        self.end_point = self.composition[-1][-1]
        
    def set_point(self, row, col, command):
        vertical = command[0]
        horizontal = command[1]

        # closed top = -1, closed bottom = 1, closed both side = 2
        if vertical == -1:
            self.composition[row][col].top = 0
        elif vertical == 1:
            self.composition[row][col].bottom = 0
        elif vertical == 2:
            self.composition[row][col].top = 0
            self.composition[row][col].bottom = 0

        # closed left = -1, closed right = 1, closed both side = 2
        if horizontal == -1:
            self.composition[row][col].left = 0
        elif horizontal == 1:
            self.composition[row][col].right = 0
        elif horizontal == 2:
            self.composition[row][col].left = 0
            self.composition[row][col].right = 0

    def get_down(self, current):
        row, col = current.get_location()
        return self.composition[row + 1][col]

    def get_up(self, current):
        row, col = current.get_location()
        return self.composition[row - 1][col]

    def get_left(self, current):
        row, col = current.get_location()
        return self.composition[row][col - 1]

    def get_right(self, current):
        row, col = current.get_location()
        return self.composition[row][col + 1]

    def set_path(self):
        for point in self.final_path:
            point.icon = "*"

    #get path
    def get_path(self):
        #path_stack initialize
        path_stack = Stack()
        visited = []

        path_stack.push([self.start_point, self.start_point])
        print("PUSH", path_stack.peak()[0].get_location())
        current = path_stack.peak()[0]
        recent = path_stack.peak()[1]
        final = []

        # current가 end_point에 도달할 때 까지
        while True:

            if path_stack.isEmpty():
                print("\n스택 활용 횟수 %d회\n" % path_stack.call)
                self.final_path = final
                self.print_result()
                break

            # top bottom left right
            temp = [0, 0, 0, 0]
            # 만약 해당 Point에서 열려있고 가장 최근에 방문했던 path가 아닌 것들을 temp리스트에 넣음
            # temp 리스트의 길이가 0이면 막혀있음
            # temp 리스트의 길이가 1이면 포인트를 다음 포인트로 변경하여 다음 while 문 진행
            # temp 리스트의 길이가 2이면 해당 포인트를 stack에 넣고 둘 중 하나를 선택한 후 다음 포인트를 진행
            if current.top and self.get_up(current) not in visited:
                temp[0] = 1
            if current.bottom and self.get_down(current) not in visited:
                temp[1] = 1
            if current.left and self.get_left(current) not in visited:
                temp[2] = 1
            if current.right and self.get_right(current) not in visited:
                temp[3] = 1

            #막혔다면
            if (temp[0] + temp[1] + temp[2] + temp[3]) == 0:
                print("POP", path_stack.peak()[0].get_location())

                previous_point = path_stack.pop()
                current = previous_point[0]
                recent = previous_point[1]
                pop_index = visited.index(recent)
                visited = visited[:pop_index + 1]

            #막히지 않았다면
            else:
                target = current

                if temp[0]:
                    target = self.get_up(current)
                    path_stack.push([target, current])
                    print("PUSH", path_stack.peak()[0].get_location())

                if temp[2]:
                    target = self.get_left(current)
                    path_stack.push([target, current])
                    print("PUSH", path_stack.peak()[0].get_location())

                if temp[1]:
                    target = self.get_down(current)
                    path_stack.push([target, current])
                    print("PUSH", path_stack.peak()[0].get_location())

                if temp[3]:
                    target = self.get_right(current)
                    path_stack.push([target, current])
                    print("PUSH", path_stack.peak()[0].get_location())
                
                if current == self.end_point:
                    visited.append(current)
                    end_point_index = visited.index(current)

                    final.append(visited[:end_point_index + 1])
                else:
                    visited.append(current)


                print("POP", path_stack.peak()[0].get_location())
                next_point = path_stack.pop()
                current = next_point[0]
                recent = next_point[1]


                    
    # printing Maze itself
    def print_maze(self):

        #print top line
        for col in range(self.maze_col):
            print("%3s" % "_______", end="")
        print()

        #print two rows

        for row in range(self.maze_row):

            for i in range(2):

                for col in range(self.maze_col):

                    if i == 1 and self.composition[row][col].icon != " ":
                        if col == 0:
                            print("|", end=" ")
                            print(self.composition[row][col].icon * 2, end="  ")
                        else:
                            print(" ", end=" ")
                            print(self.composition[row][col].icon * 2, end="  ")
                    else:
                        if col == 0:
                            print("|", end="     ")
                        else:
                            print(" ", end="     ")                        


                    if not(self.composition[row][col].right):
                        print("|", end="")
                    else:
                        print(" ", end="")
                print()            

            #print last row

            for col in range(self.maze_col):

                if col == 0:
                    if (self.composition[row][col].bottom):
                        print("|", end="    ")
                    else:
                        print("|", end="____")
                elif not(self.composition[row][col].bottom):
                    print("_" * 5, end="")
                else:
                    print(" " * 5, end="")


                if not(self.composition[row][col].bottom):
                    print("_", end="")
                else:
                    print(" ", end="")
                    
                #print right
                if not(self.composition[row][col].right):
                    print("|", end = "")
                else:
                    if not(self.composition[row][col].bottom):
                        print("_", end="")
                    else:
                        print(" ", end="")
            print()

    def print_result(self):
        paths = self.final_path

        if len(paths):
            print("모두 %d개의 길을 찾았습니다." % len(paths))
            print("가장 짧은 길을 표시합니다")
            final = paths[0]
            for path in paths[1:]:
                if len(path) < len(final):
                    final = path

            self.final_path = final
            #시작점은 거리계산에서 빼기 때문에 -1을 해줌
            print("(거리 %d)" % (len(final) - 1))
        else:
            print("경로가 없습니다.")

a = Maze()
print("미로를 표시합니다.")
a.print_maze()

a.get_path()
a.set_path()

print("최종 경로를 표시합니다.")
a.print_maze()