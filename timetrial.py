import pygame
import time
import math
import sys
import track
import mainmenu
from car import Car
from pygame.locals import *

def completeLap(car, finish_line):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 5)) and (car.hitbox[0] > (finish_line[0] - 5)):
            print("Lap finished")



def timeTrial(display_surface):
    # display_surface = screen
    track1 = track.Track()
    white = (0, 128, 0)
    clock = pygame.time.Clock()
    t0 = time.time()

    car = Car('images/f1sprite.png', (719, 144))
    car_group = pygame.sprite.Group(car)

    pad_group = track1.getPads()
    finish_line = (960,50,20,125)
    while True:
        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)
        track.checkpoint(display_surface)
        deltat = clock.tick(60)
        font = pygame.font.Font('fonts/American Captain.ttf', 32)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                car.k_right = down * -5
            elif event.key == K_SPACE:
                car.speed = 0
            elif event.key == K_LEFT:
                car.k_left = down * 5
            elif event.key == K_UP:
                car.k_up = down * 2
            elif event.key == K_DOWN:
                car.k_down = down * -2
            elif event.key == K_ESCAPE:
                mainmenu.main_menu(display_surface)
                # sys.exit(0)  # quit the game

        # Update car and draw track
        font = font.render("Time: " + str(), True, (255, 255, 255))
        display_surface.blit(font, (0,0))
        car_group.update(deltat)
        car_group.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
        pygame.display.flip()
        completeLap(car,finish_line)
        pygame.display.update()