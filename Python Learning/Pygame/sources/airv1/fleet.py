from gamesprites import GameSprite
from configs import Config
import random
import os
import pygame


class Enemy(GameSprite):
    def __init__(self):
        super().__init__(os.path.join('images','enemy1.png'))
        #指定敌机的初始随机速度
        self.speed = random.randint(1,3)
        #指定敌机的初始随机位置
        self.rect.x = random.randint(0,Config.SCREEN_WIDTH-self.rect.width)
        self.rect.bottom = 0
        self.enemies = []
        for i in range(1,3):
            self.enemies.append(os.path.join('images',f'enemy{i}.png'))
        self.image = pygame.image.load(random.choice(self.enemies))
        self.explode_sounds = [
            pygame.mixer.Sound(os.path.join('images','expl0.wav')),
            pygame.mixer.Sound(os.path.join('images','expl1.wav'))
        ]

    # 重写父类的方法update
    def update(self):
        super().update()
        #判断是否飞出屏幕，则从精灵组中删除该飞机
        if self.rect.y >= Config.SCREEN_HEIGHT:
            # 精灵飞出屏幕之后，敌机被销毁
            self.kill()

    def __del__(self):
        #print('飞机被销毁了%s' %self.rect)
        pass
