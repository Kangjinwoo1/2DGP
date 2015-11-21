import random

from pico2d import *

class Road:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 400, 600
        self.game_speed = 0.1
        if Road.image == None:
            Road.image = load_image('road.png')

    def update(self, frame_time):
        self.y -= self.game_speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 0,0,799,50

    #def __del__(self):
     #   del self.image
        #del self.bgm

