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
            return self.items.pop()
            self.call += 1
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
        self.__checked = False
    
    def down(self):
        return (self.__location[0] + 1, self.__location[1])

    def up(self):
        return (self.__location[0] - 1, self.__location[1])

    def left(self):
        return (self.__location[0], self.__location[1] - 1)

    def right(self):
        return (self.__location[0], self.__location[1] + 1)


    def get_location(self):
        return self.__location
    
    def set_location(self, location):
        self.__location = location

    def get_checked(self):
        return self.__checked
    
    def set_checked(self):
        return self.__checked

    def __str__(self):
        return str((self.__location[0], self.__location[1]))

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
        ((0, 2), (-1, 2), (1, 2), (-1, 2), (-1, 2), (1, 2), (-1, -1), (1, 0), (1, 1)),
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

    #get path
    def get_path(self):
        #path_stack initialize
        path_stack = Stack()

        current = self.start_point
        recent = self.start_point

        row, col = 0, 0
        visited = []

        # current가 end_point에 도달할 때 까지
        while current.get_location() != self.end_point.get_location():
            # top bottom left right
            temp = [0, 0, 0, 0]
            # 만약 해당 Point에서 열려있고 가장 최근에 방문했던 path가 아닌 것들을 temp리스트에 넣음
            # temp 리스트의 길이가 0이면 막혀있음
            # temp 리스트의 길이가 1이면 포인트를 다음 포인트로 변경하여 다음 while 문 진행
            # temp 리스트의 길이가 2이면 해당 포인트를 stack에 넣고 둘 중 하나를 선택한 후 다음 포인트를 진행
            if current.top and current.up() != recent.get_location():
                temp[0] = 1
            elif current.bottom and current.down() != recent.get_location():
                temp[1] = 1
            elif current.left and current.left() != recent.get_location():
                temp[2] = 1
            elif current.right and current.right() != recent.get_location():
                temp[3] = 1
            
            
               
        
        
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



a = Maze()
a.print_maze()


b = Point(1, 1)
print(b.down())
print(b)