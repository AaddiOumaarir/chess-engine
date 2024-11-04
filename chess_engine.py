import numpy as np
import pygame as p
class GameState:
    # '--' represent empty square
    def __init__(self):
        self.board = np.array([['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                               ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                               ['--', '--', '--', '--', '--', '--', '--', '--'],
                               ['--', '--', '--', '--', '--', '--', '--', '--'],
                               ['--', '--', '--', '--', '--', '--', '--', '--'],
                               ['--', '--', '--', '--', '--', '--', '--', '--'],
                               ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                               ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']])
        self.WhiteToMove = True
        self.moveLog = []

print(p.Color('white'))