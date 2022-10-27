
import pygame as pg
from classes import *
import time
from sys import exit


pg.init()


pg.display.set_caption( "Osu India the game" )
width, height = 800, 400
screen = pg.display.set_mode( (width, height) )
clock = pg.time.Clock()
collision_leniency = 15
game_state = 0 
framerate = 60
gravity = 0.5

#sprite groups
background_image = pg.image.load("graphics\sidetracked.png")
background_image = pg.transform.scale(background_image, (800, 300))
background_rect = background_image.get_rect(topleft = (0, 0))

player = pg.sprite.GroupSingle()
player.add(Player("graphics\masala.png"))

ground = pg.sprite.GroupSingle()
ground.add(Ground("graphics\ground.png"))

platforms = pg.sprite.Group()
platforms.add(Platform())

#delta time
prev_time = time.time()

while True:
    keys = pg.key.get_pressed()
    dt = time.time() - prev_time
    prev_time = time.time()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            exit()
    
    if game_state == 0:
#player update#################################################

        platforms.update()
        player.sprite.collision_ground(ground.sprite)
        player.update()

#platforms######################################################  


        
        
        
        print(player.sprite.vx)
        screen.blit(background_image, background_rect)
        platforms.draw(screen)
        player.draw(screen)
        ground.draw(screen)
        
    pg.display.update()
    clock.tick(framerate)


