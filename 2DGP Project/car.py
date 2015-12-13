import random

from pico2d import *

class RedCar:
    PIXEL_PER_METER = (10.0 / 0.3)              # 10 pixel 30 cm
    RED_CAR_SPEED_KMPH = 60.0                   # Km / Hour
    RED_CAR_SPEED_MPM = (RED_CAR_SPEED_KMPH * 1000.0 / 60.0)
    RED_CAR_SPEED_MPS = (RED_CAR_SPEED_MPM / 60.0)
    RED_CAR_SPEED_PPS = (RED_CAR_SPEED_MPS * PIXEL_PER_METER)
    image = None;

    def __init__(self):
        self.x, self.y = 1000, 500 + 55
        self.distance_x = self.x
        self.distance_y = self.y
        self.count = 600
        self.time_count = 0
        self.game_speed = 0.3
        self.car_speed = 0.175
        if RedCar.image == None:
            RedCar.image = load_image('redcar.png')

    def update(self, frame_time):
        distance = RedCar.RED_CAR_SPEED_PPS * frame_time
        self.x -= distance * self.car_speed
        self.y -= self.game_speed
        self.count -= self.game_speed
        self.time_count += self.game_speed
        if self.time_count >= 600:
            self.game_speed += 0.01
            self.time_count = 0
        if self.x <= -200:
            self.x += 2000
        if self.count <= 0:
            self.count = 600
        if self.count == 600:
            self.y -= self.y - self.distance_y

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 80, self.y - 25, self.x + 75, self.y + 25

class Truck(RedCar):
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    TRUCK_SPEED_KMPH = 60.0                    # Km / Hour
    TRUCK_SPEED_MPM = (TRUCK_SPEED_KMPH * 1000.0 / 60.0)
    TRUCK_SPEED_MPS = (TRUCK_SPEED_MPM / 60.0)
    TRUCK_SPEED_PPS = (TRUCK_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        self.x, self.y = -200, 0 + 60
        self.distance_x = self.x
        self.distance_y = self.y
        self.count = 600
        self.time_count = 0
        self.game_speed = 0.3
        self.car_speed = 0.3
        if Truck.image == None:
            Truck.image = load_image('truck.png')
        self.parent = None

    #def stop(self):
     #   self.car_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            distance = Truck.TRUCK_SPEED_PPS * frame_time
            self.x += distance * self.car_speed
            self.y -= self.game_speed
            self.count -= self.game_speed
            self.time_count += self.game_speed
            if self.time_count >= 600:
                self.game_speed += 0.01
                self.time_count = 0
            if self.x >= 1000:
                self.x -= 2000
            if self.count <= 0:
                self.count = 600
            if self.count == 600:
                self.y -= self.y - self.distance_y

    def get_bb(self):
        return self.x - 115, self.y - 40, self.x + 115, self.y + 27

    def set_parent(self, brick):
        self.parent = brick
        self.rx = self.x - brick.x
        self.ry = self.y - brick.y
        pass


class BrownCar(RedCar):
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    BROWN_CAR_SPEED_KMPH = 60.0                    # Km / Hour
    BROWN_CAR_SPEED_MPM = (BROWN_CAR_SPEED_KMPH * 1000.0 / 60.0)
    BROWN_CAR_SPEED_MPS = (BROWN_CAR_SPEED_MPM / 60.0)
    BROWN_CAR_SPEED_PPS = (BROWN_CAR_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        self.x = -200
        self.y = 300 + 55
        self.distance_x = self.x
        self.distance_y = self.y
        self.count = 600
        self.time_count = 0
        self.game_speed = 0.3
        self.car_speed = 0.225
        if BrownCar.image == None:
            BrownCar.image = load_image('browncar.png')
        self.parent = None

    #def stop(self):
     #   self.car_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            distance = BrownCar.BROWN_CAR_SPEED_PPS * frame_time
            self.x += distance * self.car_speed
            self.y -= self.game_speed
            self.count -= self.game_speed
            self.time_count += self.game_speed
            if self.time_count >= 600:
                self.game_speed += 0.01
                self.time_count = 0
            if self.x >= 1000:
                self.x -= 2000
            if self.count <= 0:
                self.count = 600
            if self.count == 600:
                self.y -= self.y - self.distance_y

    def get_bb(self):
        return self.x - 90, self.y - 33, self.x + 90, self.y + 27

    def set_parent(self, brick):
        self.parent = brick
        self.rx = self.x - brick.x
        self.ry = self.y - brick.y
        pass


class GrayCar(RedCar):
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    GRAY_CAR_SPEED_KMPH = 60.0                    # Km / Hour
    GRAY_CAR_SPEED_MPM = (GRAY_CAR_SPEED_KMPH * 1000.0 / 60.0)
    GRAY_CAR_SPEED_MPS = (GRAY_CAR_SPEED_MPM / 60.0)
    GRAY_CAR_SPEED_PPS = (GRAY_CAR_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        self.x, self.y = -200, 100 + 52
        self.distance_x = self.x
        self.distance_y = self.y
        self.count = 600
        self.time_count = 0
        self.game_speed = 0.3
        self.car_speed = 0.165
        if GrayCar.image == None:
            GrayCar.image = load_image('graycar.png')
        self.parent = None

    #def stop(self):
     #   self.car_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            distance = GrayCar.GRAY_CAR_SPEED_PPS * frame_time
            self.x += distance * self.car_speed
            self.y -= self.game_speed
            self.count -= self.game_speed
            self.time_count += self.game_speed
            if self.time_count >= 600:
                self.game_speed += 0.01
                self.time_count = 0
            if self.x >= 1000:
                self.x -= 2000
            if self.count <= 0:
                self.count = 600
            if self.count == 600:
                self.y -= self.y - self.distance_y

    def get_bb(self):
        return self.x - 77, self.y - 27, self.x + 77, self.y + 27

    def set_parent(self, brick):
        self.parent = brick
        self.rx = self.x - brick.x
        self.ry = self.y - brick.y
        pass


class BlueCar(RedCar):
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    BLUE_CAR_SPEED_KMPH = 60.0                    # Km / Hour
    BLUE_CAR_SPEED_MPM = (BLUE_CAR_SPEED_KMPH * 1000.0 / 60.0)
    BLUE_CAR_SPEED_MPS = (BLUE_CAR_SPEED_MPM / 60.0)
    BLUE_CAR_SPEED_PPS = (BLUE_CAR_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        self.x, self.y = 1000, 400 + 55
        self.distance_x = self.x
        self.distance_y = self.y
        self.count = 600
        self.time_count = 0
        self.game_speed = 0.3
        self.car_speed = 0.225
        if BlueCar.image == None:
            BlueCar.image = load_image('bluecar.png')
        self.parent = None

    #def stop(self):
     #   self.car_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            distance = BlueCar.BLUE_CAR_SPEED_PPS * frame_time
            self.x -= distance * self.car_speed
            self.y -= self.game_speed
            self.count -= self.game_speed
            self.time_count += self.game_speed
            if self.time_count >= 600:
                self.game_speed += 0.01
                self.time_count = 0
            if self.x <= -200:
                self.x += 2000
            if self.count <= 0:
                self.count = 600
            if self.count == 600:
                self.y -= self.y - self.distance_y

    def get_bb(self):
        return self.x - 73, self.y - 25, self.x + 70, self.y + 20


class GreenCar(RedCar):
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    GREEN_CAR_SPEED_KMPH = 60.0                    # Km / Hour
    GREEN_CAR_SPEED_MPM = (GREEN_CAR_SPEED_KMPH * 1000.0 / 60.0)
    GREEN_CAR_SPEED_MPS = (GREEN_CAR_SPEED_MPM / 60.0)
    GREEN_CAR_SPEED_PPS = (GREEN_CAR_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        self.x, self.y = 1000, 200 + 55
        self.distance_x = self.x
        self.distance_y = self.y
        self.count = 600
        self.time_count = 0
        self.game_speed = 0.3
        self.car_speed = 0.25
        if GreenCar.image == None:
            GreenCar.image = load_image('greencar.png')
        self.parent = None

    #def stop(self):
     #   self.car_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            distance = GreenCar.GREEN_CAR_SPEED_PPS * frame_time
            self.x -= distance * self.car_speed
            self.y -= self.game_speed
            self.count -= self.game_speed
            self.time_count += self.game_speed
            if self.time_count >= 600:
                self.game_speed += 0.01
                self.time_count = 0
            if self.x <= -200:
                self.x += 2000
            if self.count <= 0:
                self.count = 600
            if self.count == 600:
                self.y -= self.y - self.distance_y

    def get_bb(self):
        return self.x - 90, self.y - 32, self.x + 85, self.y + 30

########################################################################
class YellowCar(RedCar):
    PIXEL_PER_METER = (10.0 / 0.3)                   # 10 pixel 30 cm
    YELLOW_CAR_SPEED_KMPH = 100.0                    # Km / Hour
    YELLOW_CAR_SPEED_MPM = (YELLOW_CAR_SPEED_KMPH * 1000.0 / 60.0)
    YELLOW_CAR_SPEED_MPS = (YELLOW_CAR_SPEED_MPM / 60.0)
    YELLOW_CAR_SPEED_PPS = (YELLOW_CAR_SPEED_MPS * PIXEL_PER_METER)
    image = None

    def __init__(self):
        self.x, self.y = 1000, random.randint(2, 18) * 100 + 50
        self.count = 100
        self.game_speed = 0.3
        self.car_speed = 0.9
        if YellowCar.image == None:
            YellowCar.image = load_image('yellowcar.png')
        self.parent = None

    #def stop(self):
    #   self.car_speed = 0

    def update(self, frame_time):
        if self.parent:
            self.x = self.parent.x + self.rx
            self.y = self.parent.y + self.ry
        else:
            distance = YellowCar.YELLOW_CAR_SPEED_PPS * frame_time
            self.x -= distance * self.car_speed
            self.y -= self.game_speed
            self.count -= self.game_speed
        if self.count <= 0:
            self.count = 100
        if self.x <= -200:
            if self.count == 100:
                self.x = 1000
                self.y = random.randint(2, 18) * 100 + 50
                self.car_speed = 2

    def get_bb(self):
        return self.x - 90, self.y - 29, self.x + 83, self.y + 30
