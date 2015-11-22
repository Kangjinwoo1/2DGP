from pico2d import *

import game_framework


from boy import Boy # import Boy class from boy.py
from car import RedCar, Truck, GreenCar, YellowCar, BlueCar
from road import Road



name = "main_state"

boy = None
red_cars = None
trucks = None
road = None

def create_world():
    global boy, road, red_cars, trucks, blue_cars, yellow_cars, green_cars

    boy = Boy()
    trucks = [Truck() for i in range(3)]
    green_cars = [GreenCar() for i in range(3)]
    blue_cars = [BlueCar() for i in range(4)]
    yellow_cars = [YellowCar() for i in range(2)]
    red_cars = [RedCar() for i in range(4)]
    red_cars = red_cars + trucks + blue_cars + yellow_cars + green_cars
    road = Road()


def destroy_world():
    global boy, red_cars, road

    del(boy)
    del(red_cars)
    del(road)



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
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    road.update(frame_time)

    for car in red_cars:
        car.update(frame_time)

    for car in red_cars:
        if collide(boy, car):
            red_cars.remove(car)

    #for car in trucks:
     #   if collide(road, car):
      #      car.stop()

    boy.update(frame_time)


def draw(frame_time):
    clear_canvas()
    road.draw()
    for car in red_cars:
        car.draw()

    road.draw_bb()
    boy.draw_bb()
    for car in red_cars:
        car.draw_bb()

    boy.draw()
    update_canvas()






