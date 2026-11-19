import pygame
from sys import exit
from .Display import * 
import json

with open("./Game/map.json","r") as f:
            MAP=json.load(f)


class Player():
    # major atributes
    # player (x,y)
    
    def __init__(self):
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.screen_x=gameatts["screen"]["width"]
        self.screen_y=gameatts["screen"]["height"]
        self.image=pygame.Surface((50,50))
        self.image.fill("red")
        self.rect=self.image.get_rect()
        self.rect.midbottom=(self.screen_x//2,self.screen_y//2)
        self.x=0
        self.y=0
        self.pos=(int(self.x),int(self.y)) 
        self.key={'w': True,'s': True,'a': True,'d': True}
        self.delta=10
    def movement(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.player_collision()
            if self.key['w']: self.y+=self.delta
            
        if key[pygame.K_s]:
            self.player_collision()
            if self.key['s']: self.y-=self.delta
            
        if key[pygame.K_a]:
            self.player_collision()
            if self.key['a']: self.x+=self.delta
            
        if key[pygame.K_d]:
            self.player_collision()
            if self.key['d']: self.x-=self.delta
        self.pos=(int(self.x),int(self.y))   
        
        
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.screen_x=gameatts["screen"]["width"]
        self.screen_y=gameatts["screen"]["height"] 
        self.rect.midbottom=(self.screen_x//2,self.screen_y//2)
    def player_collision(self):
        obstacle=Map(self,(0,0))
        Obstacles=obstacle.create_Obstacles(self)
        self.key={'w': True,'s': True,'a': True,'d': True}
        pos=self.rect.midbottom
        
        for i in Obstacles:
            if i[0].collidepoint(pos[0],pos[1]+self.delta):
                self.key['s']=False
            if i[0].collidepoint(pos[0],pos[1]-self.delta):
                self.key['w']=False
            if i[0].collidepoint(pos[0]+self.delta,pos[1]):
                self.key['d']=False
            if i[0].collidepoint(pos[0]-self.delta,pos[1]):
                self.key['a']=False




    def update(self):
        self.movement()



class Map(pygame.sprite.Sprite):
    # should update based on player coords
    
    
    def __init__(self,player,coords):
        
        with open("./Game/game_attributes.json","r") as f:
            gameatts=json.load(f)
        self.screen_x=gameatts["screen"]["width"]
        self.screen_y=gameatts["screen"]["height"]
        self.img=None
        match(MAP[str(coords)]): 
            
             
            case "Deep Ocean": self.img="#01579B"
            
            case"Mid-Depth Water":self.img="#0288D1"
            
            case "Shallow Reef / Coast": self.img="#4DD0E1"
            
            case "Grassland": self.img="#4CAF50"
            
            case "Beach / Sand": self.img="#F4E1A1"
            
            case "Forest": self.img="#2E7D32"
            
            case "Highland / Peak": self.img="#795548"
            
        self.grid=100
        self.pos = (int(((0+coords[0])*self.grid+player.pos[0])+self.screen_x//2),int(((0-coords[1])*self.grid+player.pos[1])+self.screen_y//2))
        
        self.image= pygame.Surface((self.grid,self.grid))
        if(self.img!=None):   
            self.image.fill(self.img)
        elif((coords[0]%2!=0 and coords[1]%2==0) or (coords[0]%2==0 and coords[1]%2!=0)):
            self.image.fill("green")
        else:
            self.image.fill("yellow")
                
        self.rect = self.image.get_rect()
        self.rect.center=self.pos


    
    
    def get_center(self,player):
        center=(int((((0-player.pos[0])-self.grid/2)//self.grid)+1),int((((0+player.pos[1])-self.grid/2)//self.grid)+1))
        return center

    def create_map(self,player):
        

        center = self.get_center(player)
        topleft=(center[0]-int(((self.screen_x/2)+self.grid)//self.grid),center[1]+int(((self.screen_y/2)+self.grid)//self.grid))
        obstacles=[]
        obstacles.clear
        i,j=topleft
        
        
        while(True):
            while(True):
                obstacle=Map(player,(i,j))
                
                if (obstacle.pos[1]< -2*(obstacle.grid) or obstacle.pos[1]> (self.screen_y+obstacle.grid)):
                    
                    break
                else:
                   
                    obstacles.append((obstacle.rect,obstacle.image))
                j-=1
            i+=1
            j=topleft[1]       

            if (obstacle.pos[0]< -2*(obstacle.grid) or obstacle.pos[0]> (self.screen_x+obstacle.grid)):
                break
        
        
        return obstacles

    def create_Obstacles(self,player):
        

        center = self.get_center(player)

        obstacles=[]
        obstacles.clear
        topleft=(center[0]-1,center[1]+1)
        i,j=topleft
        
        while(i<topleft[0]+3):
            while(j>topleft[1]-3):
                obstacle=Map(player,(i,j))
                
                
                match(MAP[str((i,j))]): 
            
             
                    case "Deep Ocean": pass
                        
                    case"Mid-Depth Water":pass
                        
                    case "Shallow Reef / Coast": pass
                        
                    case "Grassland": obstacles.append((obstacle.rect,obstacle.image))
                        
                    case "Beach / Sand": obstacles.append((obstacle.rect,obstacle.image))
                        
                    case "Forest": obstacles.append((obstacle.rect,obstacle.image))
                        
                    case "Highland / Peak": obstacles.append((obstacle.rect,obstacle.image))
                j-=1
            i+=1
            j=topleft[1]       

        
        
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
    players=[(player.rect,player.image)]
    player.update()
    x=Map(player,(0,0))
    gamemap=x.create_map(player)
    game_display(screen,players,gamemap)
    