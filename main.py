import pygame
from objects import game
from objects import paddle
from objects import ball



def main():
    run = True
    clock = pygame.time.Clock()
    
    width, height =  700, 500
    
    black = (0,0,0)
    white = (255,255,255)
    
    l_score = 0
    r_score = 0
    
    score_font = pygame.font.SysFont("PixelifySans-Regular", 50)
    score_win = 10
    
    WIN = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    g = game.Game(WIN, width, height)
    l_paddle = paddle.Paddle(
            10, height // 2 - paddle.Paddle.height // 2)
    r_paddle = paddle.Paddle(
            width - 10 - paddle.Paddle.width, height // 2 - paddle.Paddle.height//2)
    b = ball.Ball(width // 2, height // 2)

    while run:
        clock.tick(60)
        g.draw(g.window, [l_paddle, r_paddle], b, l_score, r_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
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
            pygame.draw.rect(g.window, black, (x - 10, y - 10, text.get_width() + 20, text.get_height() + 20))
            g.window.blit(text, (x, y))
            pygame.display.update()
            pygame.time.delay(5000)
            b.reset()
            l_paddle.reset()
            r_paddle.reset()
            l_score = 0 
            r_score = 0
        
        keys = pygame.key.get_pressed()
        g.handle_paddle_movement(keys, l_paddle, r_paddle)
        b.move()
        g.handle_collision(b, l_paddle, r_paddle)
        
        if b.x < 0:
            r_score += 1
            b.reset()
        elif b.x > width:
            l_score += 1
            b.reset()
    pygame.quit()  

main()