import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    # Класс для управления ресурсами и поведением игры.
    def __init__(self):
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Инициализирует игру и создает игровые ресурсы.
        pygame.init()
        pygame.display.set_caption("Вторжение пришельцев")
        """ДЛЯ ПОЛНОЭКРАННОГО РЕЖИМА 
              self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
               self.settings.screen_width = self.screen.get_rect().width
               self.settings.screen_height = self.screen.get_rect().height"""
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    def run_game(self):
        # Запуск основного цикла игры.
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            # при каждом проходе цикла перериcовывается экран
            self._update_screen()
            self.ship.update()
            self._update_bullets()

            print(f"Число пуль на экране {len(self.bullets)}")
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_UP:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""

        # Обновление позиций снарядов.
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)



if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
