import engine
from setup import *
import pygame
from pygame.locals import *
from random import randint



pygame.init ()

screen = pygame.display.set_mode ((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def randColor ():
    result = []
    for i in range (3):
        result.append (randint (0, 255))
    return result



eng = engine.Engine (WIN_WIDTH, WIN_HEIGHT)
alive = True
timer = 0
while alive:
    for event in pygame.event.get ():
        if event.type == QUIT:
            alive = False
        elif event.type == MOUSEBUTTONDOWN:
            timer = 0
        elif event.type == MOUSEBUTTONUP:
            speed = pygame.mouse.get_rel ()
            eng.addEnt (randColor (),
            event.pos[0],
            event.pos[1],
            timer + START_SIZE,
            timer + START_SIZE,
            speed[0] / 10 * MOUSE_SENSITIVITY,
            speed[1] / 10 * MOUSE_SENSITIVITY,
            timer)
        keys = pygame.key.get_pressed ()
        if keys[K_BACKSPACE]:
            if eng.entities:
                eng.entities.pop ()

    # DOESNT WORK
    """
    keys = pygame.key.get_pressed()
    if keys[K_UP] and GRAV_FORCE > 0:
        GRAV_FORCE -= 1000000
        print(GRAV_FORCE)
    elif keys[K_DOWN]:
        GRAV_FORCE += 1000000
        print(GRAV_FORCE)
    """
    timer += 1
    screen.fill (BLACK)
    eng.update (PRECISION)
    eng.drawEnts (screen)
    clock.tick (FPS)
    pygame.display.flip()

