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

    player_x = 0
    player_o = 0

    for row in board:
        for i in row:
            if i == X:
                player_x += 1
            elif i == O:
                player_o += 1
    
    if player_x <= player_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions= set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_actions.add((i,j))
    
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i,j = action

    if i not in range(3) or j not in range(3):
        raise Exception("Invalid action: out of bounds")

    if board[i][j] != EMPTY:
        raise Exception("It is not valid!")
    
    board2 = copy.deepcopy(board)

    next_player = player(board)

    board2[i][j]= next_player

    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i == [O,O,O]:
            return O
        elif i== [X,X,X]:
            return X
    
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for j in row:
            if j == EMPTY:
                return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result= winner(board)

    if result == X:
        return 1
    elif result== O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        best = -2
        move = None
        for action in actions(board):
            new = result(board, action)
            score = min_value(new)
            if score > best:
                best = score
                move = action
        return move
    else:
        best = 2
        move = None
        for action in actions(board):
            new = result(board, action)
            score = max_value(new)
            if score < best:
                best = score
                move = action
        return move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v