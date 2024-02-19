import pygame
import random
from Menu import Select_player
class Platform(Select_player.Select_player):
    def __init__(self,x,y,image):
        super().__init__(x,y,image)
        self.direction=random.choice([-1,1])
        self.movement=random.randint(1,6)
        self.number=0
        self.width=0
        self.height=0

    def draw(self,platform_group,screen,player,HEIGHT,crab_group,crab):
        for p in platform_group:
            screen.blit(p.image,(p.rect.x-3,p.rect.y))
            if p.number==4 and (player.rect.top-p.rect.top>150):
                (crab._creating_crabs(p.rect.top,p.rect.left,crab_group))
            if p.rect.bottom > HEIGHT:
                p.kill()

    def update(self,climb):
        self.rect.y += climb

    def _create_infinity_platforms(self,bg_climb,HEIGHT,platform_wider_image,WIDTH,platform_group):
        if bg_climb >= 800:
            for i in range(5):
                if i==4:
                    platform_y = i * 150 - 750
                    platform_x = random.randint(180, WIDTH - 180)
                    if platform_y < HEIGHT - 50:
                        platform = Platform(platform_x, platform_y, platform_wider_image)
                        platform.width = 200
                        platform.height = 30
                        platform_group.add(platform)
                        platform.number=i
                else:
                    platform_y = i * 150 - 750
                    platform_x = random.randint(130, WIDTH - 130)
                    if platform_y < HEIGHT - 50:
                        platform = Platform(platform_x, platform_y, self.image)
                        platform.width = 100
                        platform.height = 30
                        platform_group.add(platform)
                        platform.number=i

    def _moving(self,WIDTH):
        self.rect.x += self.movement * self.direction
        if self.rect.x <= 150:
            self.rect.x = 150
            self.direction = 1
        elif self.rect.x >= WIDTH - 150:
            self.rect.x = WIDTH - 150
            self.direction = -1