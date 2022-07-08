from gamesprites import GameSprite
import pygame


class Bomb(GameSprite):
    # 初始化爆炸
    def __init__(self,center,ishero=False):
        # 加载爆炸资源
        super().__init__('./images/me_destroy_1.png',0)
        self.frame = 0
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 300 #这个值越大，爆炸动画就越长
        # 飞机摧毁图片,以数字形式保存
        self.destory_image = []
        if ishero:
            self.destory_image.extend([
                #pygame.image.load('./images/me_destroy_1.png'),
                pygame.image.load('./images/me_destroy_2.png'),
                pygame.image.load('./images/me_destroy_3.png'),
                pygame.image.load('./images/me_destroy_4.png')
            ])
        else:
            self.destory_image.extend([
                pygame.image.load('./images/enemy1_down1.png'),
                pygame.image.load('./images/enemy1_down2.png'),
                pygame.image.load('./images/enemy1_down3.png'),
                pygame.image.load('./images/enemy1_down4.png')
            ])

    def update(self):
        now = pygame.time.get_ticks() #获取毫秒表示的时间
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.destory_image):
                self.kill()
            else:
                self.image = self.destory_image[self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center