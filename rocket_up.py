"""
    利用12章相关内容，自己设计一个可移动的火箭：
    要求火箭能在给定的屏幕移动，但不能超出屏幕范围。火箭可以在x和y轴移动，并且开始的状态为在屏幕中央位置
"""
# 以下是程序代码：
# 首先要导入pygame来对屏幕进行绘制，绘制的屏幕大小在1280x800
# 导入sys和pygame模块
import sys
import pygame
# 将rocket_sets类中的参数在此处导入
from Rocket_Nav.rocket_sets import RocketSets
from Rocket_Nav.rocket_in import Rocket
import Rocket_Nav.rock_fun as rockfun


# 主程序在开始的状态下显示的效果，并定义初始化屏幕内容的方法
def main():
    """
    通过pygame模块初始化屏幕:
    由于此处的screen宽高和背景色都是可以在相应的类里面进行定义的，所以此处可以定义一个宽高和背景设置的类，这个类里面还可以加入在主屏幕中
    更多的相关设置项，这里的screen width和screen height，background color,还有后期的一些加入项的设置,调用火箭的图片需要用到火
    箭的类，在main方法中则必须导入火箭的类Rocket,并将主程序中设置实参关联Rocket类，如rock = Rocket(screen)
    """
    pygame.init()
    # 设置屏幕的宽高像素为1280x800
    # screen = pygame.display.set_mode((1280, 800))  此项已经加入到rocket_sets类
    # 由于将上面一行的内容加入了rocket_sets类，所以后面的过程中我们需要重新构建一个形参来涵盖我们在rocket_sets类中定义的实参
    ai_sets = RocketSets()
    # 定义了ai_sets实参为RocketSets的形参,pygame.display.set_mode((a,b)),记得，set_mode里一定是元组，而非int整数
    screen = pygame.display.set_mode((ai_sets.screen_width, ai_sets.screen_height))
    # 设置屏幕窗口显示的字样是Rocket Move
    pygame.display.set_caption("Rocket Move")
    # 设置调用火箭的类
    rock = Rocket(screen)
    # 设置屏幕的背景
    # bg_color = (87, 250, 255) 此项也已加入rocket_sets类
    # 设置游戏的主体循环体
    """
    因为在主体循环中，有对按键的判断，如果用户按上下左右键和松开后火箭会在屏幕中移动，因此将检测用户按上下左右方向键然后松开的动作反馈到屏幕显示
    上面，但要求火箭无论如何都不能超出屏幕范围，即不能让火箭消失在屏幕上。
    """
    while 1:
        """ 检测用户按键情况并进行相应的反馈   此处因为在后期重构了event检测的方法，所以此处不再需要以下几行代码，只需要导入重构的event检测
        模块，最后在此处将模块的方法用上。
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # sys.exit()
        """
        rockfun.check_events(rock)
        rockfun.update_screen(ai_sets, screen, rock)
        """
        # 每次循环都重绘屏幕图像
        因为在rock_fun中重新定义了screen.fill和rock.paintup方法，所以在此处，我们只需要调用，而可以减少此处的代码
        # screen.fill(bg_color) 同样因为rocket_sets形参里面已经包含了bg_color的实参，所以要调用bg_color只需要如下调用即可：
        # screen.fill(ai_sets.bg_color)
        # 将火箭绘制到屏幕中央
        # rock.paintup()
        """
        # 绘制屏幕图像并显示
        pygame.display.flip()


main()
