import pygame, random

pygame.init()
win = pygame.display.set_mode((1280,678))

pygame.display.set_caption("Stickman")

walkright = [pygame.image.load("Anim/rg1.png"), pygame.image.load("Anim/rg2.png"),
             pygame.image.load("Anim/rg3.png"), pygame.image.load("Anim/rg4.png")]
walkleft = [pygame.image.load("Anim/left1.png"), pygame.image.load("Anim/left2.png"),
             pygame.image.load("Anim/left3.png"), pygame.image.load("Anim/left4.png")]

bwalkrg = [pygame.image.load("Anim/brg1.png"), pygame.image.load("Anim/brg2.png"),
             pygame.image.load("Anim/brg3.png"), pygame.image.load("Anim/brg4.png")]

bwalkleft = [pygame.image.load("Anim/bleft1.png"), pygame.image.load("Anim/bleft2.png"),
             pygame.image.load("Anim/bleft3.png"), pygame.image.load("Anim/bleft4.png")]

bg = pygame.image.load("Anim/bg.jpg")
playerstand = pygame.image.load("Anim/stay.png")

clock = pygame.time.Clock()

x = 500
y = 550
width = 40
height = 60
speed = 4

isjump = False
jumpcount = 10

left = False
right = False
animcount = 0
lastmove = ""

class enemy():
    def __init__(self):
        self.x = -30
        self.y = 550
        self.health = 3
        self.speed = 2
    def spawn(self):
        while self.health != 0:
            for i in bwalkrg:
                i



class bullet():
    def __init__(self, x,y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 12 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawwin():
    global animcount
    win.blit(bg, (0, 0))

    if animcount + 1 >= 40:
        animcount = 0

    if left:
        win.blit(walkleft[animcount//10], (x, y))
        animcount +=1
    elif right:
        win.blit(walkright[animcount//10], (x, y))
        animcount +=1
    else:
        win.blit(playerstand, (x,y))

    for bull in bullets:
        bull.draw(win)
    pygame.display.update()

run = True
bullets = []
enemies = []

run = True

while run:
    clock.tick(40)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    for bull in bullets:
        if bull.x < 1280 and bull.x > 0:
            bull.x += bull.vel
        else:
            bullets.pop(bullets.index(bull))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastmove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 8:
            bullets.append(bullet(round(x + width // 2), round(y + height // 2), 5, (255,0,0), facing))
    if keys[pygame.K_LEFT] and x>5:
        x -= speed
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 1280 - width - 5:
        x += speed
        left = False
        right = True
        lastmove = "right"
    else:
        left = False
        right = False
        animcount = 0
        lastmove = "left"


    if not isjump:
        if keys[pygame.K_SPACE] :
            isjump = True
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                y += (jumpcount**2) / 5
            else:
                y -= (jumpcount**2) / 5
            jumpcount -= 1

        else:
            isjump = False
            jumpcount = 10


    drawwin()

pygame.quit()
