import random
from game import Board, rand_player
import math

class Node:
    def __init__(self, move, parent, board):
        self.move = move
        self.visits = 0
        self.wins = 0
        self.losses = 0
        self.children = set()
        self.untried_moves = set(
        (r, c)
        for r in range(3)
        for c in range(3)
        if board.state[r][c] == "-"
    )
        self.parent = parent
        self.board = board

def best_child_by_UCT(root, exploration_constant=math.sqrt(2)):
    max_score, max_child = float("-inf"), None
    for c in root.children:
        uct_score = c.wins / c.visits + exploration_constant * math.sqrt(math.log(root.visits) / c.visits)
        if uct_score > max_score: max_score, max_child = uct_score, c
    return max_child

def winner(board):
    # Normalize the rollout's status string into "X", "O", or "draw".
    if "X" in board.status:
        return "X"
    if "O" in board.status:
        return "O"
    return "draw"


def reward(node, winner):
    # Credit for the player who moved INTO this node, given the rollout winner.
    if winner == "draw":
        return 0.5
    r, c = node.move
    mover = node.board.state[r][c]  # the symbol this node's move placed
    return 1 if mover == winner else 0


def mtcs(root, n_iters):
    for _ in range(n_iters):
        cur = root
        # game is not complete and we know the node is fully expanded
        while not cur.untried_moves and cur.board.status is None:
            cur = best_child_by_UCT(cur)
                
        # expansion
        if cur.board.status is None:
                prev = cur
                r, c = cur.untried_moves.pop()
                newboard = prev.board.copy()
                newboard.move(r, c)
                cur = Node((r, c), prev, newboard)
                prev.children.add(cur)

        # rollout
        b = cur.board.copy()
        while b.status is None:
            rand_player(b)

        res = winner(b)
        while cur:
            cur.visits += 1
            if cur.move is not None:
                wins = reward(cur, res)
                if wins == 0: cur.losses += 1
                cur.wins += wins
            cur = cur.parent


if __name__ == '__main__':
    root = Node(None, None, Board())
    mtcs(root, 1000000)

    # Show what MCTS learned about each first move, best (most-visited) first.
    print(f"root visits: {root.visits}\n")
    print(f"{'move':<8}{'visits':>8}{'wins':>8}{'win%':>8}{'loss%':>8}")
    for child in sorted(root.children, key=lambda c: c.visits, reverse=True):
        win_rate = child.wins / child.visits * 100
        loss_rate = child.losses / child.visits * 100
        
        print(f"{str(child.move):<8}{child.visits:>8}{child.wins:>8.1f}{win_rate:>8.2f}{loss_rate:>8.2f}")

    best = max(root.children, key=lambda c: c.visits)
    print(f"\nbest move: {best.move}")