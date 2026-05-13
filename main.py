import pygame


pygame.init()

#init screen!!!!!!!
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#init positions
x_pos = 400
y_pos = 300

ROAD_TOP = 250
ROAD_BOTTOM = 350



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
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (80, 80, 80), (0, 250, SCREEN_WIDTH, 100))
    pygame.draw.rect(screen, (255, 255, 0), (x_pos, y_pos, 20, 20))
    pygame.display.flip()
    clock.tick(60)


    
pygame.quit()





