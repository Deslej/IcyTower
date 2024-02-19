import pygame
import os

path = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-906144-leap-and-jump-2d-game-kit\Png\Main Characters\Char01\PNG\Jump' )
file_names = sorted(os.listdir(path))
tab=[]
for file_name in file_names:
    tab.append(pygame.transform.scale(pygame.image.load(os.path.join(path, file_name)),(160,150)))

class PLayer():
    def __init__(self, px, py,number_player):
        super().__init__()
        self.sprites=[]
        if number_player==0:
            for i in range(len(tab)):
                self.sprites.append(tab[i])
        if number_player==1:
            for i in range(len(tab2)):
                self.sprites.append(tab2[i])
        if number_player==2:
            for i in range(len(tab3)):
                self.sprites.append(tab3[i])
        if number_player==3:
            for i in range(len(tab3)):
                self.sprites.append(tab3[i])
        self.current_sprites=0
        self.image =self.sprites[self.current_sprites]
        self.width=58
        self.height=74
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center= px, py
        self.movement=8
        self.speed_y=0
        self.lifes=3
        self.flip=False
        self.number_player=number_player

    def _handle_events(self, keys_pressed,WIDTH):

        if keys_pressed[pygame.K_LEFT] and self.rect[0] > 50:
            self.rect.x -= self.movement * 3
            self.flip=False

        if keys_pressed[pygame.K_RIGHT] and self.rect[0] < WIDTH - self.rect.width-50:
            self.rect.x += self.movement * 3
            self.flip=True

    def _collision(self,HEIGHT,platform_group,CLIMB_THRESH):
        dy=0

        self.speed_y+=self.movement-5
        dy+=self.speed_y

        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.speed_y>0:
                        self.rect.bottom = platform.rect.top
                        dy=0
                        self.speed_y= -40
                        self.current_sprites=0

        climb=0
        if self.rect.top <= CLIMB_THRESH:
            if self.speed_y<0:
                climb = -dy
        self.rect.y += dy+climb

        return climb

    def draw(self,screen,life_image):
        if self.current_sprites < len(self.sprites)-1:
            self.current_sprites+=0.2
        self.image = self.sprites[int(self.current_sprites)]
        if self.number_player==0:
            screen.blit(pygame.transform.flip(self.image,self.flip,False), (self.rect.x-50 , self.rect.y-50 ))
            #pygame.draw.rect(screen,(255,255,255),self.rect,2)
        if self.number_player == 3:
            self.height=70
            screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 50, self.rect.y - 40))
            #pygame.draw.rect(screen,(255,255,255),self.rect,2)
        if self.number_player==1 or self.number_player==2 :
            screen.blit(pygame.transform.flip(self.image,self.flip,False), (self.rect.x-50 , self.rect.y-35 ))
            #pygame.draw.rect(screen,(255,255,255),self.rect,2)
        for i in range(self.lifes):
            screen.blit(life_image,(5+25*i,-10))

    def update(self, keys_pressed,WIDTH):
        self._handle_events(keys_pressed,WIDTH)


path2 = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-906144-leap-and-jump-2d-game-kit\Png\Main Characters\Char02\PNG\Jump' )
file_names2 = sorted(os.listdir(path))
tab2=[]
for file_name in file_names2:
    tab2.append(pygame.transform.scale(pygame.image.load(os.path.join(path2, file_name)),(160,150)))
path3 = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-906144-leap-and-jump-2d-game-kit\Png\Main Characters\Char03\PNG\Jump' )
file_names3 = sorted(os.listdir(path))
tab3=[]
for file_name in file_names3:
    tab3.append(pygame.transform.scale(pygame.image.load(os.path.join(path3, file_name)),(160,150)))
path4 = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-906144-leap-and-jump-2d-game-kit\Png\Main Characters\Char04\PNG\Jump' )
file_names4 = sorted(os.listdir(path))
tab4=[]
for file_name in file_names4:
    tab4.append(pygame.transform.scale(pygame.image.load(os.path.join(path4, file_name)),(160,150)))
