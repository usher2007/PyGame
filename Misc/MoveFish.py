__author__ = 'doba'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import *

bg_file_name = "sushiplate.jpg"
sprite_file_name = "fugu.png"
SCREEN_SIZE = (640, 480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

background = pygame.image.load(bg_file_name).convert()
sprite = pygame.image.load(sprite_file_name)

clock = pygame.time.Clock()

position = Vector2(100, 100)
speed=Vector2()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size())/2.
    orient = Vector2.from_points(position, destination)
    orient.normalize()

    speed = speed + orient*.6
    position += speed * time_passed_seconds

    pygame.display.update()


