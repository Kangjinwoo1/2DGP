import random
from pico2d import *

game_speed = 0.3
difficulty = 600

class Sidewalk:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None
    #image2 = None

    def __init__(self):
        self.x, self.y = 400, 100 + 50
        self.obstacle_x = -200
        self.game_speed = game_speed
        self.time_count = 0
        if Sidewalk.image == None:
            Sidewalk.image = load_image('sidewalk.png')
        #if Sidewalk.image2 == None:
        #    Sidewalk.image2 = load_image("yellowcar.png")

    def update(self, frame_time):
        self.y -= self.game_speed
        self.time_count += self.game_speed
        if self.time_count >= difficulty:
            self.time_count = 0
            if self.game_speed < 0.7:
                self.game_speed += 0.01
        if self.y <= -50:
            self.y = random.randint(7, 12) * 100 + 50
            #self.obstacle_x = 100 * random.randint(1, 8)

    def draw(self):
        self.image.draw(self.x, self.y)
        #self.image2.draw(self.obstacle_x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        #draw_rectangle(*self.obstacle_bb())

    def get_bb(self):
        return self.x - 400, self.y - 55, self.x + 400, self.y + 55

    #def obstacle_bb(self):
    #    return self.obstacle_x - 90, self.y - 29, self.obstacle_x + 83, self.y + 30


