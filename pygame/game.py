import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()

# Circle position and velocity
circle_x = 400
circle_y = 300
circle_velocity = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for keydown events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= circle_velocity
    if keys[pygame.K_RIGHT]:
        circle_x += circle_velocity
    if keys[pygame.K_UP]:
        circle_y -= circle_velocity
    if keys[pygame.K_DOWN]:
        circle_y += circle_velocity

    # Reverse direction if circle reaches screen edges
    if circle_x <= 0 or circle_x >= 800:
        circle_velocity *= -1
    if circle_y <= 0 or circle_y >= 600:
        circle_velocity *= -1

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the circle on the screen
    pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 50)

    pygame.display.update()
    clock.tick(60)