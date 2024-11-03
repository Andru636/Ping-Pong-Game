import pygame

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

class Paddle:
    def __init__(self, x, y, screen):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.screen = screen
        self.speed = 5
        self.score = 0

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        self.rect.clamp_ip(self.screen.get_rect())

    def ai_move(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.move(False)
        elif self.rect.centery > ball.rect.centery:
            self.move(True)