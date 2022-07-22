from gameelements import ElementSprite
import os


class BackGround(ElementSprite):
    def __init__(self,is_another=False):
        super().__init__(os.path.join('images','background.png'))
        if is_another:
            self.rect.y = -self.rect.height
    # 重写父类的方法update

    def update(self):
        super().update()
        # 判断是否移出屏幕，如果移出则将图片设置到屏幕的上方
        if self.rect.y >= 700:
            self.rect.y = -self.rect.height  # 在坐标系之上所以为负值