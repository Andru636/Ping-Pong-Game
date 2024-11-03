import pygame
import random

BALL_RADIUS = 10
WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.screen = screen
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])
        self.speed_increase = 0.1

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def bounce(self, axis):
        if axis == 'x':
            self.dx *= -1
        elif axis == 'y':
            self.dy *= -1
        self.dx *= 1 + self.speed_increase
        self.dy *= 1 + self.speed_increase

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])