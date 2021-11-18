class Settings():
#класс для хранения всех настроек игры
    def __init__(self):
        #инициализируем настройки игры
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (171, 205, 239)
        """настройки корабля"""
        self.ship_speed =1.1
        # Параметры снаряда
        self.bullet_speed = 0.75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 25, 25)
        #количество пуль
        self.bullets_allowed = 15
