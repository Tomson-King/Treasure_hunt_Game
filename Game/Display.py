def draw(screen,sprite):
    for i in sprite:
        screen.blit(i[1],i[0])




def game_display(screen,players,obstacles):
    screen.fill("blue")
    draw(screen,obstacles)
    draw(screen,players)