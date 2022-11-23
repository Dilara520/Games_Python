#pgzero

from turtle import back


WIDTH = 600
HEIGHT = 400

TITLE = "Animal Jumper"
FPS = 30

# Nesneler
animal = Actor("animal1", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
game = Actor("game", (300, 100))
cross = Actor("cross", (580, 20))
shop = Actor("shop", (300, 200))
collection = Actor("collection", (300, 300))
animal2 = Actor('animal2', (120, 200))
animal3 = Actor('animal3', (300, 200))
animal4 = Actor('animal4', (480, 200))

point = 0
count = 1
mode = 'menu'
price_1 = 15
price_2 = 200
price_3 = 600
animals = []

def draw():
    if mode == 'menu':
        background.draw()
        game.draw()
        screen.draw.text(point, center=(30, 20), color="white", fontsize = 36)
        shop.draw()
        collection.draw()
   
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(point, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("1$ for 2 seconds", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(price_1, center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("15$ for 2 seconds", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(price_2, center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("50$ for two seconds", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(price_3, center=(450, 310), color="black", fontsize = 20)
        cross.draw()
    
    elif mode == 'shop':
        background.draw()
        animal2.draw()
        screen.draw.text("500$", center= (120, 300), color="white", fontsize = 36)
        animal3.draw()
        screen.draw.text("2500$", center= (300, 300), color="white", fontsize = 36)
        animal4.draw()
        screen.draw.text("7000$", center= (480, 300), color="white", fontsize = 36)
        cross.draw()
        screen.draw.text(point, center=(30, 20), color="white", fontsize = 36)
    
    elif mode == 'collection':
        background.draw()
        for i in range(len(animals)):
            animals[i].draw()
        cross.draw()
        screen.draw.text(point, center=(30, 20), color="white", fontsize = 36)
        screen.draw.text("+2$", center= (120, 300), color="white", fontsize = 36)
        screen.draw.text("+3$", center= (300, 300), color="white", fontsize = 36)
        screen.draw.text("+4$", center= (480, 300), color="white", fontsize = 36)

def bonus_1_choice():
    global point
    point += 1

def bonus_2_choice():
    global point
    point += 15

def bonus_3_choice():
    global point
    point += 50

def on_mouse_down(button, pos):
    global point
    global mode
    global price_1, price_2, price_3
    global count

    if button == mouse.LEFT and mode == "game":
        if animal.collidepoint(pos):
            point += count
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if point >= price_1:
                schedule_interval(bonus_1_choice, 2)
                point -= price_1
                price_1 *= 2
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if point >= poince_2:
                schedule_interval(bonus_2_choice, 2)
                point -= price_2
                price_2 *= 2
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if point >= price_3:
                schedule_interval(bonus_3_choice, 2)
                point -= price_3
                price_3 *= 2
        elif cross.collidepoint(pos):
            mode = 'menu'
    elif mode == 'menu' and button == mouse.LEFT:
        if game.collidepoint(pos):
            mode = 'game'
        elif shop.collidepoint(pos):
            mode = 'shop'
        elif collection.collidepoint(pos):
            mode = "collection"

    elif  mode == 'shop' and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = 'menu'
        elif animal2.collidepoint(pos):
            animal2.y = 180
            animate(animal2, tween='bounce_end', duration=0.5, y=200)
            if animal in animals:
                animal.image = 'animal2'
            elif point >= 500:
                point -= 500
                count = 2
                animal.image = 'animal2'
                animals.append(animal2)
        elif animal3.collidepoint(pos):
            animal3.y = 180
            animate(animal3, tween='bounce_end', duration=0.5, y=200)
            if animal3 in animals:
                animals.image = 'animal3'
            elif point >= 2500:
                point -= 2500
                count = 3
                animal.image = 'animal3'
                animals.append(animal3)
        elif animal4.collidepoint(pos):
            animal4.y = 180
            animate(animal4, tween='bounce_end', duration=0.5, y=200)
            if animal4 in animals:
                animal4.image = 'animal4'
            elif point >= 7000:
                point -= 7000
                count = 4
                animal.image = 'animal4'
                animals.append(animal4)

    elif  mode == 'collection' and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = 'menu'
        elif animal2.collidepoint(pos):
            animal2.y = 180
            animate(animal2, tween='bounce_end', duration=0.5, y=200)
            if animal2 in animals:
                animal.image = 'animal2'
        elif animal3.collidepoint(pos):
            animal3.y = 180
            animate(animal3, tween='bounce_end', duration=0.5, y=200)
            if animal3 in animals:
                animals.image = 'animal3'
        elif animal4.collidepoint(pos):
            animal4.y = 180
            animate(animal4, tween='bounce_end', duration=0.5, y=200)
            if animal4 in animals:
                animal4.image = 'animal4'
