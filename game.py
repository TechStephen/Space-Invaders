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
    if(roundCount != 3):
        print("-----Enemy X and Y's -----")
        print("1.) " + str(en_x) + " " + str(en_y))
        print("2.) " + str(en2_x) + " " + str(en2_y))
        print("3.) " + str(en3_x) + " " + str(en3_y))
        print("4.) " + str(en4_x) + " " + str(en4_y))
        print("5.) " + str(en5_x) + " " + str(en5_y))
        print("6.) " + str(en6_x) + " " + str(en6_y))
        print("7.) " + str(en7_x) + " " + str(en7_y))
        print("8.) " + str(en8_x) + " " + str(en8_y))
        print("9.) " + str(en9_x) + " " + str(en9_y))
        print("10.) " + str(en10_x) + " " + str(en10_y))
        print("11.) " + str(en11_x) + " " + str(en11_y))
        print("12.) " + str(en12_x) + " " + str(en12_y))
        print("13.) " + str(en13_x) + " " + str(en13_y))
        print("14.) " + str(en14_x) + " " + str(en14_y))
        print("15.) " + str(en15_x) + " " + str(en15_y))
        print("16.) " + str(en16_x) + " " + str(en16_y))
        print("17.) " + str(en17_x) + " " + str(en17_y))
        print("18.) " + str(en18_x) + " " + str(en18_y) + "\n")
    else:
        print("-----Boss X and Y's -----")
        print(str(boss_x) + " " + str(boss_y))
        print("-----Enemy X and Y's -----")
        print("1.) " + str(enn_x) + " " + str(enn_y))
        print("2.) " + str(enn2_x) + " " + str(enn2_y))
        print("3.) " + str(enn3_x) + " " + str(enn3_y))
        print("4.) " + str(enn4_x) + " " + str(enn4_y))
        print("5.) " + str(enn5_x) + " " + str(enn5_y) + "\n")

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

# if player pressed play
play = False

# if on boss level
bosss = False

# if won game bool
winn = False

# if boss shot bools
bossShot = False
bossShot2 = False

# player x and y
x = 350
y = 465

# player change x
lead_x = 0

# bullet change y
lead_y = 0

# enemies x and y's, row 1
en_x = 0
en_y = 30
en2_x = 80
en2_y = 30
en3_x = 200
en3_y = 30
en4_x = 300
en4_y = 30
en5_x = 400
en5_y = 30
en6_x = 500
en6_y = 30

# row 2
en7_x = 0
en7_y = 105
en8_x = 80
en8_y = 105
en9_x = 200
en9_y = 105
en10_x = 300
en10_y = 105
en11_x = 400
en11_y = 105
en12_x = 500
en12_y = 105

# row 3
en13_x = 0
en13_y = 180
en14_x = 80
en14_y = 180
en15_x = 200
en15_y = 180
en16_x = 300
en16_y = 180
en17_x = 400
en17_y = 180
en18_x = 500
en18_y = 180

# counter for each enemy, if not hit --> 0 if hit --> 1
cntr = 0
cntr2 = 0
cntr3 = 0
cntr4 = 0
cntr5 = 0 
cntr6 = 0
cntr7 = 0
cntr8 = 0
cntr9 = 0
cntr10 = 0
cntr11 = 0 
cntr12 = 0
cntr13 = 0
cntr14 = 0
cntr15 = 0
cntr16 = 0
cntr17 = 0 
cntr18 = 0

# lives lost counter
j = 0

# roundCount counter
roundCount = 1

# boss enemy blits counters
cnt = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0

# enemies x and y's
boss_x = 450
boss_y = 40

# boss laser timer
laserTimer = 0

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

# boss enemy positions
enn_x =  0
enn_y = 250
enn2_x = 100
enn2_y = 250
enn3_x = 200
enn3_y = 250
enn4_x = 300
enn4_y = 250
enn5_x = 400
enn5_y = 250

# health bar starting amount
health = 100

# boss movement bools
bossMoveX = False
bossMoveY = False

# heart hit bools
hasLives = [True] * 3

# temp enemy x and y
tempx = 0
tempy = 0

# pixel size(s)
pixel = 64
pixel2 = 45

# starting amount(s), enemy x movement
amount = 9
amount2 = 14

# RGB values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0,0,255)
skyblue = (135,206,235)
magenta = (1105, 0, 1105)
transparent = (0, 0, 0, 0)

""" Screen """

# mixer setup
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.

# plays game music
pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.wav'))

# screen
screen = pygame.display.set_mode((height, width), pygame.DOUBLEBUF, 32)

# caption
pygame.display.set_caption('Space Invaders')

# clock element
clock = pygame.time.Clock()

# creates background 
bg = pygame.image.load("background.jpg")

# creates imgs
player = pygame.image.load('ship.png').convert_alpha()
enemy = pygame.image.load('enemy.png').convert_alpha()
enemy2 = pygame.image.load('enemy2.png').convert_alpha()
enemy3 = pygame.image.load('enemy3.png').convert_alpha()
win = pygame.image.load('youwin.png').convert_alpha()
lose = pygame.image.load('youlose.png').convert_alpha()
start = pygame.image.load('start.png').convert_alpha()
heart = pygame.image.load('heart.png').convert_alpha()
lives = pygame.image.load('lives.png').convert_alpha()
round1 = pygame.image.load('round1.png').convert_alpha()
round2 = pygame.image.load('round2.png').convert_alpha()
round3 = pygame.image.load('round3.png').convert_alpha()
advance = pygame.image.load('advance.png').convert_alpha()
boss = pygame.image.load('boss.png').convert_alpha()
thanks = pygame.image.load('thanks.png').convert_alpha()
tryagain = pygame.image.load('tryagain.png').convert_alpha()


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
                if(over == False):
                    shot = True
                    pew()
                    tempx = x 
                    tempy = y
                    lead_y += 15

            if event.key == pygame.K_RETURN:
                winn = False
                bosss = False
                play = True
            
            if event.key == pygame.K_y:
                print("play again pressed")
                roundCount += 1
                if(roundCount == 2): # if round 2 reset alot of variables to default, speed faster (amount)
                    over = False
                    en_x = 0
                    en_y = 30
                    en2_x = 80
                    en2_y = 30
                    en3_x = 200
                    en3_y = 30
                    en4_x = 300
                    en4_y = 30
                    en5_x = 400
                    en5_y = 30
                    en6_x = 500
                    en6_y = 30
                    en7_x = 0
                    en7_y = 105
                    en8_x = 80
                    en8_y = 105
                    en9_x = 200
                    en9_y = 105
                    en10_x = 300
                    en10_y = 105
                    en11_x = 400
                    en11_y = 105
                    en12_x = 500
                    en12_y = 105
                    en13_x = 0
                    en13_y = 180
                    en14_x = 80
                    en14_y = 180
                    en15_x = 200
                    en15_y = 180
                    en16_x = 300
                    en16_y = 180
                    en17_x = 400
                    en17_y = 180
                    en18_x = 500
                    en18_y = 180
                    cntr = 0
                    cntr2 = 0
                    cntr3 = 0
                    cntr4 = 0
                    cntr5 = 0 
                    cntr6 = 0
                    cntr7 = 0
                    cntr8 = 0
                    cntr9 = 0
                    cntr10 = 0
                    cntr11 = 0 
                    cntr12 = 0
                    cntr13 = 0
                    cntr14 = 0
                    cntr15 = 0
                    cntr16 = 0
                    cntr17 = 0 
                    cntr18 = 0
                    j = 0
                    amount = 13
                    hasLives[0] = True
                    hasLives[1] = True
                    hasLives[2] = True
                elif(roundCount == 3):
                    bosss = True
                    over = False
    
    """ Game Code """

    if(play == True and bosss == False):

        # player movements
        x += lead_x
        if(x>650):
            x = 650
        elif(x<0):
            x = 0
        
        # enemy movements, all 18 enemy x and y's below
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
        
        en6_x += amount
        if(en6_x > 700):
            amount += 0.08
            en6_x = 0
            en6_y += 30
        
        en7_x += amount
        if(en7_x > 700):
            amount += 0.08
            en7_x = 0
            en7_y += 30
        
        en8_x += amount
        if(en8_x > 700):
            amount += 0.08
            en8_x = 0
            en8_y += 30
        
        en9_x += amount
        if(en9_x > 700):
            amount += 0.08
            en9_x = 0
            en9_y += 30
        
        en10_x += amount
        if(en10_x > 700):
            amount += 0.08
            en10_x = 0
            en10_y += 30
        
        en11_x += amount
        if(en11_x > 700):
            amount += 0.08
            en11_x = 0
            en11_y += 30
        
        en12_x += amount
        if(en12_x > 700):
            amount += 0.08
            en12_x = 0
            en12_y += 30
        
        en13_x += amount
        if(en13_x > 700):
            amount += 0.08
            en13_x = 0
            en13_y += 30

        en14_x += amount
        if(en14_x > 700):
            amount += 0.08
            en14_x = 0
            en14_y += 30
        
        en15_x += amount
        if(en15_x > 700):
            amount += 0.08
            en15_x = 0
            en15_y += 30

        en16_x += amount
        if(en16_x > 700):
            amount += 0.08
            en16_x = 0
            en16_y += 30
        
        en17_x += amount
        if(en17_x > 700):
            amount += 0.08
            en17_x = 0
            en17_y += 30
        
        en18_x += amount
        if(en18_x > 700):
            amount += 0.08      
            en18_x = 0
            en18_y += 30

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
        
        # blits round count
        if(roundCount == 1):
            screen.blit(pygame.transform.scale(round1, (400,400)), (535,-140))
        elif(roundCount == 2):
            screen.blit(pygame.transform.scale(round2, (400,400)), (535,-140)) 
        elif(roundCount == 3):
            screen.blit(pygame.transform.scale(round3, (400,400)), (535,-140))

        # blits player
        screen.blit(pygame.transform.scale(player, (140,150)), (x,y))

        # if game not running dont draw enemies
        if(over == False):
        
        # prints game stats
            printGameStats()
        
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
            
            if(cntr6 == 0):
                screen.blit(pygame.transform.scale(enemy2, (80,80)), (en6_x,en6_y))

            if(cntr7 == 0):
                screen.blit(pygame.transform.scale(enemy, (80,80)), (en7_x,en7_y))  
            
            if(cntr8 == 0):  
                screen.blit(pygame.transform.scale(enemy, (80,80)), (en8_x,en8_y))
            
            if(cntr9 == 0):  
                screen.blit(pygame.transform.scale(enemy, (80,80)), (en9_x,en9_y))
            
            if(cntr10 == 0):
                screen.blit(pygame.transform.scale(enemy, (80,80)), (en10_x,en10_y))

            if(cntr11 == 0):  
                screen.blit(pygame.transform.scale(enemy, (80,80)), (en11_x,en11_y))
            
            if(cntr12 == 0):
                screen.blit(pygame.transform.scale(enemy, (80,80)), (en12_x,en12_y))

            if(cntr13 == 0):
                screen.blit(pygame.transform.scale(enemy3, (80,80)), (en13_x,en13_y))

            if(cntr14 == 0):
                screen.blit(pygame.transform.scale(enemy3, (80,80)), (en14_x,en14_y)) 
            
            if(cntr15 == 0):
                screen.blit(pygame.transform.scale(enemy3, (80,80)), (en15_x,en15_y))

            if(cntr16 == 0):
                screen.blit(pygame.transform.scale(enemy3, (80,80)), (en16_x,en16_y))

            if(cntr17 == 0):
                screen.blit(pygame.transform.scale(enemy3, (80,80)), (en17_x,en17_y))

            if(cntr18 == 0):
                screen.blit(pygame.transform.scale(enemy3, (80,80)), (en18_x,en18_y))    
        
        # creates bullet and movement
        if(shot == True):
            pygame.draw.rect(screen,red,[tempx+63,tempy+17,15,15])
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
            elif((tempx > en4_x - pixel) and (tempy < en4_y + pixel) and (tempx < en4_x + pixel) and (tempy > en4_y - pixel)):
                hit()
                cntr4 += 1
                shot = False
                en4_x =-50
                en4_y=-50
            elif((tempx > en5_x - pixel) and (tempy < en5_y + pixel) and (tempx < en5_x + pixel) and (tempy > en5_y - pixel)):
                hit()
                cntr5 += 1
                shot = False
                en5_x =-50
                en5_y=-50
            elif((tempx > en6_x - pixel) and (tempy < en6_y + pixel) and (tempx < en6_x + pixel) and (tempy > en6_y - pixel)):
                hit()
                cntr6 += 1
                shot = False
                en6_x =-50
                en6_y=-50
            elif((tempx > en7_x - pixel) and (tempy < en7_y + pixel) and (tempx < en7_x + pixel) and (tempy > en7_y - pixel)):
                hit()
                cntr7 += 1
                shot = False
                en7_x =-50
                en7_y=-50
            elif((tempx > en8_x - pixel) and (tempy < en8_y + pixel) and (tempx < en8_x + pixel) and (tempy > en8_y - pixel)):
                hit()
                cntr8 += 1
                shot = False
                en8_x =-50
                en8_y=-50
            elif((tempx > en9_x - pixel) and (tempy < en9_y + pixel) and (tempx < en9_x + pixel) and (tempy > en9_y - pixel)):
                hit()
                cntr9 += 1
                shot = False
                en9_x =-50
                en9_y=-50
            elif((tempx > en10_x - pixel) and (tempy < en10_y + pixel) and (tempx < en10_x + pixel) and (tempy > en10_y - pixel)):
                hit()
                cntr10 += 1
                shot = False
                en10_x =-50
                en10_y=-50
            elif((tempx > en11_x - pixel) and (tempy < en11_y + pixel) and (tempx < en11_x + pixel) and (tempy > en11_y - pixel)):
                hit()
                cntr11+= 1
                shot = False
                en11_x =-50
                en11_y=-50
            elif((tempx > en12_x - pixel) and (tempy < en12_y + pixel) and (tempx < en12_x + pixel) and (tempy > en12_y - pixel)):
                hit()
                cntr12+= 1
                shot = False
                en12_x =-50
                en12_y=-50
            elif((tempx > en13_x - pixel) and (tempy < en13_y + pixel) and (tempx < en13_x + pixel) and (tempy > en13_y - pixel)):
                hit()
                cntr13+= 1
                shot = False
                en13_x =-50
                en13_y=-50
            elif((tempx > en14_x - pixel) and (tempy < en14_y + pixel) and (tempx < en14_x + pixel) and (tempy > en14_y - pixel)):
                hit()
                cntr14+= 1
                shot = False
                en14_x =-50
                en14_y=-50
            elif((tempx > en15_x - pixel) and (tempy < en15_y + pixel) and (tempx < en15_x + pixel) and (tempy > en15_y - pixel)):
                hit()
                cntr15+= 1
                shot = False
                en15_x =-50
                en15_y=-50
            elif((tempx > en16_x - pixel) and (tempy < en16_y + pixel) and (tempx < en16_x + pixel) and (tempy > en16_y - pixel)):
                hit()
                cntr16+= 1
                shot = False
                en16_x =-50
                en16_y=-50
            elif((tempx > en17_x - pixel) and (tempy < en17_y + pixel) and (tempx < en17_x + pixel) and (tempy > en17_y - pixel)):
                hit()
                cntr17+= 1
                shot = False
                en17_x =-50
                en17_y=-50
            elif((tempx > en18_x - pixel) and (tempy < en18_y + pixel) and (tempx < en18_x + pixel) and (tempy > en18_y - pixel)):
                hit()
                cntr18+= 1
                shot = False
                en18_x =-50
                en18_y=-50
                        
        # win text if all enemies hit, and lose a life if player gets hit by any of the 18 enemies
        if(cntr > 0 and cntr2 > 0 and cntr3 > 0 and cntr4 > 0 and cntr5 > 0 
        and cntr6 > 0 and cntr7 > 0 and cntr8 > 0 and cntr9 > 0 and cntr10 > 0 
        and cntr11 > 0 and cntr12 > 0 and cntr13 > 0 and cntr14 > 0 and cntr15 > 0 
        and cntr16 > 0 and cntr17 > 0 and cntr18 > 0):
            screen.blit(pygame.transform.scale(win, (300,300)), (250,80)) 
            screen.blit(pygame.transform.scale(advance, (400,400)), (195,180))
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('win.wav'))
            over = True
        elif(y - en_y <= 45 and x - en_x < 0):
            if(cntr == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr += 1
                j += 1
        elif(y - en2_y <= 45 and x - en2_x < 0):
            if(cntr2 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr2 += 1
                j += 1
        elif(y - en3_y <= 45 and x - en3_x < 0):
            if(cntr3 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr3 += 1
                j += 1
        elif(y - en4_y <= 45 and x - en4_x < 0):
            if(cntr4 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr4 += 1
                j += 1
        elif(y - en5_y <= 45 and x - en5_x < 0):
            if(cntr5 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr5 += 1
                j += 1
        elif(y - en6_y <= 45 and x - en6_x < 0):
            if(cntr6 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr6 += 1
                j += 1
        elif(y - en7_y <= 45 and x - en7_x < 0):
            if(cntr7 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr7 += 1
                j += 1
        elif(y - en8_y <= 45 and x - en8_x < 0):
            if(cntr8 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr8 += 1
                j += 1 
        elif(y - en9_y <= 45 and x - en9_x < 0):
            if(cntr9 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr9 += 1
                j += 1
        elif(y - en10_y <= 45 and x - en10_x < 0):
            if(cntr10 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr10 += 1
                j += 1
        elif(y - en11_y <= 45 and x - en11_x < 0):
            if(cntr11 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr11 += 1
                j += 1
        elif(y - en12_y <= 45 and x - en12_x < 0):
            if(cntr12 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr12 += 1
                j += 1
        elif(y - en13_y <= 45 and x - en13_x < 0):
            if(cntr13 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr13 += 1
                j += 1
        elif(y - en14_y <= 45 and x - en14_x < 0):
            if(cntr14 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr14 += 1
                j += 1
        elif(y - en15_y <= 45 and x - en15_x < 0):
            if(cntr15 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr15 += 1
                j += 1
        elif(y - en16_y <= 45 and x - en16_x < 0):
            if(cntr16 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr16 += 1
                j += 1
        elif(y - en17_y <= 45 and x - en17_x < 0):
            if(cntr17 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr17 += 1
                j += 1
        elif(y - en18_y <= 45 and x - en18_x < 0):
            if(cntr18 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cntr18 += 1
                j += 1

        # if lose all lives, lose
        if(hasLives[2] == False):
            screen.blit(pygame.transform.scale(lose, (300,300)), (220,80))
            screen.blit(pygame.transform.scale(tryagain, (600,600)), (170,180))
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('lose.wav'))
            over = True
    
    # round 3, boss round
    elif(play == True and bosss == True):
        
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
        enn_x += amount2
        if(enn_x > 700):
            amount2 += 0.08
            enn_x = 0
            enn_y += 30
        
        enn2_x += amount2
        if(enn2_x > 700):
            amount2 += 0.08
            enn2_x = 0
            enn2_y += 30
            
        enn3_x += amount2
        if(enn3_x > 700):
            amount2 += 0.08
            enn3_x = 0
            enn3_y += 30

        enn4_x += amount2
        if(enn4_x > 700):
            amount2 += 0.08
            enn4_x = 0
            enn4_y += 30
            
        enn5_x += amount2
        if(enn5_x > 700):
            amount2 += 0.08
            enn5_x = 0
            enn5_y += 30

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
        
        # blits round count
        if(roundCount == 1):
            screen.blit(pygame.transform.scale(round1, (400,400)), (535,-140))
        elif(roundCount == 2):
            screen.blit(pygame.transform.scale(round2, (400,400)), (535,-140)) 
        elif(roundCount == 3):
            screen.blit(pygame.transform.scale(round3, (400,400)), (535,-140))
            
        # blits enemies if not hit
        if(cnt == 0):
            screen.blit(pygame.transform.scale(enemy2, (80,80)), (enn_x,enn_y)) 
                
        if(cnt2 == 0):  
            screen.blit(pygame.transform.scale(enemy2, (80,80)), (enn2_x,enn2_y)) 
                
        if(cnt3 == 0):  
            screen.blit(pygame.transform.scale(enemy2, (80,80)), (enn3_x,enn3_y))

        if(cnt4 == 0):  
            screen.blit(pygame.transform.scale(enemy2, (80,80)), (enn4_x,enn4_y)) 
                
        if(cnt5 == 0):  
            screen.blit(pygame.transform.scale(enemy2, (80,80)), (enn5_x,enn5_y))

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
        if(over == False):
            printGameStats()

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
            if((tempx > enn_x - pixel) and (tempy < enn_y + pixel) and (tempx < enn_x + pixel) and (tempy > enn_y - pixel)):
                hit()
                cnt += 1
                shot = False
                en_x =-50
                en_y=-50
            elif((tempx > enn2_x - pixel) and (tempy < enn2_y + pixel) and (tempx < enn2_x + pixel) and (tempy > enn2_y - pixel)):
                hit()
                cnt2 += 1
                shot = False
                enn2_x =-50
                enn2_y=-50
            elif((tempx > enn3_x - pixel) and (tempy < enn3_y + pixel) and (tempx < enn3_x + pixel) and (tempy > enn3_y - pixel)):
                hit()
                cnt3 += 1
                shot = False
                enn3_x =-50
                enn3_y=-50
            elif((tempx > enn4_x - pixel) and (tempy < enn4_y + pixel) and (tempx < enn4_x + pixel) and (tempy > enn4_y - pixel)):
                hit()
                cnt4 += 1
                shot = False
                enn4_x =-50
                enn4_y= -50
            elif((tempx > enn5_x - pixel) and (tempy < enn5_y + pixel) and (tempx < enn5_x + pixel) and (tempy > enn5_y - pixel)):
                hit()
                cnt5 += 1
                shot = False
                enn5_x =-50
                enn5_y= -50

        # bullet to boss collision
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
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                j += 1
                bossShot = False
        
        # boss bullet2 to player collision
        if((laserx2 > x - pixel2) and (lasery2 < y + pixel2) and (laserx2 < x + pixel2) and (lasery2 > y - pixel2) and (bossShot2 == True)):
                print(str(x) + " " + str(y) + str(laserx) + " " + str(lasery))
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                j += 1
                bossShot2 = False                

        # if hit by boss enemies lose a life, for all 5 boss enemies (normal enemies)
        if(y - enn_y <= 45 and x - enn_x < 0):
                if(cnt == 0):
                    try:
                        hasLives[j] = False
                    except Exception as e:
                        pass
                    cnt += 1
                    j += 1
        
        if(y - enn2_y <= 45 and x - enn2_x < 0):
            if(cnt2 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cnt2 += 1
                j += 1
        
        if(y - enn3_y <= 45 and x - enn3_x < 0):
            if(cnt3 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cnt3 += 1
                j += 1
        
        if(y - enn4_y <= 45 and x - enn4_x < 0):
            if(cnt4 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cnt4 += 1
                j += 1
        
        if(y - enn5_y <= 45 and x - enn5_x < 0):
            if(cnt5 == 0):
                try:
                    hasLives[j] = False
                except Exception as e:
                    pass
                cnt5 += 1
                j += 1

        # if lose all lives, lose
        if(hasLives[2] == False):
            screen.blit(pygame.transform.scale(lose, (300,300)), (220,80))
            screen.blit(pygame.transform.scale(tryagain, (600,600)), (170,180))
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('lose.wav'))
            over = True

        # if defeats boss, wins game
        if(health == 0):
            screen.blit(pygame.transform.scale(win, (400,400)), (205,60)) 
            screen.blit(pygame.transform.scale(thanks, (600,600)), (115,215))
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('win.wav'))
            over = True
            cnt += 1
            cnt2 += 1
            cnt3 += 1
            cnt4 += 1
            cnt5 += 1

        # increments laser timer if games not over
        if(over == False):
            laserTimer += 1

    else:
        """ Start Screen """

        # blits background
        screen.blit(bg, (0, 0))

        # blits start screen
        screen.blit(pygame.transform.scale(start, (600,600)), (130,0))

        # blits player
        screen.blit(pygame.transform.scale(player, (150,150)), (x,y))
    
    """ Screen Update """

    pygame.display.update()
    clock.tick(32)

        
