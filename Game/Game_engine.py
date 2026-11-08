import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    # major atributes
    # player (x,y)
    def __init__(self,screen):
        super().__init__()
        self.image=None
        self.rect=self.image.get_rect()
        self.rect.midbottom=(screen.get_width//2,screen.get_height//2)
        self.pos=(0,0)
    def update():
        pass



class Obstacles(pygame.sprite.Sprite):
    # should update based on player coords
    
    def __init__(self):
        super().__init__()
        self.grid=100
    def update(self):
        pass



class Chest(pygame.sprite.Sprite):
    def __init__():
        super().__init__()
    def update():
        pass


def start_game():
    pass


def continue_game():
    pass

