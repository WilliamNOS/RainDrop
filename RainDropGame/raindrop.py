import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single drop in the fleet"""

    def __init__(self, rd_game):
        """Initialize the drop and set its starting position"""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the drop image and set its rect attribute
        self.image = pygame.image.load('dropimages/raindrops.png')
        self.rect = self.image.get_rect()

        # Start each new drop near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the drops exact horizontal position
        self.y = float(self.rect.y) 
  
    def update(self):
        """Move the drop to the right"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
    
    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

