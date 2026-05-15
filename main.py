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


#function to cast array
def cast_ray(x, y, angle, points):

    for distance in range(0, 200):
        #tip of ray each time
        ray_x = x + distance * math.cos(math.radians(angle))
        ray_y = y + distance * math.sin(math.radians(angle))

        #check off screen bounds
        if ray_x > SCREEN_WIDTH or ray_y > SCREEN_HEIGHT or ray_x < 0 or ray_y < 0:
            return distance
        
        on_road = False
        
        for p in points:
            #check if distance less than radius
            if math.sqrt((ray_x - p[0])**2 + (ray_y - p[1]) ** 2) < 30:
                on_road = True
                break   
            
        if not on_road:
            return distance


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

    #RAY ANGLES
    ray_angles = [
        angle,
        angle + 45,
        angle - 45,
        angle + 90,
        angle - 90
    ]
   


    #drawing
    screen.fill((124, 252, 0))
    for p in points:
        pygame.draw.circle(screen, (80 , 80, 80), p, 30)
    pygame.draw.rect(screen, (3, 36, 252), (x_pos, y_pos, 20, 20))
    pygame.display.flip()
    clock.tick(60)


    
pygame.quit()





