import pygame
class player(object):
    """docstring for player"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1

        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.last = "right"

    def draw(self, win):
        win.blit(guy, (self.x, self.y))

    def movementtrack(self, direction):
        for i in [self.up, self.right, self.down, self.left]:
            if direction != i:
                i = False
            else:
                i = True   
