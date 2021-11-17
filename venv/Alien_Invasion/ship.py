import pygame

class Ship():
    """класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        """Загружает изображение корабля и получает прямоугольник."""
        self.image = pygame.image.load('Image/ship.bmp')
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()
        """Каждый новый корабль появляется у нижнего края экрана."""
        self.rect.midbottom = self.screen_rect.midbottom

        """флаг перемещения"""
        self.moving_right = False
        self.moving_left = False

        """сохранение вещественной координаты корабля"""
        self.x =float(self.recct.x)

    def update(self):
        """обновляем позицию корабля в зависимости от флага"""
        if self.moving_right:

            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)