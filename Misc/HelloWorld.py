__author__ = 'doba'

bg_file_name = 'sushiplate.jpg'
mouse_image_file = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello World")
background = pygame.image.load(bg_file_name).convert()
mouse_cursor = pygame.image.load(mouse_image_file).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    screen.blit(mouse_cursor, (x, y))

    pygame.display.update()


