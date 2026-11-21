import pygame
import json
from .Display import *
from .Game_engine import Player
from sys import exit

class Menu():
    def __init__(self,screen):
            self.mouse_click_pos = (0,0)

            mouse_pos = pygame.mouse.get_pos()
            mouse=pygame.mouse.get_just_pressed()
            if(mouse[0]):
                self.mouse_click_pos = pygame.mouse.get_pos()
            with open("./Game/game_attributes.json","r") as f:
                gameatts=json.load(f)
            self.screen_x=gameatts["screen"]["width"]
            self.screen_y=gameatts["screen"]["height"]
            c_x=self.screen_x//2
            c_y=self.screen_y//2
            

            newgame_img=pygame.image.load("graphics/newgame.png").convert_alpha()
            continue_img=pygame.image.load("graphics/continue.png").convert_alpha()
            exit_img=pygame.image.load("graphics/exit.png").convert_alpha()
            newgame_selected_img=pygame.image.load("graphics/newgameselected.png").convert_alpha()
            continue_selected_img=pygame.image.load("graphics/continueselected.png").convert_alpha()
            exit_selected_img=pygame.image.load("graphics/exitselected.png").convert_alpha()

            newgame_img.set_colorkey((126,196,0))
            continue_img.set_colorkey((126,196,0))
            exit_img.set_colorkey((126,196,0))
            newgame_selected_img.set_colorkey((126,196,0))
            continue_selected_img.set_colorkey((126,196,0))
            exit_selected_img.set_colorkey((126,196,0))

            newgame_rect=newgame_img.get_rect(center = (c_x,c_y-120))
            continue_rect=continue_img.get_rect(center = (c_x,c_y))
            exit_rect=exit_img.get_rect(center = (c_x,c_y+120))
            newgame_selected_rect=newgame_selected_img.get_rect(center = (c_x,c_y-120))
            continue_selected_rect=continue_selected_img.get_rect(center = (c_x,c_y))
            exit_selected_rect=exit_selected_img.get_rect(center = (c_x,c_y+120))

            
            menusprites=[]
            menusprites.clear()
            menusprites.append((newgame_img,newgame_rect))
            menusprites.append((continue_img,continue_rect))
            menusprites.append((exit_img,exit_rect))
            
            self.menu,self.player=True,None
            if(newgame_selected_rect.collidepoint(mouse_pos)):
                menusprites.append((newgame_selected_img,newgame_selected_rect))
                menusprites.remove((newgame_img,newgame_rect))
            elif( continue_selected_rect.collidepoint(mouse_pos)):
                menusprites.append((continue_selected_img,continue_selected_rect))
                menusprites.remove((continue_img,continue_rect))
            elif(exit_selected_rect.collidepoint(mouse_pos)):
                menusprites.append((exit_selected_img,exit_selected_rect))
                menusprites.remove((exit_img,exit_rect))
            else:
                pass
            if(newgame_selected_rect.collidepoint(self.mouse_click_pos)):
                self.menu=False
                self.start_game()
            elif( continue_selected_rect.collidepoint(self.mouse_click_pos)):
                self.menu=False
                self.continue_game()
            elif(exit_selected_rect.collidepoint(self.mouse_click_pos)):          
                exit()
            else:
                pass
            Display(screen,[menusprites])
            
    def start_game(self):
        self.player=Player((0,0))


    def continue_game(self):
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.player=Player((gameatts["player"]["x"],gameatts["player"]["y"]))
        
        



