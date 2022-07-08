"""pygame.transform对加载和创建后的图像操作"""
"""
    常用方法：
        pygame.transform.scale()	将图片缩放至指定的大小，并返回一个新的 Surface 对象
        pygame.transform.rotate()	将图片旋转至指定的角度
        pygame.transform.rotozoom()	以角度旋转图像，同时将图像缩小或放大至指定的倍数

"""
import pygame

#引入pygame中所有常量，比如 QUIT
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((500,250))
pygame.display.set_caption('c语言中文网')

#加载一张图片（455*191)
image_surface = pygame.image.load("C:/Users/Administrator/Desktop/c-net.png").convert()
image_new = pygame.transform.scale(image_surface,(300,300))

# 查看新生成的图片的对象类型
#print(type(image_new))

# 对新生成的图像进行旋转至45度
image_1 =pygame.transform.rotate(image_new,45)

# 使用rotozoom() 旋转 0 度，将图像缩小0.5倍
image_2 = pygame.transform.rotozoom(image_1,0,0.5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # 将最后生成的image_2添加到显示屏幕上
    screen.blit(image_2,(0,0))
    pygame.display.update()