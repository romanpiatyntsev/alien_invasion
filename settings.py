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
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 10
        self.bullet_width = 600
        self.bullet_height = 10
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        #alien's settings
        self.alien_speed = 1

        # fleet direction right = 1, direction left = -1
        self.fleet_direction = 2
        self.fleet_drop_speed = 10
