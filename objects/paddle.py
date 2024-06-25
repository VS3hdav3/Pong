import pygame

class Paddle: 
    width, height = 20, 100
    
    def __init__(self, x, y, vel):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.vel = self.origin_vel = vel

        
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))
        
    def move(self):
        self.y += self.vel
        
    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y
        self.vel = self.origin_vel
