import pygame as p


import chess_engine

HEIGHT = WIDTH = 400
DIMENTION = 8
SQUARE_SIZE = HEIGHT//DIMENTION
MAX_FPS = 15
Images = {}

def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        Images[piece] = p.transform.scale(p.image.load('chess_pieces/'+piece+'.png'), (SQUARE_SIZE,SQUARE_SIZE))

def main():
    p.init()
    screen  = p.display.set_mode((WIDTH, HEIGHT))

    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    game_state = chess_engine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, game_state):
    draw_board(screen)

    draw_pieces(screen, game_state.board)

def draw_board(screen):
    colors = [(200, 111, 111), p.Color('gray')]
    for r in range(DIMENTION):
        for c in range(DIMENTION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
def draw_pieces(screen, board):
    for r in range(DIMENTION):
        for c in range(DIMENTION):
            piece = board[r][c]
            if piece !='--':
                screen.blit(Images[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))




main()