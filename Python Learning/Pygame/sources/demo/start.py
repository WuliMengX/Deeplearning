import sys
import pygame
from demo.bg import BackGround
from demo.config import Parameter
from demo.player import Player
from demo.enemy import Enemy


class ShootingGame:

    def __init__(self): #初始化这个类别中的属性
        pygame.init()
        #创建游戏窗口
        self.screen = pygame.display.set_mode((Parameter.SCREEN_WIDTH, Parameter.SCREEN_HEIGHT))
        # 设置游戏标题
        pygame.display.set_caption(Parameter.TITLE)

        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 设置分数的字体
        self.font_name = pygame.font.match_font(Parameter.FONT)

        # 设置定时事件，创建敌机 1s
        pygame.time.set_timer(Parameter.ENEMY_EVENT, 1000)
        #设置分数的事件，分数越高代表存活时间越长
        pygame.time.set_timer(Parameter.SCORE_EVENT,1000)

        #游戏开始的时候加载我们的游戏背景,对于每一个游戏精灵类建议使用不同的精灵组
        bg_false = BackGround() #背景本身和screen重合
        bg_true = BackGround(True) #背景在screen的上方
        self.background_group = pygame.sprite.Group(bg_false)
        self.background_group.add(bg_true)

        # 游戏开始的时候加载我们的玩家飞机
        self.player1 = Player()  # 背景本身和screen重合
        self.player_group = pygame.sprite.Group(self.player1)

        # 游戏开始的时候加载我们的敌人飞机
        self.enemy_group = pygame.sprite.Group()
        self.score = 0

    def draw_text(self,surf, font_name, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, Parameter.BLUE)  # (R,G,B)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surface, text_rect)

    def start_game(self):
        print('游戏开始')
        #代表游戏循环的开始
        while True:
            #设置刷新帧率，1秒最多被执行60次
            self.clock.tick(Parameter.FRAME)

            # 事件监听
            for event in pygame.event.get():
                # 判断是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # 判断敌人飞机产生的事件
                if event.type == Parameter.ENEMY_EVENT:
                    enemy = Enemy()
                    self.enemy_group.add(enemy)
                # 判断敌人飞机产生的事件
                if event.type == Parameter.SCORE_EVENT:
                    self.score += 1
                    print(self.score)
                # 判断玩家的操作事件
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player1.moving_down = True
                    elif event.key == pygame.K_LEFT:
                        self.player1.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.player1.moving_right = True
                    elif event.key == pygame.K_UP:
                        self.player1.moving_up = True
                    elif event.key == pygame.K_SPACE:
                        #missile = Missile()
                        #self.player1.fire(missile)
                        #self.missile_group.add(missile)
                        pass
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player1.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.player1.moving_left = False
                    elif event.key == pygame.K_DOWN:
                        self.player1.moving_down = False
                    elif event.key == pygame.K_UP:
                        self.player1.moving_up = False


            # 碰撞检测
            hits = pygame.sprite.groupcollide(self.player_group, self.enemy_group, False, True)  # 撞击就已经被移除了
            for hit in hits:
                hit.health -= Parameter.DAMAGE
                if hit.health <= 0:
                    hit.kill()
                    pygame.quit()
                    sys.exit()

            # 更新精灵组
            self.background_group.update() #使得背景精灵组里的每一个背景对象都去更新一下update
            self.background_group.draw(self.screen)

            self.player_group.update()  # 使得背景精灵组里的每一个背景对象都去更新一下update
            self.player_group.draw(self.screen)

            self.enemy_group.update()  # 使得背景精灵组里的每一个背景对象都去更新一下update
            self.enemy_group.draw(self.screen)

            self.draw_text(self.screen, self.font_name, 'Score is ' + str(self.score), 15, Parameter.SCREEN_WIDTH / 2, 10)
            # 更新显示,在所有绘制工作完成后，统一调用，更新绘制窗口，并且显示
            pygame.display.update()


if __name__ == '__main__':
    #创建游戏对象
    game = ShootingGame()
    game.start_game()