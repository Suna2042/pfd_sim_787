import pygame
from game import Game

pygame.init()

screen_width=900
screen_height=900
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TCAS Simulator: 787")

#FPS設定
FPS=30
clock=pygame.time.Clock()

game=Game()

#メインループ====================================================
run=True
while run:
    game.run()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()
    clock.tick(FPS)
    #print(clock.get_fps())

#===============================================================
pygame.quit()