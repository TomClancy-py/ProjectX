import pygame
from sys import exit

def game():
    WIDTH = 300
    HEIGHT = 500
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    font = pygame.font.Font(None,40)
    headline = font.render("Coming soon!!",True,(0,0,0))
    headline_rect = headline.get_rect()
    headline_rect.center = (WIDTH//2,HEIGHT//2)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        screen.fill((255,255,255))
        screen.blit(headline,headline_rect)
        pygame.display.update()
        