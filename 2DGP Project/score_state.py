import game_framework
from pico2d import *
import start_state
import title_state
import main_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('score.png')


def exit():
    global image
    del(image)
    close_canvas()


def update(frame_time):
    pass


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
    pass


def pause(): pass

def resume(): pass