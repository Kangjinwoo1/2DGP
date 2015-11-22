import random

from pico2d import *

class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    eat_sound = None

    UP_RUN, DOWN_RUN, LEFT_RUN, RIGHT_RUN = 0, 1, 2, 3
    UP_STAND, DOWN_STAND, LEFT_STAND, RIGHT_STAND = 4, 5, 6, 7

    def __init__(self):
        self.x, self.y = 400, 180
        self.frame = random.randint(0, 11)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir_x = 0
        self.dir_y = 0
        self.game_speed = 0.1
        self.state = self.UP_STAND
        if Boy.image == None:
            Boy.image = load_image('boy_animation.png')
        # fill here

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2
        self.x += (self.dir_x * distance)
        self.y += (self.dir_y * distance) - self.game_speed

        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)

    def eat(self, ball):
        # fill here
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 99, 100, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.UP_STAND, self.DOWN_STAND, self.RIGHT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.LEFT_RUN
                self.dir_x = -1
                self.dir_y = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.UP_STAND, self.DOWN_STAND, self.LEFT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.RIGHT_RUN
                self.dir_x = 1
                self.dir_y = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.UP_STAND, self.DOWN_STAND, self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN):
                self.state = self.UP_RUN
                self.dir_x = 0
                self.dir_y= 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.UP_STAND, self.DOWN_STAND, self.RIGHT_RUN, self.LEFT_RUN, self.UP_RUN):
                self.state = self.DOWN_RUN
                self.dir_x = 0
                self.dir_y = -1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir_x = 0
                self.dir_y = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir_x = 0
                self.dir_y = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.UP_STAND
                self.dir_x = 0
                self.dir_y = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.DOWN_STAND
                self.dir_x = 0
                self.dir_y = 0


