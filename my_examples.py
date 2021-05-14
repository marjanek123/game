import numpy as np
import pygame
import sys
import random

is_game_run = True
ROW_COUNT = 16

COLUMN_COUNT = 16
SQUARESIZE = 32

terrain = [pygame.image.load('grass.GIF'), pygame.image.load('grass2.GIF')]


class adventure_map:
    def __init__(self):
        self.terrain=[]
        self.obj=[]
        self.board=create_board()
        self.regenerate_map=regenerate_map()




    def create_board(self,board):
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board


    def print_board(self,board):
        np.flip(board, 0)


    def regenerate_map():
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                print(r)
                screen.blit(random.choice(terrain), (int(c * SQUARESIZE), int(r * SQUARESIZE)))


    
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT) * SQUARESIZE
size = (width + 100, height + 100)
screen = pygame.display.set_mode(size)
    # box= pygame.Rect(34,34,5,5,)
    # regenerate_map(print_board(board))

pygame.init()

clock = pygame.time.Clock()

while True:
    # obsługa zdarzeń generowanych przez gracza

    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    adventure_map.regenerate_map()





#    screen.fill((0,0,0))
    pygame.display.flip()
#    pygame.draw.rect(screen,(233,230,2


