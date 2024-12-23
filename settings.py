class Settings:
    def __init__(self):
        self.fleet_drop_speed = 10
        # 加快速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # 1表示向右，为-1表示向左
        self.fleet_direction = 1
        # 指定玩家每击落一个外星人都将得到多少个点
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置并增加外星人分数值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)