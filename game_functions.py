import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(al_settings, screen, ship):
    #Update image on the screen and flip to the new screen
    screen.fill(al_settings.bg_color)
    ship.blitme()

    #Make the most recently drawn screen visible
    pygame.display.flip()
