import pygame
class player(object):
    """docstring for player"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.vel = 4

        self.up = False
        self.right = False
        self.down = False
        self.left = False
        self.last = "right"

        self.shoot_cooldown = 0
        self.enemy_cd = 0
        #self.health = 5
        self.score = 0
        self.highscore = 0

    def draw(self, win, char):
        win.blit(char, (self.x, self.y))

     
