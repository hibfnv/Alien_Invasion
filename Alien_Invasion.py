import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    # 初始化游戏，并绘制游戏窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        # 监听鼠标键盘事件
        gf.check_events(ship)
        ship.update()
        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
