import random

from pico2d import *

game_speed = 0.3
difficulty = 600

class Road:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None
    bgm = None

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen_width_half = 400
        self.screen_height_half = 300
        self.x, self.y1, self.y2 = self.screen_width_half, self.screen_height_half, self.screen_height_half + self.screen_height
        self.time_count = 0
        self.time = 0
        self.level = 0
        self.game_speed = game_speed
        self.score = 0
        if Road.bgm == None:
            self.bgm = load_music('bgm.ogg')
            self.bgm.set_volume(64)
            self.bgm.repeat_play()
        if Road.image == None:
            Road.image = load_image('road.png')

    def update(self, frame_time):
        self.y1 -= self.game_speed
        self.y2 -= self.game_speed
        self.time += frame_time
        self.time_count += self.game_speed
        self.score += 0.1 * self.game_speed
        if self.time_count >= difficulty:
            self.time_count = 0
            if self.game_speed < 0.7:
                self.game_speed += 0.01
        if self.y1 <= -self.screen_height_half:
            self.y1 = self.screen_height_half + self.screen_height
        if self.y2 <= -self.screen_height_half:
            self.y2 = self.screen_height_half + self.screen_height
        self.level = self.game_speed * 10 - 3

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

