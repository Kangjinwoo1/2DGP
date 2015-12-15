from pico2d import *
import score_state

import game_framework

from sidewalk import Sidewalk
from boy import Boy # import Boy class from boy.py
from car import RedCar, Truck, GreenCar, BlueCar, BrownCar, GrayCar     #YellowCar
from road import Road

name = "main_state"
score = 0
bombman = None
red_cars = None
trucks = None
crossyroad = None
sidewalk = None

def create_world():
    global bombman, crossyroad, red_cars, trucks, blue_cars, green_cars, gray_cars, brown_cars, sidewalk       #yellow_cars
    bombman = Boy()

    brown_cars = [BrownCar() for i in range(10)]
    for i in range(10):
        if i <= 4:
            brown_cars[i].x = i * (-400) + 400
            brown_cars[i].y = 300 + 55
            brown_cars[i].distance_x = brown_cars[i].x
            brown_cars[i].distance_y = brown_cars[i].y
        else:
            brown_cars[i].x = (i - 5) * (-400) + 400
            brown_cars[i].y = 900 + 55
            brown_cars[i].distance_x = brown_cars[i].x
            brown_cars[i].distance_y = brown_cars[i].y

    gray_cars = [GrayCar() for i in range(10)]
    for i in range(10):
        if i <= 4:
            gray_cars[i].x = i * (-400) + 400
            gray_cars[i].y = 100 + 52
            gray_cars[i].distance_x = gray_cars[i].x
            gray_cars[i].distance_y = gray_cars[i].y
        else:
            gray_cars[i].x = (i - 5) * (-400) + 400
            gray_cars[i].y = 700 + 55
            gray_cars[i].distance_x = gray_cars[i].x
            gray_cars[i].distance_y = gray_cars[i].y

    trucks = [Truck() for i in range(10)]
    for i in range(10):
        if i <= 4:
            trucks[i].x = i * (-400) + 400
            trucks[i].y = 0 + 60
            trucks[i].distance_x = trucks[i].x
            trucks[i].distance_y = trucks[i].y
        else:
            trucks[i].x = (i - 5) * (-400) + 400
            trucks[i].y = 600 + 60
            trucks[i].distance_x = trucks[i].x
            trucks[i].distance_y = trucks[i].y

    green_cars = [GreenCar() for i in range(10)]
    for i in range(10):
        if i <= 4:
            green_cars[i].x = i * 400 + 400
            green_cars[i].y = 200 + 55
            green_cars[i].distance_x = green_cars[i].x
            green_cars[i].distance_y = green_cars[i].y
        else:
            green_cars[i].x = (i - 5) * 400 + 400
            green_cars[i].y = 800 + 55
            green_cars[i].distance_x = green_cars[i].x
            green_cars[i].distance_y = green_cars[i].y

    blue_cars = [BlueCar() for i in range(10)]
    for i in range(10):
        if i <= 4:
            blue_cars[i].x = i * 400 + 400
            blue_cars[i].y = 400 + 55
            blue_cars[i].distance_x = blue_cars[i].x
            blue_cars[i].distance_y = blue_cars[i].y
        else:
            blue_cars[i].x = (i - 5) * 400 + 400
            blue_cars[i].y = 1000 + 55
            blue_cars[i].distance_x = blue_cars[i].x
            blue_cars[i].distance_y = blue_cars[i].y

    red_cars = [RedCar() for i in range(10)]
    for i in range(10):
        if i <= 4:
            red_cars[i].x = i * 400 + 400
            red_cars[i].y = 500 + 55
            red_cars[i].distance_x = red_cars[i].x
            red_cars[i].distance_y = red_cars[i].y
        else:
            red_cars[i].x = (i - 5) * 400 + 400
            red_cars[i].y = 1100 + 55
            red_cars[i].distance_x = red_cars[i].x
            red_cars[i].distance_y = red_cars[i].y

    #yellow_cars = [YellowCar() for i in range(1)]

    red_cars = red_cars + trucks + blue_cars + green_cars + gray_cars + brown_cars       #yellow_cars
    crossyroad = Road()
    sidewalk = [Sidewalk() for i in range(3)]


def destroy_world():
    global bombman, red_cars, crossyroad, sidewalk

    del(bombman)
    del(red_cars)
    del(crossyroad)
    del(sidewalk)


def enter():
    open_canvas()
    hide_cursor()
    game_framework.reset_time()
    create_world()



def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                bombman.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def include(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > left_b - 40 and right_a < right_b + 40 and top_a < top_b + 20 and bottom_a > bottom_b - 20:
        return True
    return False


def update(frame_time):
    global location
    location = 0

    print("%f" % crossyroad.game_speed)

    crossyroad.update(frame_time)
    bombman.update(frame_time)

    #if bombman.include == 1:
     #   for car in red_cars:
      #      if collide(bombman, car):

    for side in sidewalk:
        side.update(frame_time)

    for car in red_cars:
        car.update(frame_time)

    for side in sidewalk:
        if include(bombman, side):
            location = 1
            print("include")

    for car in red_cars:
        if collide(bombman, car) and location == 0:
            #print("collide")
            bombman.eat(car)
            destroy_world()
            game_framework.run(score_state)


def draw(frame_time):
    clear_canvas()
    crossyroad.draw()
    for car in red_cars:
        car.draw()

    crossyroad.draw_bb()

    #for car in red_cars:
    #    car.draw_bb()
    for side in sidewalk:
        side.draw()
    #for side in sidewalk:
    #    side.draw_bb()

    #bombman.draw_bb()
    bombman.draw()
    debug_print('Score = %d' % crossyroad.score, 5, 15)

    update_canvas()





