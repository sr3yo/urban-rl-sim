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

        self.start_x = 400
        self.start_y = 80
        self.start_angle = 0

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
        
