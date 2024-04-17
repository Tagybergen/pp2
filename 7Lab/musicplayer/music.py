import pygame
import os

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music Player')

music_files = [os.path.join("C:\\Users\\acer\\Desktop\\pp2\\7Lab\\musicplayer\\mymusic", f) for f in os.listdir("C:\\Users\\acer\\Desktop\\pp2\\7Lab\\musicplayer\\mymusic") if f.endswith('.mp3')]
current_track = 0
paused = False
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
                paused = False

            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
                paused = False

            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
                current_track = 0
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play(-1)
                paused = False

    screen.fill((255, 255, 255))
    font = pygame.font.SysFont(music_files, 30)
    filename = os.path.basename(music_files[current_track])
    filename_without_mp3 = os.path.splitext(filename)[0]
    text = font.render(filename_without_mp3, True, (128, 0, 128))
    screen.blit(text, (50, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
