import pygame

class projectile(object):
    def __init__(self, x, y, radius, color, dirx, diry):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dirx = dirx
        self.diry = diry
        self.velx = 10 * dirx
        self.vely = 10 * diry

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x),int(self.y)), self.radius)

class enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        self.vel = 3
        
    def draw(self, win, char):
        win.blit(char, (self.x - 10, self.y - 10))