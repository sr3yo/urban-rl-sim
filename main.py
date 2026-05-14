import pygame
import math 

pygame.init()

#init screen!!!!!!!
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#init positions
x_pos = 400
y_pos = 300


#for figure 8 road
points = []

#angle and speed variables
angle = 0
speed = 0

for t in range(0, 1000):
    x = SCREEN_WIDTH//2 + int(400 * math.sin(t * 0.01))
    y = SCREEN_HEIGHT//2 + int(200 * math.sin(t * 0.02))
    points.append((x, y))



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        angle -= 3

    if keys[pygame.K_d]:
        angle += 3

    if keys[pygame.K_w]:
        speed = 3

    elif keys[pygame.K_s]:
        speed = -3

    
    else:
        speed = 0
    
    x_pos += speed * math.cos(math.radians(angle))
    y_pos -= speed * math.sin(math.radians(angle))
   


    #drawing
    screen.fill((124, 252, 0))
    for p in points:
        pygame.draw.circle(screen, (80 , 80, 80), p, 30)
    pygame.draw.rect(screen, (3, 36, 252), (x_pos, y_pos, 20, 20))
    pygame.display.flip()
    clock.tick(60)


    
pygame.quit()





