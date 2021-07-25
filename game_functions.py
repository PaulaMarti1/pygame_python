import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(al_settings, screen, ship):
    #Update image on the screen and flip to the new screen
    screen.fill(al_settings.bg_color)
    ship.blitme()

    #Make the most recently drawn screen visible
    pygame.display.flip()
