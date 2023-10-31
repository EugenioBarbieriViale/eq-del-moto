import pygame, sys
from numpy import sqrt, cos

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Oscillatore armonico")

xi = screenx/2-20
yi = 20
m = 500
c = 0.5
g = 9.81

t = 0
v = 0
vi = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((128,128,128))
    
    t += 0.1

    F = m * g - c * v
    a = F/m
    v = vi + a * t
    y = yi + v * t - 0.5 * a * t**2

    pygame.draw.circle(screen, (255,0,0), (xi,y), 40)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
