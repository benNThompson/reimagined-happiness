import sys
import pygame
import pymunk
from pymunk import Vec2d
import Car

def main():
    #region Initialize Pygame
    display_flags = 0
    display_size = (750, 750)

    pygame.init()
    screen = pygame.display.set_mode(display_size, display_flags)
    width, height = screen.get_size()

    def to_pygame(p):
        # Small hack to convert pymunk to pygame coordinates
        return int(p.x), int(-p.y + height)

    def from_pygame(p):
        # The reverse conversion is the same
        return to_pygame(p)

    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 16)
    #endregion

    #region Initialize Pymunk
    space = pymunk.Space()
    space.gravity = (0.0, -1900.0)
    #endregion

    #region Create the initial generation of cars
    cars = []
    for x in range(10):
        cars.append(Car.random_car())
    car = cars[0]
    #endregion

    #region Add car to pymunk space

    #endregion

if __name__ == '__main__':
    sys.exit(main())