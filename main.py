import sys
import pygame
from setting import Settings
from ship import Ship

def run_game():
    #inicializacja pygame
    pygame.init()
    al_settings = Settings()
    #ustawienie szerokości i wysokości okna
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    #tekst, który wyśwteila się jako tytuł gry
    pygame.display.set_caption("Alien Invasion!")
    #ustawienie koloru tła
    bg_color = (al_settings.bg_color)
    # wstawiam shipa
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()
