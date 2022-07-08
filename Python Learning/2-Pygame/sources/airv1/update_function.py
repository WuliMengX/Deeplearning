import random
import sys
import pygame
from background import PlaneBackGround
from configs import Config
from fleet import Enemy
from hero import Hero
from bomb import Bomb
from missiles import Missile


def check_events(hero,enemy_group):
    for event in pygame.event.get():
        # 判断是否是退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == Config.ENEMY_EVENT:
            enemy = Enemy()
            enemy_group.add(enemy)
        if event.type == Config.BOSS_EVENT:
            print('警惕警惕，敌人的首脑飞机出现了！！！')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                hero.moving_down = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True
            elif event.key == pygame.K_RIGHT:
                hero.moving_right = True
            elif event.key == pygame.K_UP:
                hero.moving_up = True
            elif event.key == pygame.K_SPACE:
                if hero.health > 0:
                    missile = Missile()
                    hero.fire(missile) #飞船射击
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero.moving_left = False
            elif event.key == pygame.K_DOWN:
                hero.moving_down = False
            elif event.key == pygame.K_UP:
                hero.moving_up = False


def create_sprites():
    bg1 = PlaneBackGround()
    bg2 = PlaneBackGround(True)
    background_group = pygame.sprite.Group(bg1,bg2)
    # 创建敌机的精灵组
    enemy_group = pygame.sprite.Group()
    # 创建英雄飞机的对象
    hero = Hero()
    hero_group = pygame.sprite.Group(hero)
    bomb_group = pygame.sprite.Group()
    return background_group,enemy_group,hero_group,bomb_group

# 用来检测英雄子弹与敌人飞机的碰撞
def collisions(enemys,missiles,bomb_group):
    hits = pygame.sprite.groupcollide(enemys,missiles,True,True)
    for hit in hits: #hit就是enemy对象
        Config.SCORE += 1
        random.choice(hit.explode_sounds).play(0)
        enemy_bomb = Bomb(hit.rect.center,False)
        bomb_group.add(enemy_bomb)

# 用来检测英雄飞机撞击敌人飞机时候的碰撞
def hero_collisions(hero_group,enemies,bomb_group):
    hits = pygame.sprite.groupcollide(hero_group, enemies, False, True) #撞击就已经被移除了
    for hit in hits:
        hit.health -=  Config.damage
        if hit.health <= 0:
            enemy_bomb = Bomb(hit.rect.center,True)
            bomb_group.add(enemy_bomb)
            hit.kill()
    # hits = pygame.sprite.spritecollide(hero,enemies,True)
    # if len(hits) >0:
    #     Config.SCORE += 1
    #     for hit in hits:
    #         random.choice(hit.explode_sounds).play(0)
    #         enemy_bomb = Bomb(hit.rect.center)
    #         bomb_group.add(enemy_bomb)
    #     hero.health -= Config.damage
    #     if hero.health <= 0:
    #         print('英雄飞机被无情炸毁了')
    #         hero.bomb()
    #         hero.bomb_sound.play(0)
    #         hero.kill()


def draw_text(surf,font_name,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,Config.BLUE) #(R,G,B)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)

def draw_hero_health(surf,hero,hp,x,y):
    if hero.health < 0:
        hp = 0
    bar_length = 100
    bar_height = 10
    fill = (hp/100) * bar_length
    outline_rect = pygame.Rect(x,y,bar_length,bar_height)
    fill_rect = pygame.Rect(x,y,fill,bar_height)
    pygame.draw.rect(surf,(0,255,0),fill_rect) #如果没有第四个参数就会填满
    pygame.draw.rect(surf,(0,0,0),outline_rect,2) #如果有第四个参数就是外框