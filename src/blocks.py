class Blocks:
    def __init__(self, color, y, board):
        self.color = color
        self.y = y
        self.board = board
        self.board_center = int(len(board[0]) // 2)

    def blockI(self):
        for i in range(self.board_center-1, self.board_center+3):
            self.board[x][i] = 1

    def blockO(self):
        for i in range(self.board_center, self.board_center+2):
            for j in range(2):
                self.board[x+j][i] = 1

    def blockT(self):
        for i in range(self.board_center-1, self.board_center+2):
            self.board[x][i] = 1
        self.board[x+1][self.board_center] = 1
