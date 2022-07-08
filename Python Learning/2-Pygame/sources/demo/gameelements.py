import pygame


class ElementSprite(pygame.sprite.Sprite):
    def __init__(self,image,speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed


    def update(self):
        self.rect.y += self.speed
