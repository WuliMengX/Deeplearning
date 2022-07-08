import pygame.sprite
from gamesprites import GameSprite
from configs import Config
from bomb import Bomb
import random
import os


class Hero(GameSprite):
    def __init__(self):
        super().__init__(os.path.join('images','me1.png'),4)
        self.switchimage = 3
        #玩家的飞船初始的位置
        self.rect.centerx = Config.SCREEN_WIDTH/2
        self.rect.bottom = Config.SCREEN_HEIGHT

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #创建子弹组
        self.missiles = pygame.sprite.Group()

        # 子弹射击音效
        self.shoot_sound = pygame.mixer.Sound(os.path.join('images', 'shoot.wav'))

        # 英雄飞机被炸毁音效
        self.bomb_sound = pygame.mixer.Sound(os.path.join('images', 'rumble.ogg'))

        # 创建爆炸组
        self.bombs = pygame.sprite.Group()
        self.health = 100

    def update(self):

        # 英雄图片大变装
        if self.switchimage == random.randint(1,5):
            self.image = pygame.image.load(os.path.join('images','me2.png'))# 不同的系统里不会因为路径错误
        else:
            self.image = pygame.image.load(os.path.join('images','me1.png'))
        if self.moving_right:
            self.rect.right += self.speed
        elif self.moving_left:
            self.rect.left -= self.speed
        elif self.moving_up:
            self.rect.top -= self.speed
        elif self.moving_down:
            self.rect.bottom += self.speed
        self.__crossscreen()

    # 防止玩家飞机越界
    def __crossscreen(self):
        if self.rect.right >= Config.SCREEN_WIDTH:
            self.rect.right -= self.speed
        if self.rect.bottom > Config.SCREEN_HEIGHT:
            self.rect.bottom -= self.speed
        if self.rect.left < 0:
            self.rect.left += self.speed
        if self.rect.top < 0:
            self.rect.top += self.speed

    def fire(self,missile):
        #设置子弹位置
        if self.health > 0:
            missile.rect.bottom = self.rect.top
            missile.rect.centerx = self.rect.centerx
            #将子弹添加到精灵组
            self.missiles.add(missile)
            self.shoot_sound.play(0)

    def bomb(self):
        #创建子弹
        print('爆炸产生')
        bomb = Bomb(self.rect.center)
        #将子弹添加到精灵组
        self.bombs.add(bomb)



    def __del__(self):
        print('hero确实被销毁了')