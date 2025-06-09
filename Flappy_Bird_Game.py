
import pygame
import random

pygame.init()
width, height = 500, 500
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bird = pygame.Rect(100, 250, 30, 30)
velocity = 0
gravity = 1

running = True
while running:
    win.fill((135, 206, 250))  # Sky blue background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -10

    velocity += gravity
    bird.y += velocity
    pygame.draw.rect(win, (255, 0, 0), bird)  # Bird

    pygame.display.update()
    clock.tick(30)

pygame.quit()