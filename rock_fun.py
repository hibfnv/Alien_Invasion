"""
        将主体中的键盘按键动作进行判断，如果用户按下键盘出现什么情况，如果用户松开又会发生什么变化
"""
# 同样导入sys模块和pygame模块
import sys
import pygame


def check_events(rock):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rock.rect.centerx += 1


# 更新屏幕上的图片信息
def update_screen(ai_sets, screen, rock):
    screen.fill(ai_sets.bg_color)
    rock.paintup()
    # 绘制屏幕可见
    pygame.display.flip()
