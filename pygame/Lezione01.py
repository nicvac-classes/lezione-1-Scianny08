import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Pygame")

x, y = 320, 240
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= speed
    
    if keys[pygame.K_RIGHT]:
        x += speed
        
    if keys[pygame.K_DOWN]:
        y += speed
        
    if keys[pygame.K_UP]:
        y -= speed
        
    
    screen.fill((30, 30, 50))
    
    cerchio = pygame.draw.circle(
        screen,         #surface
        (255, 0, 0),    #colore rgb
        (x, y),     #x, y
        30              #raggio
        )
    pygame.display.flip()
    
    
    