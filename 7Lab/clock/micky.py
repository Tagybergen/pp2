import pygame
import time
import sys
pygame.init()
size = (800, 600)

screen = pygame.display.set_mode(size)
back = pygame.image.load("back.jpg")
seconds = pygame.image.load("seconds.png")
minutes = pygame.image.load("minutes.png")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(back,(0,0))
    now = time.localtime()

    m_angle = 360 - (now.tm_min * 6)
    min_rotate = pygame.transform.rotate(minutes, m_angle)
    min_pos = ((size[0] - min_rotate.get_width())/2, (size[1] - min_rotate.get_width())/2)
    screen.blit(min_rotate, min_pos)

    s_angle = 360 - (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, s_angle)
    sec_pos = ((size[0] - sec_rotate.get_width())/2, (size[1] - sec_rotate.get_width())/2)
    screen.blit(sec_rotate, sec_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()