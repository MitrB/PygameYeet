import pygame
#import robot
import player as pl
import classes as cl
import random as rnd

pygame.init()

#game window
window = (800, 800)
win = pygame.display.set_mode(window)
pygame.display.set_caption("Yeet sanctuary")
# general pygame preload
guy = pygame.image.load("Guy.png")
clock = pygame.time.Clock()
# the player character:
character = pl.player(50,50, 64, 64)
projectiles = []
enemies = []
spawn_coord_enemy = [(n,0) for n in range(0, window[0] + 1)] +  [(0,z) for z in range(0, window[1] + 1)] \
                  + [(window[0], q) for q in range(0, window[1] +1)] + [(u, window[1]) for u in range(0, window[0] +1)]

# Redrawing all the elements on the screen in the right order
# from back to front
def redraw():

    win.fill((0,100,100))
    win.blit(guy, (character.x, character.y))
    for p in projectiles:
        p.draw(win)
    for e in enemies:
        e.draw(win)
    pygame.display.update()
    
# Interpreting key-presses
def actions():
    # Updating the cooldown of the shoot-mechanism
    if character.shoot_cooldown > 0:
        character.shoot_cooldown += 1
    if character.shoot_cooldown == 20:
        character.shoot_cooldown = 0

    key = pygame.key.get_pressed()
    
    # Walking mechanism
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

    # Shooting mechanism
    if key[pygame.K_SPACE] and character.shoot_cooldown == 0:
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
        if len(projectiles) < 10:
            projectiles.append(cl.projectile(round(character.x + character.width//2), round(character.y + character.height//2), 2, (0,0,0), dirx, diry))
            character.shoot_cooldown = 1
    
    return

def enemyspawn():
    # enemy spawn cooldown
    if character.enemy_cd > 0:
        character.enemy_cd += 1
    if character.enemy_cd == 40:
        character.enemy_cd = 0

    if character.enemy_cd == 0 and len(enemies) < 5 :
        rand_cord = rnd.choice(spawn_coord_enemy)
        enemies.append(cl.enemy(rand_cord[0], rand_cord[1]))

        character.enemy_cd += 1

# main game loop
run = True
while run:
    clock.tick(60)
    for proj in projectiles:
        for enem in enemies:
            if abs(enem.x + enem.width//2 - proj.x ) < 10 and abs(enem.y + enem.height//2 - proj.y ) < 10:
                if enem in enemies:
                    enemies.pop(enemies.index(enem))
                if proj in projectiles:
                    projectiles.pop(projectiles.index(proj))

    # updating projectiles
    for proj in projectiles:
        if proj.x < window[0] and proj.x > 0 \
        and proj.y < window[1] and proj.y > 0:
            proj.x += proj.velx
            proj.y += proj.vely
        else:
            projectiles.pop(projectiles.index(proj))

    # updating enemies

    for enem in enemies:
        if character.x + 20 > enem.x:
            enem.x += enem.vel
        if character.x + 20 < enem.x:
            enem.x -= enem.vel
        if character.y + 20 > enem.y:
            enem.y += enem.vel
        if character.y + 20 < enem.y:
            enem.y -= enem.vel

        # character hit
        if abs(character.x + 20 - enem.x) < 10 and abs(character.y + 20 - enem.y) < 10:
            print("ding")
            enemies.pop(enemies.index(enem))

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    actions()
    redraw()
    enemyspawn()
    #print(projectiles)
    #print(enemies)

pygame.quit()