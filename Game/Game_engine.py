import pygame
from sys import exit
from .Display import * 
import json

with open("./Game/map.json","r") as f:
            map=json.load(f)


class Player(pygame.sprite.Sprite):
    # major atributes
    # player (x,y)
    
    def __init__(self):
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.screen_x=gameatts["screen"]["width"]
        self.screen_y=gameatts["screen"]["height"]
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill("red")
        self.rect=self.image.get_rect()
        self.rect.midbottom=(self.screen_x//2,self.screen_y//2)
        self.x=0
        self.y=0
        self.pos=(int(self.x),int(self.y)) 
    def movement(self):
        delta=10
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y+=delta
        if key[pygame.K_s]:
            self.y-=delta
        if key[pygame.K_a]:
            self.x+=delta
        if key[pygame.K_d]:
            self.x-=delta
        self.pos=(int(self.x),int(self.y))
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.screen_x=gameatts["screen"]["width"]
        self.screen_y=gameatts["screen"]["height"] 
        self.rect.midbottom=(self.screen_x//2,self.screen_y//2)         

    def update(self):
        self.movement()



class Map(pygame.sprite.Sprite):
    # should update based on player coords
    
    
    def __init__(self,player,coords):
        
        super().__init__()
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.screen_x=gameatts["screen"]["width"]
        self.screen_y=gameatts["screen"]["height"]
        img=None      
        img=map[str(coords)]
        self.grid=100
        self.pos = (int(((0-coords[0])*self.grid+player.pos[0])+self.screen_x//2),int(((0-coords[1])*self.grid+player.pos[1])+self.screen_y//2))
        
        self.image= pygame.Surface((self.grid,self.grid))
        if(img!=None):   
            self.image.fill(img)
        elif((coords[0]%2!=0 and coords[1]%2==0) or (coords[0]%2==0 and coords[1]%2!=0)):
            self.image.fill("green")
        else:
            self.image.fill("yellow")
                
        self.rect = self.image.get_rect()
        self.rect.center=self.pos


    
    
    def get_center(self,player):
        center=(int((((0+player.pos[0])-self.grid/2)//self.grid)+1),int((((0+player.pos[1])-self.grid/2)//self.grid)+1))
        return center

    def create_map(self,player):
        

        center = self.get_center(player)
        topleft=(center[0]+int(((self.screen_x/2)+self.grid)//self.grid),center[1]+int(((self.screen_y/2)+self.grid)//self.grid))
        obstacles=pygame.sprite.Group()
        obstacles.empty()
        i,j=topleft
        
        
        while(True):
            while(True):
                obstacle=Map(player,(i,j))
                
                if (obstacle.pos[1]< -2*(obstacle.grid) or obstacle.pos[1]> (self.screen_y+obstacle.grid)):
                    
                    break
                else:
                    obstacles.add(obstacle)
                j-=1
            i-=1
            j=topleft[1]       

            if (obstacle.pos[0]< -2*(obstacle.grid) or obstacle.pos[0]> (self.screen_x+obstacle.grid)):
                break
        
        
        return obstacles
        
    def update(self):
        pass



class Chest(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def update(self):
        pass
def change_map():
    with open("./Game/sea_and_islands.json","r") as f:
             map=json.load(f)
    with open("./Game/map.json","w") as f:
            json.dump(map,f,indent=4)

def start_game():
    player=Player()
    
    with open("./Game/sea_and_islands.json","r") as f:
            map=json.load(f)
    with open("./Game/map.json","w") as f:
            json.dump(map,f,indent=4)
    
    return player


def continue_game():
    with open("./Game/game_attributes.json","r") as f:
        gameatts=json.load(f)
    player=Player()
    player.x=gameatts["player"]["x"]
    player.y=gameatts["player"]["y"]

def game(screen,player):
    players=pygame.sprite.GroupSingle()
    players.add(player)
    players.update()
    obstacle=Map(player,(0,0))
    obstacles=obstacle.create_map(player)
    game_display(screen,players,obstacles)
    