import pygame
import random

class Ball:
    init_vel = random.choice([-5, 5])         #+ve velocity such that in the initial game init, it goes towards the right paddle, without any y_vel
    max_vel = 5
    radius = 7
    
    def __init__(self, x, y):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.x_vel = self.init_vel
        self.y_vel = 0
        
    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y
        self.y_vel = 0
        self.x_vel *= -1