import pygame


class Ship():
    """SHIP"""

    def __init__(self, ai_game, speed=1):
        # get main screen
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # get ship screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start position
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.settings = ai_game.settings
        self.x = float(self.rect.x)

    def update(self):
        """"Uptates ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Render Model"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """movie ship to center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

