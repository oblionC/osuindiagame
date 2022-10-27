import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, imageloc):
        super().__init__()
        self.x = 100
        self.y = -200
        self.width = 50
        self.height = 75
        self.image = pg.image.load(imageloc).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.max_xspeed = 5.2
        self.max_yspeed = 30
        self.jump_vel = -15
        self.jump_available = 0
        self.space_prev_frame = 0
        self.down_prev_frame = 0
        self.down_pressed = 0
        self.down_released = 0
        self.up_prev_frame = 0
        self.dx = 0.5
        self.vx = 0.0
        self.vy = 0.0
        self.speed_added = 0.0
        self.gravity = 0.5
        self.friction = 0.2

    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.jump_available and self.space_prev_frame == 0:
            self.jump_available = 0
            self.vy = self.jump_vel
        
        if keys[pg.K_LEFT]:
            self.speed_added += -self.dx
            self.vx += -self.dx
            if self.speed_added < -self.max_xspeed:
                self.vx -= self.speed_added + self.max_xspeed
                self.speed_added = -self.max_xspeed
                
        if keys[pg.K_RIGHT]:
            self.speed_added += self.dx
            self.vx += self.dx
            if self.speed_added > self.max_xspeed:
                self.vx -= self.speed_added - self.max_xspeed
                self.speed_added = self.max_xspeed
        
        self.space_prev_frame = keys[pg.K_SPACE]

    def collision_ground(self, ground):

        if ground.rect.colliderect((self.x, self.y + self.vy), (self.width, self.height)):
            self.rect.bottom = ground.rect.top
            self.jump_available = 1
            self.vy = -self.gravity
    
    def collision_platform(self, platform):
        pass
        
    def apply_gravity(self):

        if self.vy < self.max_yspeed:
            self.vy += self.gravity
        else:
            self.vy = self.max_yspeed

    def apply_friction(self):
        
        if self.vx > 0.2:
            self.speed_added += -self.friction
            self.vx += -self.friction
        elif self.vx < -0.2:
            self.speed_added += self.friction
            self.vx += self.friction
        else:
            self.speed_added = 0 
            self.vx = 0

    def apply_v(self):

        self.y += self.vy
        self.rect.y = self.y

        self.x += self.vx
        self.rect.x = self.x

    def update(self):

        self.apply_friction()
        self.player_input()
        self.apply_gravity()
        self.apply_v()




class Ground(pg.sprite.Sprite):
    def __init__(self, imageloc):
        super().__init__()
        self.image = pg.image.load(imageloc)
        self.rect = self.image.get_rect(topleft = (0, 300))


class Platform(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 50
        self.x = 200
        self.y = 250
        self.image = pg.image.load("graphics\dard.jpg")
        self.image = pg.transform.scale(self.image, (self.width, self.height)) 
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.vx = -10


    def apply_v(self):
        self.x += self.vx 
        self.rect.x = self.x 

    
    def screenwrap(self):
        if self.x < -350:
            self.x = 900


    def update(self):
        self.apply_v()
        self.screenwrap()