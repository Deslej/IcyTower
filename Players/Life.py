import pygame
import random
import os
path = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-891167-jump-vertical-game-kit\PNG\Life' )
file_names = sorted(os.listdir(path))
tab=[]
for file_name in file_names:
    tab.append(pygame.transform.scale(pygame.image.load(os.path.join(path, file_name)),(60,60)))

class Life(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.sprites = []
        for i in range(len(tab)):
            self.sprites.append(tab[i])
        self.current_sprite = 0
        self.width=56
        self.height=34
        self.image = self.sprites[self.current_sprite]
        self.rect =pygame.Rect(0,0,self.width,self.height)
        self.rect.center = x, y

    def draw(self,life_group,HEIGHT,screen):
        for l in life_group:
            l.current_sprite+=0.25
            if l.current_sprite>=len(l.sprites):
                l.current_sprite=0
            l.image=l.sprites[int(l.current_sprite)]
            screen.blit(l.image,(l.rect.x-4,l.rect.y-14))
            #pygame.draw.rect(screen,(255,255,255),l.rect,2)
            if l.rect.bottom > HEIGHT:
                l.kill()

    def update(self,climb,life_group,player,Max_Lifes):
        self.rect.y+=climb
        self._collidation(life_group,player,Max_Lifes)

    def _collidation(self,life_group,player,Max_Lifes):
        for life in life_group:
            if life.rect.colliderect(player.rect.x,player.rect.y,player.width,player.height):
                if player.lifes<Max_Lifes:
                    player.lifes+=1
                    life.kill()
                life.kill()

    def _creating_life(self,life_group,Max_Life):
        if len(life_group)<Max_Life:
            life_minmax_x=random.randint(100,600)
            life_minmax_y=random.randint(200,4500)
            life=Life(life_minmax_x,-life_minmax_y)
            life_group.add(life)