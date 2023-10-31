import pygame, sys
from numpy import sqrt, cos

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Oscillatore armonico")

A = 200
xi = screenx/2-20
k = 10
m = 500

x = A
t = 0
v_ang = sqrt(k/m)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((128,128,128))

    t += 1
    x = A * cos(v_ang * t)

    p = xi + x

    pygame.draw.line(screen, (0,0,0), (0,screeny/2), (p,screeny/2), 7)
    pygame.draw.circle(screen, (255,0,0), (p,screeny/2), 40)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
