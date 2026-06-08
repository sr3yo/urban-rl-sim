import pygame
import math
import numpy as np
import gymnasium as gym

class CarEnvironment(gym.Env):
    def __init__(self):

        #constructor
        super().__init__()

        #initialize key properties for environment
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 600
        self.ROAD_COLOR = (80,80,80)

        self.start_x = 500
        self.start_y = 60
        self.start_angle = 180

        self.x = self.start_x
        self.y = self.start_y
        self.angle = self.start_angle
        self.speed = 0

        #4 options; left, right, accelerate and break
        self.action_space = gym.spaces.Discrete(4)

        #5 rays with distances between 0 - 200
        self.observation_space = gym.spaces.Box(
            low = 0, high = 200, shape = (5,), dtype=np.float32
        )


        #initialize pygame attributes
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        #drawing track 
        self.track_surface = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.track_surface.fill((124, 252, 0))
        pygame.draw.ellipse(self.track_surface, (80,80,80), (20,20,960,560), 80)        


    #function to cast array
    def cast_ray(self, x, y, angle):
        for distance in range(0, 200):
            #tip of ray each time
            ray_x = x + distance * math.cos(math.radians(angle))
            ray_y = y - distance * math.sin(math.radians(angle))

            #check off screen bounds
            if ray_x >= self.SCREEN_WIDTH or ray_y >= self.SCREEN_HEIGHT or ray_x < 0 or ray_y < 0:
                return distance
            color = self.track_surface.get_at((int(ray_x), int(ray_y)))
            if color[:3] != self.ROAD_COLOR:
                return distance
        return 200


    #reset function
    def reset(self, seed = None, options = None):


        #clear and allow gymnasium to handle reprod seeding
        super().reset(seed=seed)
        #reset all class variables to initial state
        self.x = self.start_x
        self.y = self.start_y
        self.angle = self.start_angle
        self.speed = 0


        #get the initial ray distances as well when the car resets
        ray_angles = [self.angle, self.angle+45, self.angle-45, self.angle+90, self.angle-90]
        distances = []

        for ray_angle in ray_angles:
            d = self.cast_ray(self.x, self.y, ray_angle)
            distances.append(d)
        
        #return as a numpy array
        return np.array(distances, dtype=np.float32), {}
    
    def step(self, action):
        #steering left
        if action == 0:
            self.angle += 3
        #steering right
        elif action == 1:
            self.angle -= 3
        #accelerate
        elif action == 2:
            self.speed = 3
        #brake
        elif action == 3:
            self.speed = max(0, self.speed - 1)
        
        #update x and y pos
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y  -= self.speed * math.sin(math.radians(self.angle))
            


