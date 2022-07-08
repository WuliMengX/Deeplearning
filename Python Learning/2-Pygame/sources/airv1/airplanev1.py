from update_function import *
import os


class PlaneGame:

    def __init__(self): #初始化这个类别中的属性
        pygame.init()
        #创建游戏窗口
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        # 设置游戏标题
        pygame.display.set_caption(Config.TITLE)
        # 设置分数的字体
        self.font_name = pygame.font.match_font(Config.font)
        # 设置背景音乐
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join('images','1761.wav'))
        pygame.mixer.music.play(-1)

        #创建游戏时钟
        self.clock = pygame.time.Clock()
        #设置定时事件，创建敌机 1s
        pygame.time.set_timer(Config.ENEMY_EVENT,1000)
        #设置定时事件，创建大boss 5s
        pygame.time.set_timer(Config.BOSS_EVENT,5000)
        #初始化精灵组
        self.bg_group,self.enemy_group,self.hero_group,self.bomb_group = create_sprites()
        self.hero = None
        for hero in self.hero_group:
            self.hero = hero

    def start_game(self):
        print('游戏开始')
        # 代表游戏循环
        while True:
            # #设置刷新帧率，1秒最多被执行60次
            self.clock.tick(Config.FRAME)
            # #事件监听
            check_events(self.hero,self.enemy_group)
            #更新/绘制精灵
            self.bg_group.update()
            self.bg_group.draw(self.screen)
            self.hero_group.update()
            self.hero_group.draw(self.screen)
            self.enemy_group.update()
            self.enemy_group.draw(self.screen)
            self.hero.missiles.update()
            self.hero.missiles.draw(self.screen)
            self.bomb_group.update()
            self.bomb_group.draw(self.screen)
            # 碰撞检测
            collisions(self.enemy_group, self.hero.missiles,self.bomb_group)
            hero_collisions(self.hero_group, self.enemy_group,self.bomb_group)
            draw_text(self.screen,self.font_name,'Score is '+str(Config.SCORE),15,Config.SCREEN_WIDTH/2,10)
            draw_hero_health(self.screen,self.hero,self.hero.health,5,10)
            #更新显示,在所有绘制工作完成后，统一调用，更新绘制窗口，并且显示
            pygame.display.update()


if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    game.start_game()

