import pygame, sys, os, time

""" Functions """

# when gun shoot make shooting sound
def pew():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('shoot.wav'))

# when enemy hit make explosion sound
def hit():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('hit.wav'))

# prints all xy positions of moving objs/imgs
def printGameStats():
    print("-----Player X and Y -----")
    print(str(x) + " " + str(y))
    if(shot == True):
        print("-----Bullet X and Y -----")
        print(str(tempx) + " " + str(tempy))
    print("-----Enemy X and Y's -----")
    print(str(boss_x) + " " + str(boss_y) + '\n')

""" Variables """

# dimensions 
width = 600
height = 800

# is done bool, for game loop
done = False

# if player shot bool
shot = False

# is game over bool
over = False
# player x and y
x = 350
y = 465

# player change x
lead_x = 0

# bullet change y
lead_y = 0

# enemies x and y's
boss_x = 450
boss_y = 40

# counter for each enemy, if not hit --> 0 if hit --> 1
cntr = 0

# boss laser timer
laserTimer = 0

# temp enemy x and y
tempx = 0
tempy = 0

# healthbar x and y
health_bar_x = 420
health_bar_y = 20

# cntr holding hit amount
hitCounter = 0

# boss laser xy
laserx = 0
lasery = 0
laserx2 = 0
lasery2 = 0
bossShot = False
bossShot2 = False

# enemy pos
en_x =  0
en_y = 250
en2_x = 100
en2_y = 250
en3_x = 200
en3_y = 250
en4_x = 300
en4_y = 250
en5_x = 400
en5_y = 250

hasLives = [True] * 3

# pixel size
pixel = 64
pixel2 = 45

# starting amount, enemy x movement
amount = 14

# health bar starting amount
health = 100

# counter
cnt = 0
cnt2 = 0
j = 0
cntr = 0
cntr2 = 0
cntr3 = 0
cntr4 = 0
cntr5 = 0

# boss bool
bossMoveX = False
bossMoveY = False

# RGB values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
skyblue = (135,206,235)
blue = (0,0,255)
magenta = (175, 0, 175)
transparent = (0, 0, 0, 0)

""" Screen """

# mixer/pygame init
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()

# screen
screen = pygame.display.set_mode((height, width), pygame.DOUBLEBUF, 32)

# caption
pygame.display.set_caption('Space Invaders')

# clock element
clock = pygame.time.Clock()

# background 
bg = pygame.image.load("background.jpg")

# creates imgs
player = pygame.image.load('ship.png').convert_alpha()
enemy2 = pygame.image.load('enemy2.png').convert_alpha()
win = pygame.image.load('youwin.png').convert_alpha()
lose = pygame.image.load('youlose.png').convert_alpha()
boss = pygame.image.load('boss.png').convert_alpha()
heart = pygame.image.load('heart.png').convert_alpha()
lives = pygame.image.load('lives.png').convert_alpha()

""" Game Loop """

# run program
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 11 
            
            if event.key == pygame.K_RIGHT:
                lead_x += 11
            
            if event.key == pygame.K_SPACE:
                shot = True
                pew()
                tempx = x 
                tempy = y
                lead_y += 20
    
    """ Game Code """

    # player movements
    x += lead_x
    if(x>650):
        x = 650
    elif(x<0):
        x = 0

    # boss movements
    if(bossMoveX == False):
        boss_x -= 10
        health_bar_x -= 10
        if(boss_x < 200):
            bossMoveX = True
    elif(bossMoveX == True):
        boss_x += 10
        health_bar_x += 10
        if(boss_x > 500):
            bossMoveX = False
    

    # boss enemy movements
    en_x += amount
    if(en_x > 700):
        amount += 0.08
        en_x = 0
        en_y += 30
    
    en2_x += amount
    if(en2_x > 700):
        amount += 0.08
        en2_x = 0
        en2_y += 30
        
    en3_x += amount
    if(en3_x > 700):
        amount += 0.08
        en3_x = 0
        en3_y += 30

    en4_x += amount
    if(en4_x > 700):
        amount += 0.08
        en4_x = 0
        en4_y += 30
        
    en5_x += amount
    if(en5_x > 700):
        amount += 0.08
        en5_x = 0
        en5_y += 30

    # blits background
    screen.blit(bg, (0, 0))

    # blits lives
    screen.blit(pygame.transform.scale(lives, (200,200)), (0,-50))

    # blits hearts if player has life
    if(hasLives[0] == True):
        screen.blit(pygame.transform.scale(heart, (50,80)), (0,5))

    if(hasLives[1] == True):    
        screen.blit(pygame.transform.scale(heart, (50,80)), (50,5))
        
    if(hasLives[2] == True):
        screen.blit(pygame.transform.scale(heart, (50,80)), (100,5))

        
    # blits enemies if not hit
    if(cntr == 0):
        screen.blit(pygame.transform.scale(enemy2, (80,80)), (en_x,en_y)) 
            
    if(cntr2 == 0):  
        screen.blit(pygame.transform.scale(enemy2, (80,80)), (en2_x,en2_y)) 
            
    if(cntr3 == 0):  
        screen.blit(pygame.transform.scale(enemy2, (80,80)), (en3_x,en3_y))

    if(cntr4 == 0):  
        screen.blit(pygame.transform.scale(enemy2, (80,80)), (en4_x,en4_y)) 
            
    if(cntr5 == 0):  
        screen.blit(pygame.transform.scale(enemy2, (80,80)), (en5_x,en5_y))

    # blits boss if not killed
    if(health != 0):
        screen.blit(pygame.transform.scale(boss, (150,150)), (boss_x,boss_y))

    # creates bullet variables every 5 seconds
    if(laserTimer % 100 == 0 and over == False):
        laserx = boss_x + 20
        lasery = boss_y + 100
        laserx2 = boss_x + 100
        lasery2 = boss_y + 100
        bossShot = True
        bossShot2 = True

    # blits bullets
    if(bossShot == True and over == False):
        pygame.draw.rect(screen,red,[laserx,lasery,10,10])
        lasery += 8

    if(bossShot2 == True and over == False):
        pygame.draw.rect(screen,red,[laserx2,lasery2,10,10])
        lasery2 += 8

    # blits player
    screen.blit(pygame.transform.scale(player, (150,150)), (x,y))

    # prints game stats
    #printGameStats()

    # creates health bar
    if(hitCounter == 0):
        pygame.draw.rect(screen,red,[health_bar_x,health_bar_y,200,10])
    if(hitCounter == 1):
        pygame.draw.rect(screen,red,[health_bar_x,health_bar_y,160,10])
    if(hitCounter == 2):
        pygame.draw.rect(screen,red,[health_bar_x,health_bar_y,120,10])
    if(hitCounter == 3):
        pygame.draw.rect(screen,red,[health_bar_x,health_bar_y,80,10])
    if(hitCounter == 4):
        pygame.draw.rect(screen,red,[health_bar_x,health_bar_y,40,10])
    if(hitCounter == 5):
        print("Win!")
        

    # creates bullet and movement
    if(shot == True):
        pygame.draw.rect(screen,blue,[tempx+63,tempy+17,15,15])
        tempy -= lead_y

    # bullet speed and shot reset after bullet goes offscreen
    if(tempy < 0):
        shot = False
        lead_y = 0

    # bullet to enemies collision
    if(shot == True):
        if((tempx > en_x - pixel) and (tempy < en_y + pixel) and (tempx < en_x + pixel) and (tempy > en_y - pixel)):
            hit()
            cntr += 1
            shot = False
            en_x =-50
            en_y=-50
        elif((tempx > en2_x - pixel) and (tempy < en2_y + pixel) and (tempx < en2_x + pixel) and (tempy > en2_y - pixel)):
            hit()
            cntr2 += 1
            shot = False
            en2_x =-50
            en2_y=-50
        elif((tempx > en3_x - pixel) and (tempy < en3_y + pixel) and (tempx < en3_x + pixel) and (tempy > en3_y - pixel)):
            hit()
            cntr3 += 1
            shot = False
            en3_x =-50
            en3_y=-50

    # bullet to enemies collision
    if(shot == True):
        if(tempx > boss_x - pixel) and (tempy < boss_y + pixel):
            hit()
            health -= 20
            print("Boss health: " + str(health))
            hitCounter += 1
            shot = False
    
    # boss bullet to player collision
    if((laserx > x - pixel2) and (lasery < y + pixel2) and (laserx < x + pixel2) and (lasery > y - pixel2) and (bossShot == True)):
            print(str(x) + " " + str(y) + str(laserx) + " " + str(lasery))
            hasLives[j] = False
            j += 1
            bossShot = False
    
    # boss bullet2 to player collision
    if((laserx2 > x - pixel2) and (lasery2 < y + pixel2) and (laserx2 < x + pixel2) and (lasery2 > y - pixel2) and (bossShot2 == True)):
            print(str(x) + " " + str(y) + str(laserx) + " " + str(lasery))
            hasLives[j] = False
            j += 1
            bossShot2 = False
            
    # win/lose text
    if(cntr > 4):
        screen.blit(pygame.transform.scale(win, (300,300)), (250,100)) 
        bossShot = False
        bossShot2 = False
        over = True
    elif(y - en_y <= 45 and x - en_x < 0):
            if(cntr == 0):
                hasLives[j] = False
                cntr += 1
                j += 1
    elif(y - en2_y <= 45 and x - en2_x < 0):
        if(cntr2 == 0):
            hasLives[j] = False
            cntr2 += 1
            j += 1
    elif(y - en3_y <= 45 and x - en3_x < 0):
         if(cntr3 == 0):
            hasLives[j] = False
            cntr3 += 1
            j += 1
    #elif((y - en_y <= 45 and x - en_x < 0) or (y - en2_y <= 45 and x - en2_x < 0) or (y - en3_y <= 45 and x - en3_x < 0) or (y - en4_y <= 45 and x - en4_x < 0) or (y - en5_y <= 45 and x - en5_x < 0) or (y - en6_y <= 45 and x - en6_x < 0)):
     #   screen.blit(pygame.transform.scale(lose, (300,300)), (180,100))
     #   over = True
    
    """ Screen Update """

    pygame.display.update()
    screen.fill(skyblue)
    clock.tick(32)
