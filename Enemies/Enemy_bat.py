import pygame
import random
import os

path = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-891167-jump-vertical-game-kit\PNG\Enemies\Bat' )
file_names = sorted(os.listdir(path))
tab=[]
for file_name in file_names:
    tab.append(pygame.transform.scale(pygame.image.load(os.path.join(path, file_name)),(100,55)))

class Enemy_Bat(pygame.sprite.Sprite):

    def __init__(self,Ex,Ey):
        super().__init__()
        self.sprites=[]
        for i in range(len(tab)):
            self.sprites.append(tab[i])
        self.current_sprite=0
        self.image = self.sprites[self.current_sprite]
        self.width=61
        self.height=26
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = Ex, Ey
        self.movement=random.randint(2,6)
        self.direction=1

    def _movement(self,WIDTH,platform_group):
        self.rect.x+= self.movement * self.direction
        if self.rect.x<= 0:
            self.rect.x= 0
            self.direction = 1
            for i in range(4):
                self.sprites[i]=pygame.transform.flip(self.sprites[i],True,False)
        elif self.rect.x >= WIDTH - self.width:
            self.rect.x = WIDTH - self.width
            self.direction = -1
            for i in range(4):
                self.sprites[i] = pygame.transform.flip(self.sprites[i], True, False)

    def draw(self,bat_group,screen,HEIGHT,WIDTH,platform_group):
        for b in bat_group:
            b.current_sprite+=0.2
            if b.current_sprite>=len(b.sprites):
                b.current_sprite=0
            b.image=b.sprites[int(b.current_sprite)]
            screen.blit(b.image,(b.rect.x-18,b.rect.y-15))
            #pygame.draw.rect(screen,(255,255,255),b.rect,2)
            if b.rect.bottom > HEIGHT:
                b.kill()
            b._movement(WIDTH,platform_group)

    def update(self,climb,bat_group,player):
        self.rect.y += climb
        self._collidation(bat_group,player)

    def _creating_bats(self,bat_group,Max_Bats):
        if len(bat_group)<Max_Bats:
            bat_minmax_x=random.randint(100,600)
            bat_minmax_y=random.randint(400,3000)
            bat=Enemy_Bat(bat_minmax_x,-bat_minmax_y)
            bat_group.add(bat)

    def _collidation(self,bat_group,player):
        for bat in bat_group:
            if bat.rect.colliderect(player.rect.x,player.rect.y,player.width,player.height):
                player.lifes-=1
                bat.kill()