class GameStats:
    """ Game statistics """

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """start statistic"""
        self.ships_left = self.settings.ship_limit
