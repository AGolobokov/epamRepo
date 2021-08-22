"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Check that anybody winner.
    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!"
    :param board:
    :return:
    """
    x_winner = ["x", "x", "x"]
    o_winner = ["o", "o", "o"]
    column_1, column_2, column_3 = [], [], []
    diag_1, diag_2 = [], []
    empty_flag = False

    for ind, line in enumerate(board):
        column_1.append(line[0])
        column_2.append(line[1])
        column_3.append(line[2])
        diag_1.append(line[ind])
        diag_2.append(line[-1 - ind])
        if "-" in line:
            empty_flag = True

    if x_winner in (
        column_1,
        column_2,
        column_3,
        diag_1,
        diag_2,
        board[0],
        board[1],
        board[2],
    ):
        return "x wins!"
    elif o_winner in (
        column_1,
        column_2,
        column_3,
        diag_1,
        diag_2,
        board[0],
        board[1],
        board[2],
    ):
        return "o wins!"
    elif empty_flag:
        return "unfinished!"
    else:
        return "draw!"
