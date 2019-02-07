import pygame
#import robot
import player as pl
import classes as cl

pygame.init()

#game window
window = (500, 500)
win = pygame.display.set_mode(window)
pygame.display.set_caption("Yeet sanctuary")
# general pygame preload
guy = pygame.image.load("Guy.png")
clock = pygame.time.Clock()
# the player character:
character = pl.player(50,50, 64, 64)
projectiles = []

def redraw():

    win.fill((0,100,100))
    win.blit(guy, (character.x, character.y))
    for p in projectiles:
        p.draw(win)

    pygame.display.update()
    

def movement():

    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.last = "left"
    else:
        character.left = False
    if key[pygame.K_RIGHT] and character.x < window[0] - character.vel - character.width:
        character.x += character.vel
        character.right = True
        character.last = "right"
    else:
        character.right = False
    if key[pygame.K_UP] and character.y > character.vel:
        character.y -= character.vel
        character.up = True
        character.last = "up"
    else:
        character.up = False
    if key[pygame.K_DOWN]and character.y < window[1] - character.vel - character.height:
        character.y += character.vel
        character.down = True
        character.last = "down"
    else:
        character.down = False

    if key[pygame.K_SPACE]:
        if character.left:
            dirx = -1
        elif character.right:
            dirx = 1
        else:
            dirx = 0

        if character.up:
            diry = -1
        elif character.down:
            diry = 1
        else:
            diry = 0

        if dirx == 0 and diry == 0:
            if character.last == "right":
                dirx = 1
            if character.last == "left":
                dirx = -1
            if character.last == "down":
                diry = 1
            if character.last == "up":
                diry = -1
        if len(projectiles) < 1000:
            projectiles.append(cl.projectile(round(character.x + character.width//2), round(character.y + character.height//2), 2, (0,0,0), dirx, diry))
    return


run = True
while run:
    clock.tick(60)
    #pygame.time.delay(50)
    print(projectiles)
    for proj in projectiles:
        if proj.x < window[0] and proj.x > 0 \
        and proj.y < window[1] and proj.y > 0:
            proj.x += proj.velx
            proj.y += proj.vely
        else:
            projectiles.pop(projectiles.index(proj))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    movement()
    redraw()

pygame.quit()