import pygame
import random

class PowerUp:
    def __init__(self, screen):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.active = False
        self.type = None
        self.screen = screen

    def spawn(self):
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(50, 550)
        self.active = True
        self.type = random.choice(['speed', 'size'])

    def deactivate(self):
        self.active = False