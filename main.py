import pygame
from sys import exit
import Game

class Main():
    def __init__(self):
        SCR_WDT, SCR_HGT=1280,720
        pygame.init()
        screen = pygame.display.set_mode((SCR_WDT, SCR_HGT),pygame.RESIZABLE)
        clock = pygame.time.Clock()
        menu=True
        
        while(True):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit()
            if(menu):
                pass#Menu
            else:
                pass#game


        pygame.quit()


Main()