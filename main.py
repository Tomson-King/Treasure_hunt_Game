from pygame.sysfont import pygame_main_file
from Game import *
import pygame
from sys import exit

class Main():
    def __init__(self):
        SCR_WDT, SCR_HGT=1280,720
        pygame.init()
        screen = pygame.display.set_mode((SCR_WDT, SCR_HGT),pygame.RESIZABLE)
        clock = pygame.time.Clock()
        menu=True
        start=False
        screen.fill("blue")
        while(True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):
                        start=True
                        player = start_game()
                        
            if start:
                game(screen,player)
            
            if(menu):
                pass#Menu
            else:
                pass#game
            pygame.display.update()
            clock.tick(60)
        pygame.quit()


Main()