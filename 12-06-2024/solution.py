class solution:
    def __init__(self, file_name):
        self.board = []
        with open(file_name, "r") as file:
            for line in file:
                self.board.append(list(line.strip()))
        self.current_x, self.current_y = 0, 0
        self.find_position()
        self.current_pos = self.board[self.current_x][self.current_y]
        self.border_x = len(self.board)
        self.border_y = len(self.board[0])
        # self.distinct_positions = self.get_distinct_positions()
        self.distinct_positions = 0

    def add(self, a, b):
        return a+b

    ### UTILITY ###
    def find_position(self):
        for ri, row in enumerate(self.board):
            for ci, col in enumerate(row):
                if col == "^":
                    self.current_x = ri
                    self.current_y = ci

    def is_blocked(self):
        if self.board[self.current_x][self.current_y] == "^" and self.board[self.current_x - 1][self.current_y] == "#":
            return True
        elif self.board[self.current_x][self.current_y] == "V" and self.board[self.current_x + 1][self.current_y] == "#":
            return True
        elif self.board[self.current_x][self.current_y] == ">" and self.board[self.current_x][self.current_y + 1] == "#":
            return True
        elif self.board[self.current_x][self.current_y] == "<" and self.board[self.current_x][self.current_y - 1] == "#":
            return True

        return False

    def move_forward(self):
        if self.board[self.current_x][self.current_y] == "^":
            self.move_up()
        elif self.board[self.current_x][self.current_y] == "V":
            self.move_down()
        elif self.board[self.current_x][self.current_y] == ">":
            self.move_right()
        elif self.board[self.current_x][self.current_y] == "<":
            self.move_left()

    def move_up(self):
        self.current_x -= 1
        if self.board[self.current_x][self.current_y] == ".":
            self.distinct_positions += 1
        self.set_current_pos("^")
        self.board[self.current_x + 1][self.current_y] = "X"
        return

    def move_down(self):
        self.current_x += 1
        if self.board[self.current_x][self.current_y] == ".":
            self.distinct_positions += 1
        self.set_current_pos("V")
        self.board[self.current_x - 1][self.current_y] = "X"
        return

    def move_right(self):
        self.current_y += 1
        if self.board[self.current_x][self.current_y] == ".":
            self.distinct_positions += 1
        self.set_current_pos(">")
        self.board[self.current_x][self.current_y - 1] = "X"
        return

    def move_left(self):
        self.current_y -= 1
        if self.board[self.current_x][self.current_y] == ".":
            self.distinct_positions += 1
        self.set_current_pos("<")
        self.board[self.current_x][self.current_y + 1] = "X"
        return

    def turn_right(self):
        if self.board[self.current_x][self.current_y] == "^":
            self.set_current_pos(">")
        elif self.board[self.current_x][self.current_y] == ">":
            self.set_current_pos("V")
        elif self.board[self.current_x][self.current_y] == "V":
            self.set_current_pos("<")
        elif self.board[self.current_x][self.current_y] == "<":
            self.set_current_pos("^")


    def get_distinct_positions(self):
        while True:
            if ((self.get_current_pos() == "^" or self.get_current_pos() == "V") and (self.current_x+1 >= len(self.board) or self.current_x - 1 < 0)) or ((self.get_current_pos() == ">" or self.get_current_pos() == "<") and (self.current_y+1 >= len(self.board[0]) or self.current_y - 1 < 0)):
                self.distinct_positions += 1
                break
            elif self.is_blocked():
                self.turn_right()
            else:
                self.move_forward()
            print(self.distinct_positions)
        return self.distinct_positions

    def get_current_pos(self):
        return self.board[self.current_x][self.current_y]

    def set_current_pos(self, char):
        self.board[self.current_x][self.current_y] = char

    ### PRINTERS ###
    def print_board(self): 
        print("--------------------------------------------------")
        for row in self.board:
            print(row)
