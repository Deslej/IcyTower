import pygame
class Select_player(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=x,y

    def draw(self,screen,scale):
        screen.blit(pygame.transform.scale(self.image,(100*scale,100*scale)),self.rect)
        return self.image