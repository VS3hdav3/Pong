import pygame
from objects import *

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