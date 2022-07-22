from demo.config import Parameter
from demo.gameelements import ElementSprite
import os


class Player(ElementSprite):
    def __init__(self):
        super().__init__(os.path.join('images','me1.png'),speed=4)
        #玩家的飞船初始的位置
        self.rect.centerx = Parameter.SCREEN_WIDTH/2
        self.rect.bottom = Parameter.SCREEN_HEIGHT
        self.speed = 4
        self.health = 100
        # 移动状态
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #飞机移动
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
        if self.rect.right >= Parameter.SCREEN_WIDTH:
            self.rect.right -= self.speed
        if self.rect.bottom >= Parameter.SCREEN_HEIGHT:
            self.rect.bottom -= self.speed
        if self.rect.left <= 0:
            self.rect.left += self.speed
        if self.rect.top <= 0:
            self.rect.top += self.speed



