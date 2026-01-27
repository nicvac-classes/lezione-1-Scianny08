import random
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Pygame")

x, y = 320, 240
raggio = 30
speed = 5
clock = pygame.time.Clock()
colore = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    
    if keys[pygame.K_RIGHT]:
        x += speed
        
    if keys[pygame.K_DOWN]:
        y += speed
        
    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_SPACE]:
        colore = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if keys[pygame.K_PLUS] or pygame.K_KP_PLUS:
        raggio += 1
        
    #sinistra
    if x < raggio: x = raggio

    #destra
    if x > 640 - raggio: x = 640 - raggio

    #sotto
    if y < raggio: y = raggio

    #sopra
    if y > 480 - raggio: y = 480 - raggio


    screen.fill((30, 30, 50))
    
    cerchio = pygame.draw.circle(
        screen,         #surface
        colore,         #colore rgb
        (x, y),         #x, y
        raggio              #raggio
    )
    
    pygame.display.flip()
    clock.tick(60)
