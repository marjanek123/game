import os
from kaa.sprites import Sprite, split_spritesheet
from kaa.geometry import Vector

class AssetsController:

    def __init__(self):
        self.dirt_1 = Sprite(os.path.join('assets', 'bgmap', 'dirt5.png'))
        self.dirt_2 = Sprite(os.path.join('assets', 'bgmap', 'dirt2.png'))
        self.dirt_3 = Sprite(os.path.join('assets', 'bgmap', 'dirt3.png'))
        self.dirt_1 = Sprite(os.path.join('assets', 'bgmap', 'dirt4.png'))
        self.dirt_2 = Sprite(os.path.join('assets', 'bgmap', 'dirt6.png'))
        self.dirt_3 = Sprite(os.path.join('assets', 'bgmap', 'dirt7.png'))
        self.dirt_2 = Sprite(os.path.join('assets', 'bgmap', 'dirt8.png'))
        