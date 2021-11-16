import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    # Класс для управления ресурсами и поведением игры.
    def __init__(self):
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Инициализирует игру и создает игровые ресурсы.
        pygame.init()
        pygame.display.set_caption("Вторжение пришельцев")

        self.ship = Ship(self)


    def run_game(self):
        # Запуск основного цикла игры.
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #при каждом проходе цикла перериcовывается экран
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
