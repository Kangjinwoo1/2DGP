import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()


def update(frame_time):
    global name
    global logo_time
    if (logo_time > 0.5):
        logo_time = 0
        game_framework.run(title_state)
    logo_time += frame_time

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass




