import random
from pico2d import *

class Obstacle:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 400, 100 + 50
        self.game_speed = 0.3
        if Obstacle.image == None:
            Obstacle.image = load_image("yellowcar.png")

    def update(self, frame_time):
        self.y -= self.game_speed
        if self.y <= -50:
            self.y = random.randint(7, 12) * 100 + 50
            self.x = 100 * random.randint(1, 8)

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 400, self.y - 55, self.x + 400, self.y + 55
