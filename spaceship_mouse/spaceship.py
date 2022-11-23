#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Space Wars"
FPS = 30

ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("planet1", (random.randint(0, 600), -100)), Actor("planet2", (random.randint(0, 600), -100)), Actor("planet3", (random.randint(0, 600), -100))]
meteors = []
fires = []
mode = 'menü'
ship1 = Actor("ship1", (100, 200))
ship2 = Actor("ship2", (300, 200))
ship3 = Actor("ship3", (500, 200))
point = 0

def fill(): 
    for i in range(5):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        enemy = Actor("enemy", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)
        
    for i in range(5):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        meteor = Actor("meteor", (x, y))
        meteor.speed = random.randint(2, 10)
        meteors.append(meteor)
fill()

def draw():
    if mode == 'menu':
        space.draw()
        screen.draw.text('Choose your spaceship', center = (300, 100), color = "white", fontsize = 36)
        ship1.draw()
        ship2.draw()
        ship3.draw()
    if mode == 'game':
        space.draw()
        planets[0].draw()
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        for i in range(len(enemies)):
            enemies[i].draw() 
        for i in range(len(fires)):
            fires[i].draw()
        screen.draw.text(point, (10, 10), color = "white")
    elif mode == 'end':
        space.draw()
        screen.draw.text("THE END", center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text(point, center = (300, 250), color = "white", fontsize = 64)

def on_mouse_move(pos):
    ship.pos = pos

def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

def planet_move():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

def meteor_move():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

def collides():
    global mode
    global point
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for j in range(len(fires)):
            if fires[j].colliderect(enemies[i]):
                point = point + 1
                enemies.pop(i)
                fires.pop(j)
                new_enemy()
                break

def update(dt):
    global point, mode, enemies, planets, meteors, fires
    if mode == 'game':
        enemy_ship()
        collides()
        planet_move()
        meteor_move()
        for i in range(len(fires)):
            if fires[i].y < 0:
                fires.pop(i)
                break
            else:
                fires[i].y = fires[i].y - 10
    elif mode == 'end':
        mode = 'menu'
        point = 0
        enemies = []
        planets = [Actor("planet1", (random.randint(0, 600), -100)), Actor("planet2", (random.randint(0, 600), -100)), Actor("planet3", (random.randint(0, 600), -100))]
        meteors = []
        fires = []
        fill()
        
def on_mouse_down(button, pos):
    global mode, ship
    if mode == 'menu' and ship1.collidepoint(pos):
        ship.image = "ship1"
        mode = 'game'
    elif mode == 'menu' and ship2.collidepoint(pos):
        ship.image = "ship2"
        mode = 'game'
    elif mode == 'menu' and ship3.collidepoint(pos):
        ship.image = "ship3"
        mode = 'game'
    elif mode == 'game' and button == mouse.LEFT:
        fire = Actor("fires")
        fire.pos = ship.pos
        fire.append(fire)
