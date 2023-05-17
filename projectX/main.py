__author__ = "Ashutosh"
import pygame
from sys import exit
import Game
pygame.init()

#variables
WIDTH = 300
HEIGHT = 500
run = True
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("ProjectX")
#importing images
bg = pygame.image.load("assests/background.jpeg").convert_alpha()
bg_scaled = pygame.transform.scale(bg,(WIDTH,HEIGHT))


font = pygame.font.Font(None,40)
text = font.render("No game", True, (0,0,0))
text_rect = text.get_rect()
text_rect.center = (WIDTH//2,HEIGHT//2)

gui_font = pygame.font.Font(None,40)

class Button:
    def __init__(self, text, width, height, pos):
        self.pressed = False
        #self.elevation = elevation
        #self.dynamic_elevation = elevation

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_rect.center = (width,height)
        self.top_color = '#475F77'

        self.text_surface = gui_font.render(text,True,'#ffffff')
        self.text_rect = self.text_surface.get_rect(center= self.top_rect.center)
    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius=12)
        screen.blit(self.text_surface,self.text_rect)
        self.check_click()
    def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.top_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed= True
                else:
                    if self.pressed== True:
                        self.pressed = False
                    



start_button = Button("start",100,30,(WIDTH//2,HEIGHT//2))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                Game.game()
            
    screen.fill((255,0,0))
    screen.blit(bg_scaled,(0,0))
    #screen.blit(text,text_rect)
    start_button.draw()

    
    pygame.display.update()


