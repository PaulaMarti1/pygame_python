import pygame
class Ship():
    def __init__(self,screen):
        self.screen = screen

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/rocket.bmp') # loading the image
        self.rect = self.image.get_rect() #pygame treats image as a rectangle
        self.screen_rect = screen.get_rect() # screen is rectange too

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
