import pygame
from Menu import Select_player
class Button(Select_player.Select_player):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.clicked=False

    def draw(self,screen):
        click=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
            click=True
            self.clicked=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        screen.blit(self.image,self.rect)
        return click

    def change_position(self,width,height):
        self.rect.x=width
        self.rect.y=height
