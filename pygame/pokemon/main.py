import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Attack Monster RPG")

# Enemy sprite

enemy_image = pygame.image.load("enemy.jpeg")  # Replace with your enemy sprite
enemy_rect = enemy_image.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))

# Attack button rectangle
attack_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)


def main():
    clock = pygame.time.Clock()

    player_health = 100
    enemy_health = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if attack_button_rect.collidepoint(event.pos):
                    # Player attacks
                    enemy_health -= 10
                    print("You attacked! Enemy health:", enemy_health)

                    # Enemy counter-attacks
                    player_health -= 5
                    print("Enemy counter-attacks! Your health:", player_health)

        # Draw everything
        screen.fill(WHITE)
        screen.blit(enemy_image, enemy_rect)
        pygame.draw.rect(screen, RED, attack_button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Atacar", True, WHITE)
        text_rect = text.get_rect(center=attack_button_rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
