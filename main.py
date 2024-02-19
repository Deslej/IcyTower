import random
import time

from Enemies import Enemy_bat,Enemy_crab
from Players import Gracz,Life,Platform
from Menu import Button,Text,Select_player

import pygame
import os

pygame.init()
pygame.mixer.init()

SCREENSIZE = WIDTH, HEIGHT = 700 , 800
CLIMB_THRESH=200
climb=0
bg_climb=0
Max_Lifes=5
Max_Life=1
Score=0
Max_Bats=1
select=0
select_background=0
tab_players=[]
tab_background=[]
tab_background_walls=[]
tab_platform_first=[]
tab_platform_wider=[]
tab_platform=[]

screen= pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('Icy Tower')
clock= pygame.time.Clock()

player_image=pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/Char1Select.png').convert_alpha()
player2_image=pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/Char2Select.png').convert_alpha()
player3_image=pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/Char4Select.png').convert_alpha()
player4_image=pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/Char5Select.png').convert_alpha()

background_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/01/Layer1.png').convert(),(WIDTH,HEIGHT))
background2_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/02/Layer1.png').convert(),(WIDTH,HEIGHT))
background3_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/03/Layer1.png').convert(),(WIDTH,HEIGHT))
background4_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/04/Layer1.png').convert(),(WIDTH,HEIGHT))
background_walls_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/01/Layer3.png').convert_alpha(),(WIDTH,HEIGHT))
background2_walls_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/02/Layer3.png').convert_alpha(),(WIDTH,HEIGHT))
background3_walls_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/03/Layer2.png').convert_alpha(),(WIDTH,HEIGHT))
background4_walls_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/Background/06/Layer2.png').convert_alpha(),(WIDTH,HEIGHT))
platform_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer1.png').convert_alpha(),(100,30))
platform_wider_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer1.png').convert_alpha(),(200,30))
first_platform_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer1.png').convert_alpha(),(620,30))
platform2_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer2.png').convert_alpha(),(100,30))
platform_wider2_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer2.png').convert_alpha(),(200,30))
first_platform2_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer2.png').convert_alpha(),(620,30))
platform3_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer3.png').convert_alpha(),(100,30))
platform_wider3_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer3.png').convert_alpha(),(200,30))
first_platform3_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer3.png').convert_alpha(),(620,30))
platform4_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer6.png').convert_alpha(),(100,30))
platform_wider4_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer6.png').convert_alpha(),(200,30))
first_platform4_image=pygame.transform.scale(pygame.image.load
                                        ('craftpix-891167-jump-vertical-game-kit/PNG/OtherAssets/Platformer6.png').convert_alpha(),(620,30))

life_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Life/1.png').convert_alpha(),(60,60))
menu_button_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/menuBtn.png').convert_alpha(),(100,100))
accept_button_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/YesBtn.png').convert_alpha(),(100,100))
play_button_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/PlayBtn.png').convert_alpha(),(100,100))
select_player_button_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/CharactersBtn.png').convert_alpha(),(90,90))
napis_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/BigLogo.png').convert_alpha(),(400,400))
score_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/ScoreBox.png').convert_alpha(),(150,40))
high_score_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/HighScore.png').convert_alpha(),(150,70))
tlo_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/Background.png').convert_alpha(),(WIDTH,HEIGHT))
select_player_background_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/Background3.png').convert_alpha(),(WIDTH,HEIGHT))
move_select_player_image=pygame.transform.scale(pygame.image.load('craftpix-891167-jump-vertical-game-kit/PNG/Ui/RightArrow.png').convert_alpha(),(100,50))
stop_button_image=pygame.transform.scale(pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/PausBtn.png').convert_alpha(),(40,40))
pause_box_image=pygame.transform.scale(pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/PausedBox.png').convert_alpha(),(300,300))
close_button_image=pygame.transform.scale(pygame.image.load('craftpix-906144-leap-and-jump-2d-game-kit/Png/User Interfaces/CloseBtn.png'),(90,90))

def infinity_background(image,bg_climb):
    screen.blit(image,(0,0+bg_climb))
    screen.blit(image,(0,-800+bg_climb))

def menu():
    screen.blit(tlo_image,(0,0))
    screen.blit(napis_image,(150,-50))
    screen.blit(high_score_image,(20,HEIGHT-150))
    f = open("HighScore.txt", "r")
    High_score = f.read()
    High_score_text = Text.Text(f"{High_score}", (0, 0, 0), 100, HEIGHT -60, None,
                           45)
    High_score_text.draw(screen)
    f.close()
    return High_score

def end_menu(High_score,Score,tlo):
    screen.blit(tlo, (0, 0))
    if Score > int(High_score):
        High_score = Score
        f = open("HighScore.txt", "w")
        f.write(str(High_score))
        f.close()
    score_box(Score,WIDTH//2-75,HEIGHT//2-200)
    Game_Over_text = Text.Text("Game Over", (0, 0, 0), WIDTH // 2, 100,None,80)
    Game_Over_text.draw(screen)

def score_box(Score,width,height):
    screen.blit(score_image,(width,height))
    Score_text = Text.Text(f"{Score}", (0, 0, 0), width+80, height+25, None, 30)
    Score_text.update()
    Score_text.draw(screen)

def chosen_player(i,tab,scale):
    if i == 0:
        select = tab[i].draw(screen,scale)
    if i == 1:
        select = tab[i].draw(screen,scale)
    if i == 2:
        select = tab[i].draw(screen,scale)
    if i == 3:
        select = tab[i].draw(screen,scale)
    return select

def create_select_tab(tab,WIDTH,HEIGHT,image1,image2,image3,image4):
    tab.append(Select_player.Select_player(WIDTH, HEIGHT, image1))
    tab.append(Select_player.Select_player(WIDTH, HEIGHT, image2))
    tab.append(Select_player.Select_player(WIDTH, HEIGHT, image3))
    tab.append(Select_player.Select_player(WIDTH, HEIGHT, image4))

window_open=True
menu_open=False
end_game=False
select_player_open=False
pause=False
window_menu=True

button_start = Button.Button(WIDTH//2,HEIGHT//2-10,play_button_image)
button_menu=Button.Button(WIDTH//2,HEIGHT-200,menu_button_image)
accept_button=Button.Button(WIDTH//2-50,HEIGHT-150,accept_button_image)
button_select_player=Button.Button(WIDTH//2,HEIGHT//2+140,select_player_button_image)
button_move_select_player=Button.Button(WIDTH-200,HEIGHT//2-140,move_select_player_image)
button_move_select_background=Button.Button(WIDTH-200,HEIGHT//2-20,move_select_player_image)
button_move_select_platforms=Button.Button(WIDTH-200,HEIGHT//2+90,move_select_player_image)
button_stop=Button.Button(WIDTH//2,30,stop_button_image)
close_button=Button.Button(WIDTH//2,HEIGHT//2-60,close_button_image)

while window_open:

    pygame.mixer.music.load('Background music DOWNLOAD (125).wav')
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)
    window_menu=True

    while window_menu:

        High_score=menu()

        if button_select_player.draw(screen):
            i=0
            j=0
            k=0
            select_player_open=True
            screen.blit(select_player_background_image, (0, 0))
            create_select_tab(tab_players,WIDTH // 2+15,HEIGHT // 2-80,player_image,player2_image,player3_image,player4_image)
            create_select_tab(tab_background_walls,WIDTH//2+300,HEIGHT//2+330,background_walls_image,background2_walls_image,
                              background3_walls_image,background4_walls_image)
            create_select_tab(tab_background,WIDTH//2+300,HEIGHT// 2+330,background_image,background2_image,background3_image,
                              background4_image)
            create_select_tab(tab_platform, WIDTH // 2 , HEIGHT // 2+50, platform_image, platform2_image, platform3_image,
                              platform4_image)
            create_select_tab(tab_platform_first, WIDTH // 2 , HEIGHT // 2, first_platform_image,first_platform2_image,
                              first_platform3_image,first_platform4_image)
            create_select_tab(tab_platform_wider, WIDTH // 2, HEIGHT // 2 , platform_wider_image, platform_wider2_image,
                              platform_wider3_image,platform_wider4_image)

            while select_player_open:

                accept_button.change_position(WIDTH//2-50,HEIGHT-150)
                screen.blit(select_player_background_image, (0, 0))

                if button_move_select_player.draw(screen):
                    i=i+1

                if i>3:
                    i=0

                if button_move_select_background.draw(screen):
                    j=j+1

                if j>3:
                    j=0

                if button_move_select_platforms.draw(screen):
                    k=k+1

                if k>3:
                    k=0

                select_background = chosen_player(j, tab_background,0.8)
                select_background_walls=chosen_player(j,tab_background_walls,0.8)
                chosen_player(i,tab_players,1)
                select=i
                select_platform_wider=tab_platform_wider[k].image
                select_platform=chosen_player(k,tab_platform,0.8)
                select_first_platform=tab_platform_first[k].image

                if accept_button.draw(screen):
                    select_player_open=False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        select_player_open = False
                        window_open = False
                        window_menu=False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            select_player_open = False

                pygame.display.update()

        if button_start.draw(screen):

            menu_open = True
            end_game = True

            if select_background==0:

                select_background=background_image
                select_background_walls=background_walls_image
                select_platform=platform_image
                select_platform_wider=platform_wider_image
                select_first_platform=first_platform_image

            player = Gracz.PLayer(WIDTH // 2-100, HEIGHT-200,select)

            platform_group = pygame.sprite.Group()
            first_platform = Platform.Platform(340, HEIGHT - 100, select_first_platform)
            platform_group.add(first_platform)

            bat = Enemy_bat.Enemy_Bat(150, 300)
            bat_group = pygame.sprite.Group()

            life_group = pygame.sprite.Group()
            life = Life.Life(0, 0)

            crab =Enemy_crab.Enemy_crab(0, HEIGHT)
            crab_group = pygame.sprite.Group()
            crab_group.add(crab)

            for i in range(10):
                platform_y = i * 150 - 750
                platform_x = random.randint(130, WIDTH - 130)
                if platform_y < HEIGHT - 50:
                    platform = Platform.Platform(platform_x, platform_y, select_platform)
                    platform_group.add(platform)

            pygame.mixer.music.load('Renegade-X-I-Was-Never-There.mp3')
            pygame.mixer.music.set_volume(0)
            pygame.mixer.music.play(-1)

            while menu_open:

                if player.rect.bottom < HEIGHT - 30 and player.lifes != 0:
                    clock.tick(30)
                    keys_pressed = pygame.key.get_pressed()
                    Score+=climb
                    climb = player._collision(HEIGHT,platform_group,CLIMB_THRESH)
                    player.update(keys_pressed, WIDTH)

                    bg_climb += climb
                    platform._create_infinity_platforms(bg_climb,HEIGHT,select_platform_wider,WIDTH,platform_group)

                    if bg_climb >= 800:
                        bg_climb = 0

                    infinity_background(select_background, bg_climb)
                    infinity_background(select_background_walls, bg_climb)
                    player.draw(screen,life_image)
                    platform_group.update(climb)
                    platform.draw(platform_group,screen,player,HEIGHT,crab_group,crab)

                    bat._creating_bats(bat_group,Max_Bats)
                    bat_group.update(climb,bat_group,player)
                    bat.draw(bat_group,screen,HEIGHT,WIDTH,platform_group)

                    life._creating_life(life_group,Max_Life)
                    life_group.update(climb,life_group,player,Max_Lifes)
                    life.draw(life_group,HEIGHT,screen)

                    if Score >1000 and Score <2000:
                        Max_Bats = 2
                    elif Score >=2000 and Score < 3500:
                        Max_Bats = 3
                        Max_Life = 2
                    elif Score >=3500 and Score <6000:
                        Max_Bats = 3
                        Max_Life = 2
                        crab_group.update(climb, crab_group, player, platform_group)
                        crab.draw(crab_group, HEIGHT, screen)
                    elif Score >=6000 and Score <10000:
                        Max_Bats = 5
                        Max_Life = 3
                        crab_group.update(climb, crab_group, player, platform_group)
                        crab.draw(crab_group, HEIGHT, screen)
                        for p in platform_group:
                            if p.number != 4 and p.number % 3 == 0:
                                p._moving(WIDTH)
                    elif Score>10000:
                        Max_Bats=7
                        Max_Life = 4
                        crab_group.update(climb, crab_group, player, platform_group)
                        crab.draw(crab_group, HEIGHT, screen)
                        for p in platform_group:
                            if p.number != 4:
                                p._moving(WIDTH)

                    score_box(Score, WIDTH - 175, 5)

                    if button_stop.draw(screen):
                        pause=True
                        pygame.mixer.music.load('Background music DOWNLOAD (125).wav')
                        pygame.mixer.music.set_volume(0)
                        pygame.mixer.music.play(-1)
                        while pause:
                            screen.blit(pause_box_image,(WIDTH//2-150,HEIGHT//2-150))
                            if close_button.draw(screen):
                                pause=False
                            button_menu.change_position(WIDTH//2-50,HEIGHT//2)
                            if button_menu.draw(screen):
                                climb = 0
                                bg_climb = 0
                                Max_Life = 1
                                Score = 0
                                Max_Bats = 1
                                select = 0
                                select_background = 0
                                end_game = False
                                menu_open = False
                                select_player_open = False
                                pause=False
                                window_menu=False
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    end_game = False
                                    menu_open = False
                                    window_open = False
                                    pause=False
                                    window_menu=False
                            pygame.display.update()
                else:
                    pygame.mixer.music.load('mixkit-arcade-game-over-1949.wav')
                    pygame.mixer.music.set_volume(0)
                    pygame.mixer.music.play(-1)
                    while end_game:
                        end_menu(High_score,Score,select_background)
                        if button_menu.draw(screen):
                            climb = 0
                            bg_climb = 0
                            Max_Life = 1
                            Score = 0
                            Max_Bats = 1
                            select = 0
                            select_background = 0
                            end_game = False
                            menu_open = False
                            select_player_open=False
                            window_menu=False

                            time.sleep(0.3)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                end_game = False
                                menu_open=False
                                window_open=False
                                window_menu=False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    climb = 0
                                    bg_climb = 0
                                    Max_Life = 1
                                    Score = 0
                                    Max_Bats = 1
                                    select = 0
                                    select_background = 0
                                    end_game = False
                                    menu_open=False
                                    select_player_open=False

                        pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        menu_open = False
                        window_open=False
                        window_menu=False

                pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_menu = False
                window_open = False
                window_menu=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        pygame.display.update()


pygame.quit()