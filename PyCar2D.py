import pyglet
import pymunk.pyglet_util

import Car

# First, create the initial generation of cars
cars = []
for x in range(10):
    cars.append(Car.random_car())

# Display them
window = pyglet.window.Window(1000, 700, vsync=False)
space = pymunk.Space()
draw_options = pymunk.pyglet_util.DrawOptions()
