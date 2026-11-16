
def game_display(screen,players,obstacles):
    screen.fill("blue")
    obstacles.draw(screen)
    players.draw(screen)