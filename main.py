import pygame
import time
import random
import sys

pygame.display.set_caption("Ping Pong")
KEPERNYO_HOSSZUAG = 1000
KEPERNYO_SZELESEG = 1000
jatekos1 = pygame.Rect((2, 2, 20, 150))
szin = (255, 255, 255)
jatekos2 = pygame.Rect((KEPERNYO_HOSSZUAG - 22, 20, 20, 150))
ping = pygame.Rect((10, 10, 20, 20))
ping_y = KEPERNYO_SZELESEG / 2
Ping_x = KEPERNYO_HOSSZUAG / 2
Ping_x2 = 1
ping_y2 = 1
ping_speed = 1
clock = pygame.time.Clock()


fps = 500

kep = pygame.display.set_mode((KEPERNYO_HOSSZUAG, KEPERNYO_SZELESEG))
fut = True

def jatek():
    kep.fill((0, 0, 0))
    labda = pygame.draw.line(kep, szin, ((KEPERNYO_HOSSZUAG / 2), -5), ((KEPERNYO_HOSSZUAG / 2) + 5, KEPERNYO_SZELESEG))
    pygame.draw.rect(kep, (255, 255, 255), jatekos1)
    pygame.draw.rect(kep, (255, 255, 255), jatekos2)
    pygame.draw.rect(kep, (255, 255, 255), labda)

    # Játékos 1 mozgatása
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and jatekos1.top > 0:
        jatekos1.move_ip(0, -3)
    elif key[pygame.K_s] and jatekos1.bottom < KEPERNYO_SZELESEG:
        jatekos1.move_ip(0, 3)

    # Játékos 2 mozgatása
    if key[pygame.K_UP] and jatekos2.top > 0:
        jatekos2.move_ip(0, -3)
    elif key[pygame.K_DOWN] and jatekos2.bottom < KEPERNYO_SZELESEG:
        jatekos2.move_ip(0, 3)

def pong():
    global Ping_x, ping_y

    pygame.draw.ellipse(kep, (255, 255, 255), ping)


    ping.x += Ping_x * ping_speed
    ping.y += ping_y * ping_speed

while fut:
    jatek()
    pong()

    if ping.colliderect(jatekos1):
        Ping_x *= -1 
    if ping.colliderect(jatekos2):
        Ping_x *= -1 
    if ping.top <= 0 or ping.bottom >= KEPERNYO_SZELESEG:
        ping_y *= -1
    if ping.right >= KEPERNYO_HOSSZUAG or ping.left <= 0:
        ping.center = (KEPERNYO_HOSSZUAG / 2, KEPERNYO_SZELESEG / 2)
        Ping_x = random.choice((-1, 1))
        ping_y = random.choice((-1, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
            
    pygame.display.update()
    

    clock.tick(fps)

pygame.quit()
