import pygame, random


pygame.init()
win = pygame.display.set_mode((1280,678))

pygame.display.set_caption("Stickman")

walkright = [pygame.image.load("Anim/rg1.png"), pygame.image.load("Anim/rg2.png"),
             pygame.image.load("Anim/rg3.png"), pygame.image.load("Anim/rg4.png"),
             pygame.image.load("Anim/rg1.png"), pygame.image.load("Anim/rg2.png"),
             pygame.image.load("Anim/rg3.png"), pygame.image.load("Anim/rg4.png"),
             pygame.image.load("Anim/rg1.png"), pygame.image.load("Anim/rg2.png"),
             pygame.image.load("Anim/rg3.png"), pygame.image.load("Anim/rg4.png"),
             pygame.image.load("Anim/rg1.png"), pygame.image.load("Anim/rg2.png"),
             pygame.image.load("Anim/rg3.png"), pygame.image.load("Anim/rg4.png")]
walkleft = [pygame.image.load("Anim/left1.png"), pygame.image.load("Anim/left2.png"),
             pygame.image.load("Anim/left3.png"), pygame.image.load("Anim/left4.png"),
            pygame.image.load("Anim/left1.png"), pygame.image.load("Anim/left2.png"),
             pygame.image.load("Anim/left3.png"), pygame.image.load("Anim/left4.png"),
            pygame.image.load("Anim/left1.png"), pygame.image.load("Anim/left2.png"),
             pygame.image.load("Anim/left3.png"), pygame.image.load("Anim/left4.png"),
            pygame.image.load("Anim/left1.png"), pygame.image.load("Anim/left2.png"),
             pygame.image.load("Anim/left3.png"), pygame.image.load("Anim/left4.png")]

bwalkrg = [pygame.image.load("Anim/brg1.png"), pygame.image.load("Anim/brg2.png"),
             pygame.image.load("Anim/brg3.png"), pygame.image.load("Anim/brg4.png"),
           pygame.image.load("Anim/brg1.png"), pygame.image.load("Anim/brg2.png"),
             pygame.image.load("Anim/brg3.png"), pygame.image.load("Anim/brg4.png"),
           pygame.image.load("Anim/brg1.png"), pygame.image.load("Anim/brg2.png"),
             pygame.image.load("Anim/brg3.png"), pygame.image.load("Anim/brg4.png"),
           pygame.image.load("Anim/brg1.png"), pygame.image.load("Anim/brg2.png"),
             pygame.image.load("Anim/brg3.png"), pygame.image.load("Anim/brg4.png")]

bwalkleft = [pygame.image.load("Anim/bleft1.png"), pygame.image.load("Anim/bleft2.png"),
             pygame.image.load("Anim/bleft3.png"), pygame.image.load("Anim/bleft4.png"),
             pygame.image.load("Anim/bleft1.png"), pygame.image.load("Anim/bleft2.png"),
             pygame.image.load("Anim/bleft3.png"), pygame.image.load("Anim/bleft4.png"),
             pygame.image.load("Anim/bleft1.png"), pygame.image.load("Anim/bleft2.png"),
             pygame.image.load("Anim/bleft3.png"), pygame.image.load("Anim/bleft4.png")]

bg = pygame.image.load("Anim/bg.jpg")
playerstand = pygame.image.load("Anim/stay.png")

clock = pygame.time.Clock()
x1 = 0
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
animcount1 = 0
lastmove = ""

run = True
bullets = []
enemies = []




class enemy():
    def __init__(self, k, x, y):
        global animcount
        self.k = k
        self.x = x
        self.y = y
        if k == 1:
            self.qw = bwalkleft
        else:
            self.qw = bwalkrg
    def spawn(self):
        win.blit(self.qw[animcount1 // 4], (self.x, self.y))


class bullet():
    def __init__(self, x,y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def death(ff,gg):
    for en in ff:
        for bull in gg:
            if en.x == bull.x:
                gg.pop(gg.index(bull))
                ff.pop(ff.index(en))

def drawwin():
    global animcount, animcount1
    win.blit(bg, (0, 0))

    if animcount + 1 >= 40:
        animcount = 0
    if animcount1 + 1 >= 40:
        animcount1 = 0
    if left:
        win.blit(walkleft[animcount//4], (x, y))
        animcount +=1
    elif right:
        win.blit(walkright[animcount//4], (x, y))
        animcount +=1
    else:
        win.blit(playerstand, (x,y))

    for bull in bullets:
        bull.draw(win)

    for en in enemies:
        en.spawn()
        if en.k ==2:
            en.x += speed
        elif en.k ==1:
            en.x -= speed
    if True:
        animcount1 += 1
    for en in enemies:
        if x == en.x:
             run = False
    pygame.display.update()

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


    if len(enemies) < 40:
        for i in range(40):
            k = random.choice([1,2])
            if k == 1:
                f = random.randint(300,500)
                x1 = 1200 + f * i
            else:
                f = random.randint(300, 500)
                x1 = 0 - f * i
            enemies.append(enemy(k, x1, y))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if lastmove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 12:
            bullets.append(bullet(round(x + width // 2), round(y + height // 3), 5, (255,0,0), facing))
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
        if keys[pygame.K_UP] :
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

