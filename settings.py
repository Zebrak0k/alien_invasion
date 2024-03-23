class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (120, 120, 120)
        self.bullets_allowed = 8

        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1