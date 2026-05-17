import pygame
import math 

pygame.init()

#init screen!!!!!!!
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#need this layer functionality to draw the surface; cannot use get_at() otherwise
track_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
track_surface.fill((124, 252, 0))

pygame.draw.ellipse(track_surface,(80,80,80), (20,20,960,560), 80)


#init positions
x_pos = 400
y_pos = 300

#angle and speed variables
angle = 0
speed = 0

ROAD_COLOR = (80,80,80)

#function to cast array
def cast_ray(x, y, angle):

    for distance in range(0, 200):
        #tip of ray each time
        ray_x = x + distance * math.cos(math.radians(angle))
        ray_y = y - distance * math.sin(math.radians(angle))

        #check off screen bounds
        if ray_x >= SCREEN_WIDTH or ray_y >= SCREEN_HEIGHT or ray_x < 0 or ray_y < 0:
            return distance
        
        color = track_surface.get_at((int(ray_x), int(ray_y)))
        if color[:3] != ROAD_COLOR:
            return distance
        
    return 200


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
    
    #calculate current x pos and y pos
    x_pos += speed * math.cos(math.radians(angle))
    y_pos -= speed * math.sin(math.radians(angle))

    #RAY ANGLES
    ray_angles = [
        angle,
        angle + 45,
        angle - 45,
        angle + 90,
        angle - 90
    ]
   


    #drawing
    screen.blit(track_surface, (0,0))

    

    #for each respective ray angle, draw the ray-line
    for ray_angle in ray_angles:

        d = cast_ray(x_pos, y_pos, ray_angle)

        #calculate the end pos for the end of the line respectively
        end_x = x_pos + d * math.cos(math.radians(ray_angle))
        end_y = y_pos - d * math.sin(math.radians(ray_angle))

        pygame.draw.line(screen, (255,255,255), (int(x_pos), int(y_pos)), (int(end_x), int(end_y)))

    #draw the actual car
    pygame.draw.rect(screen, (3, 36, 252), (x_pos, y_pos, 20, 20))
    pygame.display.flip()

    #every 60 frames
    clock.tick(60)


    
pygame.quit()





