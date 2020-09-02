class Settings():
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (30, 144, 255)
        self.ship_speed_rate = 1.0
        # 游戏中子弹的相关参数需要在此设置
        self.bullet_speed_rate = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 248, 255, 255
        self.bullet_allowed = 3
