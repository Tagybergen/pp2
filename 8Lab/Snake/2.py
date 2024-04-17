import pygame
import random
import time

pygame.init()

snake_color = (0, 0, 128)
back_color = (255, 255, 255)
food = (255,0,0)
score_coun = (255,20, 0)


width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 10

font_go = pygame.font.SysFont('ubuntu', 30)
font_score = pygame.font.SysFont('ubuntu', 25)
font_l = pygame.font.SysFont('ubuntu', 25)


def print_score(score):
    text = font_score.render("Score: " + str(score), True, food)
    screen.blit(text, (0, 0))


def print_level(level_snake):
    level = font_l.render("Level: " + str(level_snake), True, food)
    screen.blit(level, (200, 0))


def draw_snake(snake_size, snake_pixels):
    for pixels in snake_pixels:
        pygame.draw.rect(screen, snake_color, (pixels[0], pixels[1], snake_size, snake_size))


def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10) * 10
    food_y = round(random.randrange(0, height - snake_size) / 10) * 10

    count = 0
    level_snake = 0

    snake_speed = 10

    while not game_over:
        while game_close:
            screen.fill(back_color)
            game_over_message = font_go.render("Game Over!", True, score_coun)
            screen.blit(game_over_message, (width / 3, height / 3))
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        screen.fill(back_color)
        pygame.draw.rect(screen, food, (food_x, food_y, snake_size, snake_size))

        snake_pixels.append((x, y))

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == (x, y):
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        print_level(level_snake)

        if count == 3:
            level_snake += 1
            # print_level(level_snake)
            snake_speed += 2
            count = 0

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(
                random.randrange(0, width - snake_size) / 10) * 10
            food_y = round(random.randrange(0, height - snake_size) / 10) * 10
            snake_length += 1
            count += 1

        clock.tick(snake_speed)

    pygame.quit()


run_game()