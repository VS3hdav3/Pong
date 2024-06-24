from .paddle import paddle
from .ball import ball
import pygame
pygame.init()


class game:
    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.left_paddle = paddle(
            10, self.window_height // 2 - paddle.HEIGHT // 2)
        self.right_paddle = paddle(
            self.window_width - 10 - paddle.WIDTH, self.window_height // 2 - paddle.HEIGHT//2)
        self.ball = ball(self.window_width // 2, self.window_height // 2)

        self.left_score = 0
        self.right_score = 0
        self.window = window

    def handle_paddle_movement(self, keys, left_paddle, right_paddle):
        if keys[pygame.K_w] and (left_paddle.y - left_paddle.vel >= 0):
            left_paddle.move(up=True)
        if keys[pygame.K_s] and (left_paddle.y + left_paddle.height + left_paddle.vel <= self.height):
            left_paddle.move(up=False)
        if keys[pygame.K_UP] and (right_paddle.y - right_paddle.vel >= 0):
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and (right_paddle.y + right_paddle.height + right_paddle.vel <= self.height):
            right_paddle.move(up=False) 
            
    def handle_collision(self, ball, left_paddle, right_paddle):
        if ball.y + ball.radius >= self.height:
            ball.y_vel *= -1 
        elif ball.y - ball.radius <= 0:
            ball.y_vel *= -1
        
        if ball.x_vel < 0:
            #left paddle
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                    ball.x_vel *= -1
                    
                    middle_y = left_paddle.y + (left_paddle.height / 2)
                    diff_y = middle_y - ball.y
                    red_f = (left_paddle.height / 2) / ball.max_vel
                    y_Vel = diff_y / red_f
                    ball.y_vel = -1 * y_Vel
        else:
            #right paddle
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
                if ball.x + ball.radius >= right_paddle.x:
                    ball.x_vel *= -1
                    
                    middle_y = right_paddle.y + (right_paddle.height / 2)
                    diff_y = middle_y - ball.y
                    red_f = (right_paddle.height / 2) / ball.max_vel
                    y_Vel = diff_y / red_f
                    ball.y_vel = -1 * y_Vel        
        
    def draw(self, win, paddles, ball, left_score, right_score):
        win.fill(0, 0, 0)
        for paddle in paddles:
            paddle.draw(win)
        
        left_score_txt = self.score_font.render(f"{self.left_score}", 1, (255, 255, 255))
        right_score_txt = self.score_font.render(f"{self.right_score}", 1, (255, 255, 255))
        
        win.blit(left_score_txt, (self.width // 4 - left_score_txt.get_width() // 2, 20))
        win.blit(right_score_txt, (self.width * (3 / 4) - right_score_txt.get_width() // 2, 20))
        for i in range(10, self.height, self.height//20):     #draws a dashed line in the middle
            if i % 2 == 1:
                continue
            pygame.draw.rect(win, (255, 255, 255), ((self.width//2 - 5//2), i, 5, self.height//20))
            
        ball.draw(win)
        pygame.display.update()
