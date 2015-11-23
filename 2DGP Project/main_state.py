from pico2d import *

import game_framework

from boy import Boy # import Boy class from boy.py
from car import RedCar, Truck, GreenCar, YellowCar, BlueCar, BrownCar, GrayCar
from road import Road



name = "main_state"

bombman = None
red_cars = None
trucks = None
crossyroad = None

def create_world():
    global bombman, crossyroad, red_cars, trucks, blue_cars, yellow_cars, green_cars, gray_cars, brown_cars

    bombman = Boy()

    brown_cars = [BrownCar() for i in range(3)]
    gray_cars = [GrayCar() for i in range(3)]
    trucks = [Truck() for i in range(2)]

    green_cars = [GreenCar() for i in range(2)]
    blue_cars = [BlueCar() for i in range(3)]
    yellow_cars = [YellowCar() for i in range(1)]
    red_cars = [RedCar() for i in range(3)]

    red_cars = red_cars + trucks + blue_cars + yellow_cars + green_cars + gray_cars + brown_cars
    crossyroad = Road()


def destroy_world():
    global bombman, red_cars, road

    del(bombman)
    del(red_cars)
    del(crossyroad)



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


def update(frame_time):
    crossyroad.update(frame_time)

    for car in red_cars:
        car.update(frame_time)

    for car in red_cars:
        if collide(bombman, car):
            red_cars.remove(car)

    #for car in red_cars:
     #   if collide(car, bombman):
      #      red_cars.stop(car) ?????????????????????????????

    #for car in trucks:
     #   if collide(road, car):
      #      car.stop()

    bombman.update(frame_time)


def draw(frame_time):
    clear_canvas()
    crossyroad.draw()
    for car in red_cars:
        car.draw()

    crossyroad.draw_bb()
    bombman.draw_bb()
    for car in red_cars:
        car.draw_bb()

    bombman.draw()
    update_canvas()






