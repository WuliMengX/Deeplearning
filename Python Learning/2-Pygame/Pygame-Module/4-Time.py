"""pygame.time时间控制模块管理时间和游戏帧数率"""
"""
    注意，在 Pygame 中时间以毫秒为单位（1秒=1000毫秒），这样会使游戏的设计更为精细
    
    游戏暂停：
        pygame.time.get_ticks() 	以毫秒为单位获取时间
        pygame.time.wait()	        使程序暂停一段时间
        pygame.time.set_timer()	    创建一个定时器，即每隔一段时间，去执行一些动作
        pygame.time.Clock()	        创建一个时钟对象来帮我们确定游戏要以多大的帧数运行

"""
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('c语言中文网')

# 获取以毫秒为单位的时间
t = pygame.time.get_ticks() #该时间指的从pygame初始化后开始计算，到调用该函数为止
t1 =pygame.time.wait(3000) #暂停游戏3000毫秒

print(t1)
#暂停t1时间后，加载图片
image_surface = pygame.image.load("C:/Users/Administrator/Desktop/c-net.png")


"""
    设置游戏FPS：
        pygame.time.Clock.tick()	更新clock对象
        pygame.time.Clock.get_time()	获取上一个tick中的时间
        pygame.time.Clock.get_fps()	计算clock对象的帧率
        
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption('c语言中文网')

# 获取以毫秒为单位的时间
t = pygame.time.get_ticks() #该时间指的从pygame初始化后开始计算，到调用该函数为止
t1 =pygame.time.delay(3000) #暂停游戏3000毫秒

print(t1)
#暂停t1时间后，加载图片
image_surface = pygame.image.load("C:/Users/Administrator/Desktop/c-net.png")

#创建时钟对象（控制游戏的FPS）
clock = pygame.time.Clock()

while True:
    #通过时钟对象，指定循环频率，每秒循环60次
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(image_surface,(0,0))
    pygame.display.update()