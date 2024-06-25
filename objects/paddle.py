import pygame

class Paddle: 
    width, height = 20, 100
    vel = 6
    
    def __init__(self, x, y):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))
        
    def move(self, up=True):
        if up: 
            self.y -= self.vel
        else:
            self.y += self.vel
        
    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y
