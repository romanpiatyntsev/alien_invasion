class Settings():
    """ Game Settings """

    def __init__(self):
        # main settings
        self.caption = 'Aliens Invasion'
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 5
        # count user ships
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 4

        #alien's settings
        self.alien_speed = 0.5
        self.alien_points = 50

        # fleet direction right = 1, direction left = -1
        self.fleet_direction = 2
        self.fleet_drop_speed = 12
