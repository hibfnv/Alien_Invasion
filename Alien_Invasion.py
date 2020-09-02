import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
# 导入pygame.Sprite包中的Group
from pygame.sprite import Group


def run_game():
    # 初始化游戏，并绘制游戏窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于丰储子弹的编组Group()
    bullets = Group()
    # 开始游戏的主循环
    while True:
        # 监听鼠标键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
