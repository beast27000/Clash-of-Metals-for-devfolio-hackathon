import pygame
import random
import math
from pygame import mixer

# intializing

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
mixer.music.load('wind.wav')
mixer.music.play(-1)
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('rocket.py.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('thor hammer 2.png')
playerx = 370
playery = 480
playerx_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('iron man.png'))
    # enemyx = 370
    # enemyy = 50
    # enemyx_change = 0
    enemyx.append(random.randint(0, 800))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(4)
    enemyy_change.append(40)

#intialilizing the bullet

bulletimg = pygame.image.load('thunder.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"
# score = 0
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def iscollition(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


#intialzing player movement(here the hammer) what  to do if bullet fired

running = True
while running:

    screen.fill((204, 204, 255))
    screen.blit(background,(0,0))
    # playerx += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound =mixer.Sound('scifi002.wav')
                    bullet_sound.play()

                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]

        collition = iscollition(enemyx[i], enemyy[i], bulletx, bullety)
        if collition:
            explosion_sound = mixer.Sound('scifi011.wav')
            explosion_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            # print(score)
            enemyx[i] = random.randint(0, 800)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
    # collition = iscollition(enemyx, enemyy, bulletx, bullety)
    # if collition:
    #    bullety = 480
    #    bullet_state = "ready"
    #    score += 1
    #    print(score)
    #    enemyx = random.randint(0, 735)
    #    enemyy = random.randint(50, 150)

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()
