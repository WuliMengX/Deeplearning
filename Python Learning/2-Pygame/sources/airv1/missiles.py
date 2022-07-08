from gamesprites import GameSprite
import os


class Missile(GameSprite):
    def __init__(self):
        super().__init__(os.path.join('images','bullet1.png'),-2)

    def update(self):
        super().update()
        #self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        #print('子弹被销毁')
        pass