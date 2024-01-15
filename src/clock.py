import pyglet
from pyglet import image
from pyglet.gl import *

from datetime import datetime, date


#from files import thing, load, resources
from collections import namedtuple
#import random

# Set up a window
myWindow = namedtuple('myWindow', ['X', 'Y'])
myWin = myWindow(800, 600)
game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=True, resizable=False)

main_batch = pyglet.graphics.Batch()

# Global Wind
globalVx = 0.0

# Set up the two top labels
#score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Testing - Clock!", x=400, y=575, anchor_x='center', batch=main_batch)

# Set up the game over label offscreen
time_label = pyglet.text.Label(text="Time", x=100, y=-300, anchor_x='left', batch=main_batch, font_size=48)
date_label = pyglet.text.Label(text="Date", x=100, y=-400, anchor_x='left', batch=main_batch, font_size=48)

#counter = pyglet.window.FPSDisplay(window=game_window)

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0

@game_window.event
def on_draw():
    game_window.clear()

    #bgpicSprite.draw()

    main_batch.draw()

    #fgpicSprite.draw()

    #counter.draw()

def update(dt):
    global time_label, level_label, date_label

    # Called to update time per second
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)
    time_label = pyglet.text.Label(text=current_time, x=40, y=60, anchor_x='left', batch=main_batch, font_size=72)
    today = date.today()
    # Textual month, day and year
    strdate = today.strftime("%m/%d/%y")
    date_label = pyglet.text.Label(text=strdate, x=70, y=20, anchor_x='left', batch=main_batch, font_size=36)


if __name__ == "__main__":
    # Start it up!
    #init()

    # Update the clock every second
    pyglet.clock.schedule_interval(update, 1.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
