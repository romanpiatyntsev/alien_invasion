class GameStats:
    """ Game statistics """

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # the highest score
        self.high_score = 0

    def reset_stats(self):
        """start statistic"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
