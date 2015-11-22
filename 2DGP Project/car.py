import random

from pico2d import *

class RedCar:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RED_CAR_SPEED_KMPH = 60.0                    # Km / Hour
    RED_CAR_SPEED_MPM = (RED_CAR_SPEED_KMPH * 1000.0 / 60.0)
    RED_CAR_SPEED_MPS = (RED_CAR_SPEED_MPM / 60.0)
    RED_CAR_SPEED_PPS = (RED_CAR_SPEED_MPS * PIXEL_PER_METER)

    image = None;

    def __init__(self):
        self.x, self.y = 1000, random.randint(0, 5) * 100 + 80
        self.game_speed = 0.1
        self.car_speed = random.randint(1, 10)
        if RedCar.image == None:
            RedCar.image = load_image('redcar.png')

    def update(self, frame_time):
        distance = RedCar.RED_CAR_SPEED_PPS * frame_time
        self.x -= distance * (self.game_speed * self.car_speed)
        self.y -= self.game_speed
        if self.y <= -20:
            self.x = 1000
            self.y = random.randint(0, 5) * 100 + 80


    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


class Truck(RedCar):
    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = random.randint(200,300)
        if Truck.image == None:
            Truck.image = load_image('ball41x41.png')
        self.parent = None


    def stop(self):
        self.fall_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            self.y -= frame_time * self.fall_speed

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def set_parent(self, brick):
        self.parent = brick
        self.rx = self.x - brick.x
        self.ry = self.y - brick.y
        pass