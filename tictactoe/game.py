import random


class Board:
    def __init__(self):
        self.turn = 1
        self.status = None
        self.state = [
           ["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]
        ]

    def move (self, r, c):
        if self.valid_move(r, c) is True:
            self.state[r][c] = "X" if self.turn % 2 == 1 else "O"
            self.status = self.check_status(r, c)
            self.turn += 1

    def valid_move(self, r, c):
        err_s=''
        if r < 0 or r > 2 or c < 0 or c > 2:
            return "Invalid position provided"
        if self.state[r][c] == "X" or self.state[r][c] == "O":
            err_s += "This position is already taken"
        if err_s: return err_s
        return True

    def check_status(self, r, c):
        symbol = self.state[r][c]

        if self.state[r][0] == symbol and self.state[r][1] == symbol and self.state[r][2] == symbol:
            return f"{symbol} wins"
        if self.state[0][c] == symbol and self.state[1][c] == symbol and self.state[2][c] == symbol:
            return f"{symbol} wins"
        # main diagonal (top-left to bottom-right)
        if r == c and self.state[0][0] == symbol and self.state[1][1] == symbol and self.state[2][2] == symbol:
            return f"{symbol} wins"
        # anti-diagonal (top-right to bottom-left)
        if r + c == 2 and self.state[0][2] == symbol and self.state[1][1] == symbol and self.state[2][0] == symbol:
            return f"{symbol} wins"

        # No win: the board is full once 9 moves have been played.
        if self.turn == 9:
            return "game ended in a draw"

        return None

def rand_player(board):
    moves = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board.state[r][c] == "-"
    ]
    dr, dc = random.choice(moves)
    return board.move(dr, dc)
    
if __name__=='__main__':
    x_wins, o_wins, draws = 0, 0, 0
    for i in range(1000):
        board = Board()
        while board.status is None:
            rand_player(board)
        if "X" in board.status:
            x_wins += 1
        elif "O" in board.status:
            o_wins += 1
        else:
            draws += 1
    print(f"X: {x_wins} | O: {o_wins} | draws: {draws}")

# FROM INITIAL STATS, player X (first one to move) ends up winning
# around 580-600 of the thousand games, player O wins ~ 260-290 of the games
# and around 120-140 end in a draw