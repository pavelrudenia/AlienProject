class Settings():
#класс для хранения всех настроек игры
    def __init__(self):
        #инициализируем настройки игры
        self.screen_width = 800
        self.screen_height = 640
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


        # Настройки пришельцев
        self.alien_speed = 0.5
        self.alien_speed =0.5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        self.ship_limit = 3
        self.ship_limit = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.alien_speed = 0.5
        self.bullet_speed = 0.75
        self.ship_speed = 0.75
        # self.ship_speed_factor = 1.5
        # self.bullet_speed_factor = 3.0
        # self.alien_speed_factor = 1.0
        fleet_direction = 1 #обозначает движение вправо; а -1 - влево.
        self.fleet_direction =1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points+=int(self.alien_points*self.score_scale-self.alien_points)