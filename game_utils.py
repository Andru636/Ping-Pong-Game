import pygame
import sys

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

def draw_objects(screen, player, opponent, ball, power_up):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player.rect)
    pygame.draw.rect(screen, WHITE, opponent.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)

    if power_up.active:
        color = RED if power_up.type == 'speed' else GREEN
        pygame.draw.rect(screen, color, power_up.rect)

    player_score = font.render(str(player.score), True, WHITE)
    opponent_score = font.render(str(opponent.score), True, WHITE)
    screen.blit(player_score, (200, 20))
    screen.blit(opponent_score, (600, 20))

    pygame.draw.aaline(screen, WHITE, (400, 0), (400, 600))

def check_collision(ball, player, opponent):
    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(opponent.rect):
        ball.bounce('x')

def check_power_up(player, ball, power_up):
    if power_up.active and ball.rect.colliderect(power_up.rect):
        if power_up.type == 'speed':
            player.speed += 2
        elif power_up.type == 'size':
            player.rect.height += 20
        power_up.deactivate()

def reset_power_ups(player):
    player.speed = 5
    player.rect.height = 100

def game_over(screen, winner):
    screen.fill(BLACK)
    text = large_font.render(f"{winner} wins!", True, WHITE)
    screen.blit(text, (200, 300))
    pygame.display.flip()
    pygame.time.wait(3000)

def main_menu(screen):
    while True:
        screen.fill(BLACK)
        title = large_font.render("Пинг-понг", True, WHITE)
        start = font.render("Нажмите ПРОБЕЛ чтобы начать", True, WHITE)
        quit_text = font.render("Нажмите Q чтобы выйти", True, WHITE)
        screen.blit(title, (200, 150))
        screen.blit(start, (200, 300))
        screen.blit(quit_text, (200, 450))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    return False