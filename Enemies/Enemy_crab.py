import pygame
import os

path = os.path.join(os.pardir,'D:\PyCharm Community Edition 2022.3\Icy Tower\craftpix-906144-leap-and-jump-2d-game-kit\Png\Enemy Characters\En14\PNG\Walk' )
file_names = sorted(os.listdir(path))
tab=[]
for file_name in file_names:
    tab.append(pygame.transform.scale(pygame.image.load(os.path.join(path, file_name)),(100,150)))

class Enemy_crab(pygame.sprite.Sprite):
    def __init__(self, Ex, Ey):
        super().__init__()
        self.sprites = []
        for i in range(len(tab)):
            self.sprites.append(tab[i])
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.width = 38
        self.height = 40
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = Ex, Ey
        self.movement = 2
        self.direction = 1
        self.flip=False

    def draw(self,crab_group,HEIGHT,screen):
        for c in crab_group:
            c.current_sprite+=0.5
            if c.current_sprite>=len(c.sprites):
                c.current_sprite=0
            c.image=c.sprites[int(c.current_sprite)]
            screen.blit(pygame.transform.flip(c.image,c.flip,False),(c.rect.x-30,c.rect.y-85))
            if c.rect.bottom > HEIGHT:
                c.kill()

    def update(self,climb,crab_group,player,platform_group):
        self.rect.y += climb
        self._collidation(crab_group,player)
        self._movement(platform_group)

    def _movement(self,platform_group):
            for platform in platform_group:
                if self.rect.colliderect(platform.rect.x, platform.rect.y, platform.width-self.width, platform.height):
                    self.rect.x += self.movement * self.direction
                    if self.rect.x+self.width>= platform.rect.right:
                        self.rect.x=platform.rect.right-self.width
                        self.flip=True
                        self.direction=-1
                        self.rect.x += self.movement * self.direction
                    elif self.rect.x<=platform.rect.left:
                        self.flip=False
                        self.rect.x=platform.rect.left
                        self.direction=1

    def _creating_crabs(self,top,left,crab_group):
            if len(crab_group)<1:
                    crab_x=left
                    crab_y=top
                    crab = Enemy_crab(crab_x + self.width // 2, crab_y-10)
                    crab_group.add(crab)

    def _collidation(self,crab_group,player):
        for crab in crab_group:
            if crab.rect.colliderect(player.rect.x, player.rect.y, player.width, player.height):
                player.lifes -= 1
                crab.kill()
