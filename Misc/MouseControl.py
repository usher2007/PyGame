__author__ = 'doba'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

pygame.init()

bg_file_name = "sushiplate.jpg"
sprite_file_name = "fugu.png"

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(bg_file_name).convert()
sprite = pygame.image.load(sprite_file_name).convert_alpha()

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

sprite_pos = Vector2(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    pressed_key = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    rotation_direction = pygame.mouse.get_rel()[0]/5.0

    if pressed_key[K_LEFT]:
        rotation_direction = 1.
    if pressed_key[K_RIGHT]:
        rotation_direction = -1.
    if pressed_key[K_UP] or pressed_mouse[0]:
        movement_direction = 1.
    if pressed_key[K_DOWN] or pressed_mouse[2]:
        movement_direction = -1.

    screen.blit(background, (0, 0))

    rotation_sprite  = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotation_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x-w/2, sprite_pos.y-h/2)
    screen.blit(rotation_sprite, sprite_draw_pos)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    heading_x = sin(sprite_rotation*pi/180.)
    heading_y = cos(sprite_rotation*pi/180.)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()
