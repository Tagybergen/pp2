import pygame
import sys
pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("red ball game")

white = (255, 255, 255)
red = (255, 0, 0)
ball_size = 70
b_radius = ball_size // 2

ball_x = (screen_width - ball_size) // 2
ball_y = (screen_height - ball_size) // 2
b_speed = 20

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y -= b_speed
    elif keys[pygame.K_DOWN]:
        ball_y += b_speed
    elif keys[pygame.K_LEFT]:
        ball_x -= b_speed
    elif keys[pygame.K_RIGHT]:
        ball_x += b_speed

    ball_x = max(0, min(screen_width - ball_size, ball_x))
    ball_y = max(0, min(screen_height - ball_size, ball_y))

    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x + b_radius, ball_y + b_radius), b_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()