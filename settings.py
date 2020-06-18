class Settings():
    """ Game Settings """

    def __init__(self):
        # main settings
        self.caption = 'Aliens Invasion'
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 4

        #bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 5

        #alien's settings
        self.alien_speed = 1.0
        self.alien_drop_speed = 1.0
        
        # fleet direction right = 1, direction left = -1
        self.fleet_direction = 1

