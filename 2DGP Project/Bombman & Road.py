import sys
sys.path.append('../LabsAll/Labs')

import random

from pico2d import *

running = None


class Road:

    def __init__(self):
        self.image = load_image('road1.png')

    def draw(self):
        global road_y
        self.image.draw(400, 540 + road_y)

class Truck:

    def __init__(self):
        self.image = load_image('truck.png')

    def draw(self):
        global road_y
        global truck_x, truck_x2
        self.image.draw(truck_x, 321 + road_y)
        self.image.draw(-100 + truck_x2, 492 + road_y)

class Redcar:

    def __init__(self):
        self.image = load_image('redcar.png')

    def draw(self):
        global road_y
        global redcar_x
        self.image.draw(800 + redcar_x, 398 + road_y)
        self.image.draw(1000 + redcar_x2, 564 + road_y)

class Bombman:

    image = None

    def update(self):
        global walk_state
        if walk_state == 1:
            self.frame = (self.frame + 1) % 3 + 4
            if self.frame == 6:
                walk_state = 0
                self.frame = 3
        elif walk_state == 2:
            self.frame = (self.frame + 1) % 3 + 1
            if self.frame == 3:
                walk_state = 0
                self.frame = 0
        elif walk_state == 3:
            self.frame = (self.frame + 1) % 3 + 7
            if self.frame == 9:
                walk_state = 0
                self.frame = 6
        elif walk_state == 4:
            self.frame = (self.frame + 1) % 3 + 10
            if self.frame == 12:
                walk_state = 0
                self.frame = 9

    def __init__(self):
        self.walk_state = 0
        self.frame = 3
        if Bombman.image == None:
            Bombman.image = load_image('bombman_animation.png')

    def draw(self):
        global bombman_y
        global x
        global y
        self.image.clip_draw(self.frame * 100, 0, 100, 100, x + 400, y + 210 + bombman_y)


def handle_events():
    global running
    global x
    global y
    global walk_state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                y = y + 20
                walk_state = 1
            elif event.key == SDLK_DOWN:
                y = y - 20
                walk_state = 2
            elif event.key == SDLK_LEFT:
                x = x - 20
                walk_state = 3
            elif event.key == SDLK_RIGHT:
                x = x + 20
                walk_state = 4
            elif event.key == SDLK_ESCAPE:
                running = False


def main():

    open_canvas()

    bombman = Bombman()
    road = Road()
    truck = Truck()
    redcar = Redcar()

    global running
    running = True
    global x, y, road_y, bombman_y, car_y, walk_state, truck_x, truck_x2, redcar_x, redcar_x2
    x, y, road_y, bombman_y, car_y, walk_state, truck_x, truck_x2, redcar_x, redcar_x2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    while running:
        handle_events()
        bombman_y -= 3
        road_y -= 3
        truck_x += 10
        truck_x2 += 5
        redcar_x -= 8
        redcar_x2 -= 12
        bombman.update()

        clear_canvas()

        road.draw()
        truck.draw()
        redcar.draw()
        bombman.draw()

        update_canvas()

        delay(0.1)

    close_canvas()


if __name__ == '__main__':
    main()
