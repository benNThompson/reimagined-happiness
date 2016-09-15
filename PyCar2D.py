import sys

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
import pymunk.pygame_util
from pymunk import Vec2d

import Car

def main():
    #region Initialize Pygame
    width, height = 750, 750
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 16)
    #endregion

    #region Initialize Pymunk
    space = pymunk.Space()
    space.gravity = (0.0, -1900.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    #endregion

    #region Create the initial generation of cars
    cars = []
    for x in range(10):
        cars.append(Car.random_car())
    car = cars[0]
    #endregion

    # region Add floor
    floor = pymunk.Segment(space.static_body, (50, 500), (700, 500), 5)
    floor.friction = 1
    space.add([floor])
    # endregion

    #region Add car to pymunk space
    # x = width / 2
    # y = height / 2
    #mass = 5
    #endregion

    # region Draw
    while running:
        screen.fill(pygame.color.THECOLORS["white"])
        space.debug_draw(draw_options)

        fps = 60
        dt = 1. / fps
        space.step(dt)

        clock.tick(fps)
        #endregion

if __name__ == '__main__':
    sys.exit(main())
