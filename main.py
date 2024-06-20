import pygame
pygame.init()
import random   

width, height =  700, 500

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

FPS = 60

paddle_width, paddle_height = 20, 100
ball_rad = 7

black = (0,0,0)
white=(255,255,255)

score_font = pygame.font.SysFont("Consolas", 50)
score_win = 10

class paddle:
    color = white
    vel = 6
    
    def __init__(self, x, y, width, height):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        
    def move(self, up=True):
        if up: 
            self.y -= self.vel
        else:
            self.y += self.vel
        
    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y

class ball:
    init_vel = random.choice([-5, 5])         #+ve velocity such that in the initial game init, it goes towards the right paddle, without any y_vel
    max_vel = 5
    color = white
    
    def __init__(self, x, y, radius):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.radius = radius
        self.x_vel = self.init_vel
        self.y_vel = 0
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y
        self.y_vel = 0
        self.x_vel *= -1

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and (left_paddle.y - left_paddle.vel >= 0):
        left_paddle.move(up=True)
    if keys[pygame.K_s] and (left_paddle.y + left_paddle.height + left_paddle.vel <= height):
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and (right_paddle.y - right_paddle.vel >= 0):
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and (right_paddle.y + right_paddle.height + right_paddle.vel <= height):
        right_paddle.move(up=False) 
        
def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= height:
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
    
def draw(win, paddles, ball, left_score, right_score):
    win.fill(black)
    for paddle in paddles:
        paddle.draw(win)
    
    left_score_txt = score_font.render(f"{left_score}", 1, white)
    right_score_txt = score_font.render(f"{right_score}", 1, white)
    
    win.blit(left_score_txt, (width // 4 - left_score_txt.get_width() // 2, 20))
    win.blit(right_score_txt, (width * (3 / 4) - right_score_txt.get_width() // 2, 20))

    
    for i in range(10, height, height//20):     #draws a dashed line in the middle
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, white, ((width//2 - 5//2), i, 5, height//20))
        
    ball.draw(win)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    
    left_paddle = paddle(10, height//2 - paddle_height//2, paddle_width, paddle_height)
    right_paddle = paddle(width - 10 - paddle_width, height//2 - paddle_height//2, paddle_width, paddle_height)
    
    b = ball(width//2, height//2, ball_rad)
    
    l_score = 0
    r_score = 0
    
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], b, l_score, r_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        b.move()
        handle_collision(b, left_paddle, right_paddle)
        
        if b.x < 0:
            r_score += 1
            b.reset()
        elif b.x > width:
            l_score += 1
            b.reset()
        
        won = False
        if l_score >= score_win:
            won = True
            won_txt = "Left Player Won!"
        elif r_score >= score_win:
            won = True
            won_txt = "Right Player Won!"
        
        if won:
            text = score_font.render(won_txt, 1, white)
            x = width//2 - text.get_width()//2
            y = height//2 - text.get_height()//2
            pygame.draw.rect(WIN, black, (x - 10, y - 10, text.get_width() + 20, text.get_height() + 20))
            WIN.blit(text, (x, y))
            pygame.display.update()
            pygame.time.delay(5000)
            b.reset()
            left_paddle.reset()
            right_paddle.reset()
            l_score = 0 
            r_score = 0
        
    pygame.quit()
    
if __name__ == '__main__':      #this makes it so the main function only runs when called, ie not when it is imported, I suppose it checks the file name to ensure it is main
    main()