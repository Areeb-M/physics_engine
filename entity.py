import pygame
from pygame.locals import *

class Entity (object):
    def __init__ (self, color, x, y, width, height, vx, vy, mass):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.timeInAir = 0

    def update (self, fps):
        self.x += self.vx / fps
        self.y += self.vy / fps
        self.y += 9.8 * self.timeInAir * self.timeInAir

    def collide (self, b):
        if self.mass == b.mass or b.mass < self.mass:
            self.mass += .0001
        else:
            ax = self.vx - b.vx
            ay = self.vy - b.vy

            self.vx = (((self.mass - b.mass) / (self.mass + b.mass)) * ax) + b.vx
            self.vy = (((self.mass - b.mass) / (self.mass + b.mass)) * ay) + b.vy

            b.vx += ((2 * self.mass / (self.mass + b.mass)) * ax)
            b.vy += ((2 * self.mass / (self.mass + b.mass)) * ay)

    def draw (self, screen):
        pygame.draw.rect (screen, self.color, (self.x, self.y, self.width, self.height))

