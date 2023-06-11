"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xs = 0
    os = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                xs += 1
            if board[i][j] == "O":
                os += 1

    if xs == os:
        return "X"
    return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    sim_board = copy.deepcopy(board)
    if action is None or board[action[0]][action[1]] is not None:
        raise RuntimeError
    sim_board[action[0]][action[1]] = player(board)
    return sim_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == "X":
        b = False
    else:
        b = True

    return recursive_minimax(board, None, b, True)


def recursive_minimax(board, moved, minimize, top):
    if isinstance(moved, tuple):
        board = result(board, moved)

    if terminal(board):
        return utility(board)

    if minimize:
        worst = 1
        best = 1

        for move in actions(board):
            move_utility = recursive_minimax(board, move, not minimize, False)
            if top:
                print(move_utility)
            if best > move_utility and top:
                best_move = move
            best = max(best, move_utility)
            worst = min(worst, move_utility)
        if top:
            return best_move
        return worst

    else:
        worst = -1
        best = -1
        for move in actions(board):
            move_utility = recursive_minimax(board, move, not minimize, False)


            worst = max(worst, move_utility)
            if best < move_utility and top:
                best_move = move
            best = max(best, move_utility)
        if top:
            return best_move
        return worst
