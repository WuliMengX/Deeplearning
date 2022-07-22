import pygame


class Parameter():
    # Config类里定义的是游戏中所有需要使用到的常量
    # 常量在python当中是需要大写的
    TITLE = '飞机大战'
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 700
    FRAME = 60  # 刷新的帧率设置为60帧
    ENEMY_EVENT = pygame.USEREVENT #创建敌机的事件
    SCORE_EVENT = pygame.USEREVENT + 1
    SCORE = 0
    BLUE = (0,0,255)
    FONT = 'arial'
    DAMAGE = 50
