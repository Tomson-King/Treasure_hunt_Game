import pygame
from sys import exit
from .Display import * 
screen_x=1280
screen_y=720



class Player(pygame.sprite.Sprite):
    # major atributes
    # player (x,y)
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,30))
        self.image.fill("red")
        self.rect=self.image.get_rect()
        self.rect.midbottom=(screen_x//2,screen_y//2)
        self.x=0
        self.y=0
        self.pos=(int(self.x),int(self.y)) 
    def movement(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.x+=0.1
        if key[pygame.K_s]:
            self.x-=0.1
        if key[pygame.K_a]:
            self.y-=0.1
        if key[pygame.K_d]:
            self.y+=0.1
        self.pos=(int(self.x),int(self.y))          

    def update(self):
        self.movement()



class Obstacles(pygame.sprite.Sprite):
    # should update based on player coords
    
    def __init__(self,player):
        super().__init__()
        self.grid=100
        center=((((0+player.pos[0])-self.grid/2)//self.grid)+1,(((0+player.pos[1])-self.grid)//self.grid)+1)
        topleft=(center[0]+int(((screen_x/2)+self.grid)//self.grid),center[1]+int(((screen_y/2)+self.grid)//self.grid))
        
    def update(self):
        pass



class Chest(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def update(self):
        pass


def start_game():
    player=Player()
    
    return player


def continue_game():
    pass

def game(screen,player):
    players=pygame.sprite.GroupSingle()
    players.add(player)
    players.update()
    obstacles=None
    game_display(screen,players,obstacles)
    print(player.pos)