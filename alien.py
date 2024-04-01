import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.settings = Settings()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/Enemy.png')
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, fleet_direction):
        self.x += (self.settings.alien_speed * fleet_direction)
        self.rect.x = self.x