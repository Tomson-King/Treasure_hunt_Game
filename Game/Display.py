class Display():
    def __init__(self,screen,sprites):
        screen.fill("blue")
        for sprite in sprites:
            self.draw(screen,sprite)
    def draw(self,screen,sprite):
        for i in sprite:
            screen.blit(i[0],i[1])

    