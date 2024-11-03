import pygame
import sys
from paddle import Paddle
from ball import Ball
from power_up import PowerUp
from game_utils import draw_objects, check_collision, check_power_up, reset_power_ups, game_over, main_menu

# Константы
WIDTH = 800
HEIGHT = 600
PADDLE_HEIGHT = 100
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")
clock = pygame.time.Clock()

def main():
    if not main_menu(screen):
        return

    player = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, screen)
    opponent = Paddle(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, screen)
    ball = Ball(screen)
    power_up = PowerUp(screen)

    power_up_timer = 0
    power_up_interval = 10 * FPS  # 10 секунд

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(True)
        if keys[pygame.K_DOWN]:
            player.move(False)

        opponent.ai_move(ball)
        ball.move()
        check_collision(ball, player, opponent)
        check_power_up(player, ball, power_up)

        # Проверка границ экрана и управление появлением улучшений
        if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
            ball.bounce('y')

        if ball.rect.left <= 0:
            opponent.score += 1
            ball.reset()
            reset_power_ups(player)
        elif ball.rect.right >= WIDTH:
            player.score += 1
            ball.reset()
            reset_power_ups(player)

        power_up_timer += 1
        if power_up_timer >= power_up_interval and not power_up.active:
            power_up.spawn()
            power_up_timer = 0

        draw_objects(screen, player, opponent, ball, power_up)
        pygame.display.flip()
        clock.tick(FPS)

        if player.score >= 10:
            game_over(screen, "Player")
            running = False
        elif opponent.score >= 10:
            game_over(screen, "Opponent")
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()