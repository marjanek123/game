import numpy as np
import pygame
import sys
import random
import json
is_game_run= True
ROW_COUNT = 16
pygame.init()
COLUMN_COUNT = 16
SQUARESIZE=32
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('music.mp3')
tomek=False

pygame.mixer.music.play()

_currently_playing_song = None
_songs=['LOOPCRYS.mp3','COMBAT02.mp3']
terrain=[pygame.image.load('grass.GIF'),pygame.image.load('grass2.GIF')]
###objects in current map
object=[
    {
        "lake":[[4,6],]
    },
]


###obj in src
full_object=[
    {
        "lake":{
            "img":"lake.PNG",
            "terrain":[[1,1,1],[1,1,1]]
        }
    },
    {
        "wiotrok":{
            "img":"wiotrok.gif",
            "terrain":[[0,0,0],[0,0,2]]
        }
    }
]
#class adventure_map():
class background_map:
    ROW_COUNT = 16

    COLUMN_COUNT = 16
    def __init__(self,COLUMN_COUNT,ROW_COUNT):
        self.board=(COLUMN_COUNT,ROW_COUNT)
        self.COLUMN_COUNT=COLUMN_COUNT
        self.ROW_COUNT=ROW_COUNT
    def create_board(self):
        return print(np.zeros(self.board))


    def print_board(self):
        np.flip(self.board, 0)

    def regenerate_map(self):
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                screen.blit(random.choice(terrain), (int(c * SQUARESIZE), int(r * SQUARESIZE)))
class adventure_map:
#    sorce = "obj.json"
    ROW_COUNT = 16
#    mapke = "maplyobj.json"
    COLUMN_COUNT = 16
    def __init__(self,COLUMN_COUNT,ROW_COUNT,):
        self.board=COLUMN_COUNT*ROW_COUNT



    def create_obj_board(self):
        mapk=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],])

    def do_map(self):
        global object
        global full_object
        for key in object:
            pass




    def adventure_map(self):
        with open("maplyobj.json") as f:
            pass
        return np.zeros((ROW_COUNT,COLUMN_COUNT))



maply=background_map(16,16)


maply.create_board()
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT) * SQUARESIZE
size = (width+100, height+100)
screen = pygame.display.set_mode(size)
box= pygame.Rect(34,34,5,5,)
maply.regenerate_map()
#screen.blit(crack,(0,0))
pygame.init()
maply.print_board()
clock= pygame.time.Clock()
adventure_map(16,16).create_obj_board()


while True:
    # obsługa zdarzeń generowanych przez gracza
    clock.tick(60)
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == SONG_END:
            def play_a_different_song():
                global _currently_playing_song, _songs
                next_song = random.choice(_songs)
                while next_song == _currently_playing_song:
                    next_song = random.choice(_songs)
                _currently_playing_song = next_song
                pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()



    #    screen.fill((0,255,0))
    maply.print_board()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        box.x +=1


    if pressed[pygame.K_w]:
        box.y+=-1

    if pressed[pygame.K_a]:
        box.x += -1

    if pressed[pygame.K_s]:
        box.y += 1

#    pygame.mask.from_surface(screen,tomasz)
#    screen.fill((0,0,0))
    pygame.display.flip()
    pygame.draw.rect(screen,(233,230,230),box)

