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
    
    def __init__(self,player,coords):
        super().__init__()
        self.grid=100
        center = self.get_center(player)
        topleft=(center[0]+int(((screen_x/2)+self.grid)//self.grid),center[1]+int(((screen_y/2)+self.grid)//self.grid))
        center_pos = (((player.x%self.grid)*(-1 if player.x<0 else 1))+screen_x//2,((player.y%self.grid)*(-1 if player.x<0 else 1))+screen_y//2)
        self.pos = (int((center[0]-coords[0])*self.grid+center_pos[0]),int((center[1]-coords[1])*self.grid+center_pos[1]))
        
        self.image= pygame.Surface((100,100))
        if(coords[0]%2==0 and coords[1]%2==0):   
            self.image.fill("green")
        else:
            self.image.fill("blue")
                
            
                
        self.rect = self.image.get_rect()
        self.rect.center=self.pos
        


    
    
    def get_center(self,player):
        center=(int((((0+player.pos[0])-self.grid/2)//self.grid)+1),int((((0+player.pos[1])-self.grid/2)//self.grid)+1))
        return center

    def create_map(self,player):
        center = self.get_center(player)
        topleft=(center[0]+int(((screen_x/2)+self.grid)//self.grid),center[1]+int(((screen_y/2)+self.grid)//self.grid))
        obstacles=pygame.sprite.Group()
        obstacles.empty()
        i,j=topleft
        
        
        while(True):
            while(True):
                if(j==-100): exit()
                obstacle=Obstacles(player,(i,j))
                
                if (obstacle.pos[1]< -1*(obstacle.grid) or obstacle.pos[1]> (screen_y+obstacle.grid)):
                    
                    break
                else:
                    obstacles.add(obstacle)
                j-=1
            i-=1
            j=topleft[1]       

            if (obstacle.pos[0]< -1*(obstacle.grid) or obstacle.pos[0]> (screen_x+obstacle.grid)):
                break
        
        
        return obstacles
        
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
    obstacle=Obstacles(player,(0,0))
    obstacles=obstacle.create_map(player)
    game_display(screen,players,obstacles)
    