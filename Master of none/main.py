import pygame
#import robot
#import player

pygame.init()

#game window
window = (500, 500)
win = pygame.display.set_mode(window)
pygame.display.set_caption("Yeet sanctuary")

guy = pygame.image.load("Guy.png")
run = True
clock = pygame.time.Clock()

x = 50
y = 50
vel = 5

def redraw():

    win.fill((0,100,100))
    win.blit(guy, (x,y))
    pygame.display.update()
    return

def movement():
    global x
    global y

    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT] and x > vel:
        x -= vel
    if key[pygame.K_RIGHT] and x < window[0] - vel - 32:
        x += vel
    if key[pygame.K_UP] and y > vel:
        y -= vel
    if key[pygame.K_DOWN]and y < window[1] - vel - 64:
        y += vel  
    return

while run:
    clock.tick(30)
    #pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    movement()
    redraw()

pygame.quit()