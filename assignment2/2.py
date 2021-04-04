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

class Point:
    def __init__(self, row, col):
        #openned = 1, closed = 0
        self.top = 1
        self.right = 1
        self.bottom = 1
        self.left = 1
        self.__location = (row, col)
    
    def get_location(self):
        return self.__location
    
    def set_location(self, location):
        self.__location = location

    def __str__(self):
        return "(%2d %2d)" % self.__location

class Maze:
    maze_row = 12
    maze_col = 9
    commands = (
        #row, col, vertical, horizontal
        #in vertical -1 for top closed, 1 for bottom closed, 2 for all closed
        #in horizontal -1 for left closed, 1 for right closed, 2 for all closed

        #vertical, horizontal
        ((-1, -1), (2, 0), (2, 0), (-1, 1), (2, -1), (2, 0), (-1, 0), (-1, 1), (-1, 2)),
        ((1, -1), (2, 0), (-1, 1), (0, 2), (-1, -1), (2, 0), (0, 1), (0, 2), (0, 2)),
        ((-1, -1), (2, 0), (0, 1), (1, -1), (1, 1), (-1, -1), (1, 1), (0, 2), (0, 2)),
        ((0, 2), (-1, 2), (1, 2), (-1, 2), (-1, 2), (1, 2), (-1, -1), (1, 0), (0, 1)),
        ((0, 2), (0, 2), (-1, -1), (0, 1), (1, -1), (2, 0), (1, 1), (-1, -1), (0, 1)),
        ((0, -1), (1, 1), (0, 2), (0, -1), (2, 0), (2, 1), (2, -1), (1, 1), (0, -1)),
        ((1, -1), (2, 0), (1, 1), (0, 2), (-1, -1), (2, 0), (2, 0), (-1, 0), (0, 1)),
        ((-1, 2), (-1, -1), (2, 0), (1, 1), (0, 2), (-1, -1), (2, 0), (1, 1), (1, 2)),
        ((0, 2), (1, -1), (2, 0), (-1, 0), (1, 1), (1, -1), (-1, 0), (2, 0), (-1, 0)),
        ((0, -1), (2, 0), (-1, 1), (0, -1), (-1, 1), (-1, 2), (1, 2), (-1, 2), (0, 2)),
        ((1, -1), (-1, 1), (0, 2), (0, 2), (0, 2), (0, -1), (2, 0), (1, 1), (0, 2)),
        ((2, -1), (1, 1), (1, -1), (1, 1), (1, -1), (1, 1), (2, -1), (2, 0), (1, 1)),
    )

    def __init__(self):
        self.composition = [[0 for col in range(self.maze_col)] for row in range(self.maze_row)]
        
        for row in range(self.maze_row):
            for col in range(self.maze_col):
                self.composition[row][col] = Point(row, col)

        for col in range(self.maze_col):
            self.composition[0][col].top = 0
            self.composition[-1][col].bottom = 0
        for row in range(self.maze_row):
            self.composition[row][0].left = 0
            self.composition[row][-1].right = 0

        for row in range(self.maze_row):
            for col in range(self.maze_col):
                print(row, col, self.commands[row][col])
                self.set_point(row, col, self.commands[row][col])
        
    def set_point(self, row, col, command):
        vertical = command[0]
        horizontal = command[1]

        if vertical == -1:
            self.composition[row][col].top = 0
        elif vertical == 1:
            self.composition[row][col].bottom = 0
        elif vertical == 2:
            self.composition[row][col].top = 0
            self.composition[row][col].bottom = 0

        if horizontal == -1:
            self.composition[row][col].left = 0
        elif horizontal == 1:
            self.composition[row][col].right = 0
        elif horizontal == 2:
            self.composition[row][col].left = 0
            self.composition[row][col].right = 0
        
    
    #For Debugging
    def print_composition(self):
        for row in range(self.maze_row):
            for col in range(self.maze_col):
                print(self.composition[row][col], end=" ")
            print()

    def print_maze(self):
        for col in range(self.maze_col):
            print("%s" % "___", end="")
            
        print()
        for row in range(self.maze_row):
            
            #print left
            print("|", end="")

            for col in range(self.maze_col):

                #print bottom
                if not(self.composition[row][col].bottom):
                    print("%s" % "__", end = "")
                else:
                    print("%2s" % " ", end = "")
                
                #print right
                if not(self.composition[row][col].right):
                    print("%s" % "|", end = "")
                else:
                    print("%s" % " ", end = "")
            
            print()

    


    def print_maze_v2(self):
        #print top
        for col in range(self.maze_col):
            print("%3s" % "____", end="")
        print()

        #print two rows

        for row in range(self.maze_row):

            for i in range(2):

                print("|", end=" ")

                for col in range(self.maze_col):

                    if not(self.composition[row][col].right):
                        print("%s" % "|", end = " ")
                    else:
                        print("%s" % " ", end = " ")
                print()            

            #print last row
            print("|", end=" ")

            for col in range(self.maze_col):
                if not(self.composition[row][col].bottom):
                    print("%3s" % "__"*3, end = "")
                else:
                    print("%3s" % " "*3, end = "")
                
                #print right
                if not(self.composition[row][col].right):
                    print("%2s" % " " * 2, end="")
                    print("%s" % "|", end = "")
                else:
                    print("%3s" % " ", end = "")
            
            print()


a = Maze()
a.print_maze()
a.print_maze_v2()