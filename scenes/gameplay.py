from kaa.engine import Scene
from map.genereate_map import BGMap
from map.genereate_objects import OBMap
import numpy as np
import settings
from kaa.input import Keycode


class GameplayScene(Scene):

    def __init__(self):
        super().__init__()
        self.bg = BGMap
        self.ob = OBMap
        self.mapk = np.zeros((settings.MAP_X,settings.MAP_Y), dtype=int)

    def update(self, dt):
        BGMap.openerbg(self)
        OBMap.createob(self)

        for event in self.input.events():
            if event.keyboard_key:  # check if the event is a keyboard key related event
                if event.keyboard_key.is_key_down:  # check if the event is "key down event"
                    # check which key was pressed down:
                    if event.keyboard_key.key == Keycode.q:
                        self.engine.quit()