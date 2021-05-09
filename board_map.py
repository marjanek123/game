import numpy as np
import pygame
from pygame import mixer
import sys
import random, queue
import json, random
is_game_run= True
ROW_COUNT = 24
pygame.init()
COLUMN_COUNT = 24
SQUARESIZE=32

SONG_END = pygame.USEREVENT + 1
#pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('LOOPCRYS.mp3')
pygame.mixer.music.load('LOOPELF.mp3')
tomek=False

pygame.mixer.music.play(-1)

_currently_playing_song = None
_songs=[]
terrain=[pygame.image.load('dirt7.GIF')]
###objects in current map

#pygame.image.load('dirt1.GIF'),pygame.image.load('dirt2.GIF'),pygame.image.load('dirt3.GIF'),pygame.image.load('dirt4.GIF'),pygame.image.load('dirt5.GIF'),pygame.image.load('dirt6.GIF'),pygame.image.load('dirt7.GIF'),pygame.image.load('dirt8.GIF')

###obj in src
full_object="""{
    "obj":[
    {
        "lake":[{
            "img":"lake.PNG",
            "terrain":[[1,1,1],[1,1,1]]
            ]}  
    },
    {
        "wiotrok":[{
            "img":"wiotrok.gif",
            "terrain":[[0,0,0],[0,0,2]]
        }],
    }
]
}
"""
mapk = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ])
#class adventure_map():
class background_map:
    ROW_COUNT = 2

    COLUMN_COUNT = 2
    def __init__(self,COLUMN_COUNT,ROW_COUNT):
        self.board=(COLUMN_COUNT,ROW_COUNT)
        self.COLUMN_COUNT=COLUMN_COUNT
        self.ROW_COUNT=ROW_COUNT
    def create_board(self):
        return print(np.zeros(self.COLUMN_COUNT))


    def print_board(self):
        np.flip(self.board, 0)

    def regenerate_map(self):
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                screen.blit(random.choice(terrain), (int(c * SQUARESIZE), int(r * SQUARESIZE)))
class adventure_map:
#    sorce = "obj.json"
    ROW_COUNT = 30
#    mapke = "maplyobj.json"
    COLUMN_COUNT = 30
    def __init__(self,COLUMN_COUNT,ROW_COUNT,):
        self.board=COLUMN_COUNT*ROW_COUNT



#    def create_obj_board(self):
#        mapk=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],])
#        return mapk


    def get_object(self):
        pass






    def adventure_map(self):
        izydorf=np.zeros((ROW_COUNT,COLUMN_COUNT))
        global mapk
        print( mapk)
        with open("maplypos.json") as f:
            data = json.load(f)
            for a in range(0, len(data)):
                t=data[a]["ob"]
                p=data[a]["pos"]



blue_imaget = pygame.Surface((50,50), pygame.SRCALPHA)
maply=background_map(24,24)
sprite_imag = pygame.image.load("cave.gif")
sprite_imag= pygame.transform.scale(sprite_imag, (70, 60))
blue_image = pygame.Surface((100,150), pygame.SRCALPHA)
print(background_map.create_board(COLUMN_COUNT))
pygame.Surface((30,34),pygame.SRCALPHA)
maply.create_board()
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size,pygame.SRCALPHA,32)
box= pygame.Rect(34,34,5,5,)
maply.regenerate_map()
#screen.blit(crack,(0,0))
pygame.init()
#maply.print_board()
clock= pygame.time.Clock()
blue_size = pygame.Surface((size), pygame.SRCALPHA)
adventure_map(16,16).adventure_map()
print(dir(json))
pygame.draw.rect(blue_size, (0,0,0,45),blue_size.get_rect(),600)
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
#    maply.print_board()
#    screen.blit(blue_image, (75, 17))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        box.x +=1


    if pressed[pygame.K_w]:
        box.y+=-1

    if pressed[pygame.K_a]:
        box.x += -1

    if pressed[pygame.K_s]:
        box.y += 1

    maply.regenerate_map()
    screen.blit(sprite_imag,(0,0))
    screen.blit(sprite_imag, (96, 64))
#    pygame.mask.from_surface(screen,tomasz)
#    screen.blit(blue_size, (0,0))
    pygame.display.flip()
#    pygame.draw.rect(screen,(233,230,230),box)
    pygame.display.update()

