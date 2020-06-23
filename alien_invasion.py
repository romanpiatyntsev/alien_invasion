import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """AlienInvasion Game Controller"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((1200, 800))

        self.settings = Settings()
        pygame.display.set_caption(self.settings.caption)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.stats = GameStats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            if event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - alien_width
        available_space_y = self.settings.screen_height - \
            (alien_height * 3) - self.ship.rect.height
        number_aliens_x = available_space_x // (2 * alien_width)
        number_rows = available_space_y // (2 * alien_height)

        # create row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """move down the fleet and reverse direction"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        """ Create alien and add his to row """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.y <= (0 - self.settings.bullet_height):
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """ Delete bullet and alien """
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            #
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        self.stats.ships_left -= 1

        # clear aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet
        self._create_fleet()
        self.ship.center_ship()

        # pause
        sleep(0.5)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        """RUN GAME"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            # pygame.time.delay(20)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
