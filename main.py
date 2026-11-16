from pygame.sysfont import pygame_main_file
from Game import *
import pygame
from sys import exit
from os import system


class Main():
    def __init__(self):
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        SCR_WDT, SCR_HGT=1280,720
        pygame.init()
        screen = pygame.display.set_mode((SCR_WDT, SCR_HGT),pygame.RESIZABLE)
        gameatts["screen"]["width"]=SCR_WDT
        gameatts["screen"]["height"]=SCR_HGT
        with open("./Game/game_attributes.json","w") as f:
            json.dump(gameatts,f,indent=4)
        clock = pygame.time.Clock()
        menu=True
        start=False
        
        while(True):
            if(gameatts["screen"]["width"]!=screen.width or gameatts["screen"]["height"]!=screen.height):
                gameatts["screen"]["width"]=screen.width
                gameatts["screen"]["height"]=screen.height
                with open("./Game/game_attributes.json","w") as f:
                    json.dump(gameatts,f,indent=4)

            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit()
                if (event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_ESCAPE):
                        exit()
                    if (event.key == pygame.K_RETURN):
                        if not start:
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