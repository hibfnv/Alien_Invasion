"""
        因为是火箭的移动，在主屏幕已经设置好相关的信息之后，我们没有看到火箭在哪里，所以在此处，我们就应该定义一个火箭了。
        为了让火箭的图片显示在屏幕上，我们同样需要导入pygame模块，让它能够加载我们的图片到屏幕中去
"""
import pygame


class Rocket():
    def __init__(self, screen):
        """初始化火箭的起始位置"""
        self.screen = screen
        # 加载火箭图片，并绘制火箭的大小的矩形
        self.image = pygame.image.load('imgs/rock_smp.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每次游戏窗口关闭后再打开时，火箭都放置在屏幕正中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def paintup(self):
        """将火箭放置在指定的位置"""
        self.screen.blit(self.image, self.rect)
