import pygame
class player(object):
    """docstring for player"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4

        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.last = "right"
        self.shoot_cooldown = 0
        self.enemy_cd = 0

    def draw(self, win):
        win.blit(guy, (self.x, self.y))

     
