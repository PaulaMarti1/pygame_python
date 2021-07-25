import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
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
        gf.check_events()
        gf.update_screen(al_settings,screen,ship)
run_game()
