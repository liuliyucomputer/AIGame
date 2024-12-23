import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        # msg是要在按钮中显示的文本
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50  # 设置按钮的尺寸和其他属性
        self.button_color = (0, 255, 0)  # 亮绿色
        self.text_color = (255, 255, 255)  # 白色
        self.font = pygame.font.SysFont(None, 48)  # 指定字体来渲染文本, None使用默认字体，而48指定了文本的字号
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 按钮
        self.rect.center = self.screen_rect.center  # 让按钮在屏幕上居中
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center  # 让文本图像在按钮上居中

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)  # 在按钮中心绘制文本图像