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

ROAD_TOP = 250
ROAD_BOTTOM = 350

points = []

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
        x_pos -= 3
    if keys[pygame.K_d]:
        x_pos += 3
    if keys[pygame.K_s]:
        y_pos += 3
    if keys[pygame.K_w]:
        y_pos -= 3



    x_pos = max(0, min(x_pos, SCREEN_WIDTH - 40))  
    y_pos = max(ROAD_TOP, min(y_pos, ROAD_BOTTOM - 20))



    #drawing
    screen.fill((124, 252, 0))
    for p in points:
        pygame.draw.circle(screen, (80 , 80, 80), p, 30)
    pygame.draw.rect(screen, (3, 36, 252), (x_pos, y_pos, 20, 20))
    pygame.display.flip()
    clock.tick(60)


    
pygame.quit()





