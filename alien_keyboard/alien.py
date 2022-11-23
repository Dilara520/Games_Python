#pgzero
import random

WIDTH = 600
HEIGHT = 300

TITLE = "Alien Run" 
FPS = 30 

alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))
new_pic = 'alien'
bee = Actor('bee', (850, 175))
end = Actor("end")

game_end = 0
point = 0
enemy = random.randint(1,2)
speed = 5

def boxes():
    global point
    global enemy
    global speed
    if box.x > -20:
        box.x = box.x - 5
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
        point = point + 1
        enemy = random.randint(1,2)
        speed = speed + 1
        
def bees():
    global point
    global enemy
    global speed
    if bee.x > -20:
        bee.x = bee.x - 5
    else:
        bee.x = WIDTH + 20
        point = point + 1
        enemy = random.randint(1,2)
        speed = speed + 1
        bee.y = random.randint(120,180)

def draw():
    background.draw()
    alien.draw()
    if enemy == 1:
        box.draw()
    else:
        bee.draw()
    screen.draw.text(point, pos=(10, 10), color="white", fontsize = 24)
    if game_end == 1:
        end.draw()
        screen.draw.text("Press Enter", pos=(170, 250), color= "white", fontsize = 36)

    
def update(dt):
    global game_end
    global point
    global speed
    global new_pic
    if enemy == 1:
        boxes()
    else:
        bees()

    if keyboard.left or keyboard.a and alien.x > 20:
        alien.x = alien.x - 5
        if new_pic != 'left':
            alien.image = 'left'
            new_pic = 'left'
    elif keyboard.right or keyboard.d and alien.x < 580:
        alien.x = alien.x + 5
        if new_pic != 'right':
            alien.image = 'right'
            new_pic = 'right'
    elif keyboard.down or keyboard.s:
        if new_pic != 'down':
            alien.image = 'down'
            new_pic = 'down'
            alien.y = 250
    else:
        if alien.y > 240 and new_pic == 'alien':
            alien.image = 'alien'
            new_pic = 'alien'
            alien.y = 240
    

    if game_end == 1 and keyboard.enter:
        game_end = 0 
        point = 0
        alien.pos = (50, 240)
        box.pos = (550, 265)
        bee.pos = (850, 175)
        speed = 5

    if alien.colliderect(box) or alien.colliderect(bee):
        game_end = 1
        
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)
