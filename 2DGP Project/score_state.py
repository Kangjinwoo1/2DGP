import game_framework
from pico2d import *

import main_state
import title_state
import json


name = "End_State"
image = None
font = None

def enter():
    global image, font, font1
    image = load_image('score.png')
    font = load_font('ENCR10B.TTF')

def exit():
    global image,font
    del(image)
    del(font)


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
                game_framework.change_state(title_state)

def update(frame_time):
    pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)

    with open('score.txt', 'r') as f:
        score_list = json.load(f)
    score_list.sort(reverse = True)

    top10 = score_list[:10]

    i = 1
    for score in top10:
        font.draw(400, 500 - i * 30, "%2d. Score : %d" %(i,score[0]), (0, 50, 250))
        #font.draw(350, 450 - i * 30, "Time : %d sec, level : %d" %(score[1],score[2]), (100,100,0))
        i += 1
    #font.draw(100, 100, "Press ESC To Continue", (100,49,0))
    #font1.draw(100, 100, "Press ESC To Continue", (255,255,255))

    update_canvas()