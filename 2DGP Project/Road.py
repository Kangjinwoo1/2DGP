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
        self.screen_width = 800
        self.screen_height = 600
        self.screen_width_half = 400
        self.screen_height_half = 300
        self.x, self.y1, self.y2 = self.screen_width_half, self.screen_height_half, self.screen_height_half + self.screen_height
        self.game_speed = 0.2
        if Road.image == None:
            Road.image = load_image('road.png')

    def update(self, frame_time):
        self.y1 -= self.game_speed
        self.y2 -= self.game_speed
        if self.y1 <= -self.screen_height_half:
            self.y1 = self.screen_height_half + self.screen_height
        if self.y2 <= -self.screen_height_half:
            self.y2 = self.screen_height_half + self.screen_height

    def draw(self):
        self.image.clip_draw(0, 0, self.screen_width, self.screen_height, self.x, self.y1)
        self.image.clip_draw(0, self.screen_height, self.screen_width, self.screen_height, self.x, self.y2)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    #def get_bb(self):
        #return 0,0,799,50

    #def __del__(self):
     #   del self.image
        #del self.bgm

