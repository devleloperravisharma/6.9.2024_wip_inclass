import pgzrun

import random

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------'

TITLE = "Snatch The Nectar"

WIDTH = 600

HEIGHT = 500

score = 0

game_over = False
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------'

flower = Actor("flower")

beebee = Actor("bee")

flower.pos = (100, 100)

beebee.pos = (20, 20)

def draw():
    screen.blit("pink_wallpaper", (0,0))
    flower.draw()
    beebee.draw()

def movefl():
    flower.x = random.randint(70, WIDTH-70)
    flower.y = random.randint(70, WIDTH-70)

movefl()



pgzrun.go()