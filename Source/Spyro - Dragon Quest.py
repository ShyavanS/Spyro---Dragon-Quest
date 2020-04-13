from pygame_functions import *

pygame.mixer.pre_init(44100,16,2,4096)
screenSize(1280,720)
pygame.mixer.music.load("/opt/Spyro - Dragon Quest/Mario.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
end_it=False
while (end_it==False):
    setBackgroundImage("/opt/Spyro - Dragon Quest/castle.jpg")
    for event in pygame.event.get():
        if keyPressed("space"):
            end_it=True

screenSize(1280,720)

setBackgroundImage("/opt/Spyro - Dragon Quest/Castle2.png")

Enemy1 = makeSprite("/opt/Spyro - Dragon Quest/Enemy1.png")
Enemy2 = makeSprite("/opt/Spyro - Dragon Quest/Enemy2.png")
Enemy3 = makeSprite("/opt/Spyro - Dragon Quest/Enemy1.png")
Dragon = makeSprite("/opt/Spyro - Dragon Quest/Dragon1.png")
addSpriteImage(Dragon,"/opt/Spyro - Dragon Quest/Dragon2.png")
addSpriteImage(Dragon,"/opt/Spyro - Dragon Quest/Dragon3.png")
Cage = makeSprite("/opt/Spyro - Dragon Quest/Cage.png")
Key = makeSprite("/opt/Spyro - Dragon Quest/Key.png")
Platform = makeSprite("/opt/Spyro - Dragon Quest/Platform.png")
Platform2 = makeSprite("/opt/Spyro - Dragon Quest/Platform.png")
Platform3 = makeSprite("/opt/Spyro - Dragon Quest/Platform.png")
Platform4 = makeSprite("/opt/Spyro - Dragon Quest/Platform.png")
Spyro = makeSprite("/opt/Spyro - Dragon Quest/Spyro1.png")
addSpriteImage(Spyro,"/opt/Spyro - Dragon Quest/Spyro2.png")
Fireball = makeSprite("/opt/Spyro - Dragon Quest/Fireball1.png")
addSpriteImage(Fireball,"/opt/Spyro - Dragon Quest/Fireball2.png")
Ladder = makeSprite("/opt/Spyro - Dragon Quest/Ladder.png")
Ladder2 = makeSprite("/opt/Spyro - Dragon Quest/Ladder.png")
Sword1 = makeSprite("/opt/Spyro - Dragon Quest/Sword1.png")
Sword2 = makeSprite("/opt/Spyro - Dragon Quest/Sword2.png")
Sword3 = makeSprite("/opt/Spyro - Dragon Quest/Sword1.png")
showSprite(Ladder)
showSprite(Ladder2)
showSprite(Spyro)
showSprite(Enemy1)
showSprite(Enemy2)
showSprite(Enemy3)
showSprite(Platform)
showSprite(Platform2)
showSprite(Platform3)
showSprite(Platform4)
showSprite(Sword1)
showSprite(Sword2)
showSprite(Sword3)
showSprite(Dragon)
showSprite(Cage)
showSprite(Key)

xPos = 1180
yPos = 585
XPos = 0
YPos = 450
xPOS = 590
xPoS = 167
XPOs = 755
yPOS = 170
XPOS = 110
YPOS = 670
xPOs = 407
YPoS = 406
YPOs = 120
XPoS = 940
xSpeed = 0
ySpeed = 30
XSpeed = 25
xspeed = 25
XSPEED = -25
xpos = xPos-30
ypos = yPos+40
spriteImage=0
hide=False
Hide=False
HIDE=False
locked=True
Runs=1
moveSprite(Spyro,xPos,yPos)
moveSprite(Ladder,500,450)
moveSprite(Ladder2,670,180)
moveSprite(Fireball,xpos,yPos+40)
moveSprite(Enemy1,0,620)
moveSprite(Sword1,XPOS,YPOS)
moveSprite(Platform,XPos,YPos)
moveSprite(Platform2,xPOS,YPos)
moveSprite(Platform3,xPoS,yPOS)
moveSprite(Platform4,XPOs,yPOS)
moveSprite(Key,0,362)
moveSprite(Cage,167,40)
moveSprite(Dragon,173.5,70)
moveSprite(Enemy3,297,70)
moveSprite(Sword3,xPOs,YPOs)
moveSprite(Enemy2,989,356)
moveSprite(Sword2,XPoS,YPoS)
    
while (end_it==True):
    
    if keyPressed("up") and touching (Spyro,Ladder):
        if (spriteImage==0):
            changeSpriteImage(Spyro,0)
            yPos -= 20
            ySpeed = 0
        elif (spriteImage==1):
            changeSpriteImage(Spyro,1)
            yPos -= 20
            ySpeed = 0

    elif keyPressed("up") and touching (Spyro,Ladder2):
        if (spriteImage==0):
            changeSpriteImage(Spyro,0)
            yPos -= 20
            ySpeed = 0
        elif (spriteImage==1):
            changeSpriteImage(Spyro,1)
            yPos -= 20
            ySpeed = 0

    elif keyPressed("up"):
        if (spriteImage==0):
            changeSpriteImage(Spyro,0)
            if yPos == 585:
                ySpeed = -15
                yPos = 585-130
                ySpeed = 15           
            elif yPos+135>=YPos and touching(Spyro,Platform):
                ySpeed = -15
                yPos = YPos-265
                ySpeed = 15
            elif yPos+135>=YPos and touching(Spyro,Platform2):
                ySpeed = -15
                yPos = YPos-265
                ySpeed = 15
            elif yPos+135>=yPOS and touching(Spyro,Platform3):
                ySpeed = -15
                yPos = yPOS-265
                ySpeed = 15
            elif yPos+135>=yPOS and touching(Spyro,Platform4):
                ySpeed = -15
                yPos = yPOS-265
                ySpeed = 15
        elif (spriteImage==1):
            changeSpriteImage(Spyro,1)
            if yPos == 585:
                ySpeed = -15
                yPos = 585-130
                ySpeed = 15           
            elif yPos+135>=YPos and touching(Spyro,Platform):
                ySpeed = -15
                yPos = YPos-265
                ySpeed = 15
            elif yPos+135>=YPos and touching(Spyro,Platform2):
                ySpeed = -15
                yPos = YPos-265
                ySpeed = 15
            elif yPos+135>=yPOS and touching(Spyro,Platform3):
                ySpeed = -15
                yPos = yPOS-265
                ySpeed = 15
            elif yPos+135>=yPOS and touching(Spyro,Platform4):
                ySpeed = -15
                yPos = yPOS-265
                ySpeed = 15
            
    elif keyPressed("down") and touching (Spyro,Ladder):
        if (spriteImage==0):
            changeSpriteImage(Spyro,0)
            yPos += 20
            ySpeed = 0
        elif (spriteImage==1):
            changeSpriteImage(Spyro,1)
            yPos += 20
            ySpeed = 0
    elif keyPressed("down") and touching (Spyro,Ladder2):
        if (spriteImage==0):
            changeSpriteImage(Spyro,0)
            yPos += 20
            ySpeed = 0
        elif (spriteImage==1):
            changeSpriteImage(Spyro,1)
            yPos += 20
            ySpeed = 0

    elif keyPressed("right") and touching(Spyro,Platform):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 0
        spriteImage=1

    elif keyPressed("right") and touching(Spyro,Platform2):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 0
        spriteImage=1

    elif keyPressed("right") and touching(Spyro,Platform3):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 0
        spriteImage=1

    elif keyPressed("right") and touching(Spyro,Platform4):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 0
        spriteImage=1

    elif keyPressed("right") and not touching(Spyro,Platform):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 30
        spriteImage=1

    elif keyPressed("right") and not touching(Spyro,Platform2):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 30
        spriteImage=1

    elif keyPressed("right") and not touching(Spyro,Platform3):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 30
        spriteImage=1

    elif keyPressed("right") and not touching(Spyro,Platform4):
        changeSpriteImage(Spyro,1)
        xPos += 20
        ySpeed = 30
        spriteImage=1

    elif keyPressed("left") and touching(Spyro,Platform):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 0
        spriteImage=0

    elif keyPressed("left") and touching(Spyro,Platform2):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 0
        spriteImage=0

    elif keyPressed("left") and touching(Spyro,Platform3):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 0
        spriteImage=0

    elif keyPressed("left") and touching(Spyro,Platform4):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 0
        spriteImage=0

    elif keyPressed("left") and not touching(Spyro,Platform):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 30
        spriteImage=0

    elif keyPressed("left") and not touching(Spyro,Platform2):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 30
        spriteImage=0

    elif keyPressed("left") and not touching(Spyro,Platform3):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 30
        spriteImage=0

    elif keyPressed("left") and not touching(Spyro,Platform4):
        changeSpriteImage(Spyro,0)
        xPos -= 20
        ySpeed = 30
        spriteImage=0

    elif keyPressed("space"):
        if(spriteImage==0):
            changeSpriteImage(Fireball,0)
            showSprite(Fireball)
            xSpeed -= 15
            if touching(Fireball,Enemy1):
                hideSprite(Enemy1)
                hideSprite(Sword1)
                hideSprite(Fireball)
                hide=True
            if touching(Fireball,Enemy2):
                hideSprite(Enemy2)
                hideSprite(Sword2)
                hideSprite(Fireball)
                Hide=True
            if touching(Fireball,Enemy3):
                hideSprite(Enemy3)
                hideSprite(Sword3)
                hideSprite(Fireball)
                HIDE=True
        elif(spriteImage==1):
            changeSpriteImage(Fireball,1)
            showSprite(Fireball)
            xSpeed += 15
            if touching(Fireball,Enemy1):
                hideSprite(Enemy1)
                hideSprite(Sword1)
                hideSprite(Fireball)
                hide=True
            if touching(Fireball,Enemy2):
                hideSprite(Enemy2)
                hideSprite(Sword2)
                hideSprite(Fireball)
                Hide=True
            if touching(Fireball,Enemy3):
                hideSprite(Enemy3)
                hideSprite(Sword3)
                hideSprite(Fireball)
                HIDE=True
        
    xpos += xSpeed
    if xPos > 1180:
        xPos = 1180
    elif xPos < 0:
        xPos = 0

    XPOS += XSpeed
    if XPOS > 2280:
        XPOS=110
        YPOS=670
    elif XPOS < -1000:
        XPOS=110
        YPOS=670

    xPOs += xspeed
    if xPOs > 2280:
        xPOs=407
        YPOs=120
    elif xPOs < -1000:
        xPOs=407
        YPOs=120

    XPoS += XSPEED
    if XPoS > 2280:
        XPoS=940
        YPoS=406
    elif XPoS < -1000:
        XPoS=940
        YPoS=406

    yPos += ySpeed
    if yPos > 585:
        yPos = 585
    elif yPos < 0:
        yPos = 0

    if xpos > 1180:
        xpos = xPos-30
        hideSprite(Fireball)
        xSpeed = 0
    elif xpos < 0:
        xpos = xPos-30
        hideSprite(Fireball)
        xSpeed = 0

    moveSprite(Sword1,XPOS,YPOS)
    moveSprite(Sword3,xPOs,YPOs)
    moveSprite(Sword2,XPoS,YPoS)
    moveSprite(Spyro,xPos,yPos)
    if (spriteImage==0):
        moveSprite(Fireball,xpos,yPos+40)
    elif (spriteImage==1):
        moveSprite(Fireball,xpos+130,yPos+40)

    if touching(Spyro,Key):
        hideSprite(Key)
        locked=False

    if touching(Spyro,Cage) and locked==False:
        hideSprite(Cage)
        XSpeed = 0
        xspeed = 0
        XSPEED = 0
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        xPos = 1180
        yPos = 585
        XPos = 0
        YPos = 450
        xPOS = 590
        xPoS = 167
        XPOs = 755
        yPOS = 170
        XPOS = 110
        YPOS = 670
        xPOs = 407
        YPoS = 406
        YPOs = 120
        XPoS = 940
        xSpeed = 0
        ySpeed = 30
        xpos = xPos-30
        ypos = yPos+40
        spriteImage=0
        hide=False
        Hide=False
        HIDE=False
        locked=True
        moveSprite(Spyro,xPos,yPos)
        moveSprite(Ladder,500,450)
        moveSprite(Ladder2,670,180)
        moveSprite(Fireball,xpos,yPos+40)
        moveSprite(Enemy1,0,620)
        moveSprite(Sword1,XPOS,YPOS)
        moveSprite(Platform,XPos,YPos)
        moveSprite(Platform2,xPOS,YPos)
        moveSprite(Platform3,xPoS,yPOS)
        moveSprite(Platform4,XPOs,yPOS)
        moveSprite(Key,0,362)
        moveSprite(Cage,167,40)
        moveSprite(Dragon,173.5,70)
        moveSprite(Enemy3,297,70)
        moveSprite(Sword3,xPOs,YPOs)
        moveSprite(Enemy2,989,356)
        moveSprite(Sword2,XPoS,YPoS)
        showSprite(Spyro)
        showSprite(Ladder)
        showSprite(Ladder2)
        showSprite(Enemy1)
        showSprite(Enemy2)
        showSprite(Enemy3)
        showSprite(Sword1)
        showSprite(Sword2)
        showSprite(Sword3)
        showSprite(Platform)
        showSprite(Platform2)
        showSprite(Platform3)
        showSprite(Platform4)
        showSprite(Dragon)
        showSprite(Key)
        showSprite(Cage)
        XSpeed = 25
        xspeed = 25
        XSPEED = -25
        Runs += 1

    if (Runs==2):
        setBackgroundImage("/opt/Spyro - Dragon Quest/Castle3.png")
        changeSpriteImage(Dragon,1)

    if (Runs==3):
        setBackgroundImage("/opt/Spyro - Dragon Quest/Castle4.png")
        changeSpriteImage(Dragon,2)

    if (Runs==4):
        setBackgroundImage("/opt/Spyro - Dragon Quest/Castle1.png")
        hideSprite(Spyro)
        killSprite(Ladder)
        killSprite(Ladder2)
        killSprite(Enemy1)
        killSprite(Enemy2)
        killSprite(Enemy3)
        killSprite(Sword1)
        killSprite(Sword2)
        killSprite(Sword3)
        hideSprite(Fireball)
        killSprite(Platform)
        killSprite(Platform2)
        killSprite(Platform3)
        killSprite(Platform4)
        killSprite(Dragon)
        killSprite(Key)
        killSprite(Cage)
        Ripto = makeSprite("/opt/Spyro - Dragon Quest/Ripto.png")
        Magic = makeSprite("/opt/Spyro - Dragon Quest/Magic.png")
        Health = makeSprite("/opt/Spyro - Dragon Quest/Health3.jpg")
        addSpriteImage(Health,"/opt/Spyro - Dragon Quest/Health2.jpg")
        addSpriteImage(Health,"/opt/Spyro - Dragon Quest/Health1.jpg")
        addSpriteImage(Health,"/opt/Spyro - Dragon Quest/Health0.jpg")
        hide=True
        Hide=True
        HIDE=True
        HiDE=False
        Hits=0
        xPos = 1180
        yPos = 585
        XpOs = 191
        YpOs = 530
        xSpeed = 0
        ySpeed = 30
        XsPeed = 30
        YsPeed = 3
        xpos = xPos-30
        ypos = yPos+40
        spriteImage=0
        Runs=5

    if (Runs==5):
        moveSprite(Ripto,0,520)
        moveSprite(Spyro,xPos,yPos)
        moveSprite(Magic,XpOs,YpOs)
        moveSprite(Fireball,xpos,yPos+40)
        moveSprite(Health,0,400)
        showSprite(Spyro)
        showSprite(Ripto)
        showSprite(Magic)
        showSprite(Health)
        if touching(Fireball,Ripto):
            Hits += 1
            if (Hits==5):
                changeSpriteImage(Health,1)
            elif (Hits==10):
                changeSpriteImage(Health,2)
            elif(Hits>=15):
                changeSpriteImage(Health,3)
                HiDE=True
                killSprite(Ripto)
                killSprite(Magic)
                killSprite(Health)
                pause(100)
                killSprite(Spyro)
                killSprite(Fireball)
                setBackgroundImage("/opt/Spyro - Dragon Quest/End.png")
        if touching(Spyro,Ripto) and (HiDE==False):
            hideSprite(Spyro)
            hideSprite(Fireball)
            hideSprite(Ripto)
            hideSprite(Magic)
            hideSprite(Health)
            hide=True
            Hide=True
            HIDE=True
            HiDE=True
            Runs=0
            setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")
        elif touching(Spyro,Magic) and (HiDE==False):
            hideSprite(Spyro)
            hideSprite(Fireball)
            hideSprite(Ripto)
            hideSprite(Magic)
            hideSprite(Health)
            hide=True
            Hide=True
            HIDE=True
            HiDE=True
            Runs=0
            setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")

        YpOs += YsPeed
        XpOs += XsPeed
        if XpOs > 2280:
            XpOs=191
            YpOs=530
        elif XpOs < -1000:
            XpOs=191
            YpOs=530

    if touching(Spyro,Enemy1) and (hide==False):
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        hide=True
        Hide=True
        HIDE=True
        Runs=0
        setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")
    elif touching(Spyro,Enemy2) and (Hide==False):
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        hide=True
        Hide=True
        HIDE=True
        Runs=0
        setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")
    elif touching(Spyro,Enemy3) and (HIDE==False):
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        hide=True
        Hide=True
        HIDE=True
        Runs=0
        setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")
    elif touching(Spyro,Sword1) and (hide==False):
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        hide=True
        Hide=True
        HIDE=True
        Runs=0
        setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")
    elif touching(Spyro,Sword2) and (Hide==False):
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        hide=True
        Hide=True
        HIDE=True
        Runs=0
        setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")
    elif touching(Spyro,Sword3) and (HIDE==False):
        hideSprite(Spyro)
        hideSprite(Ladder)
        hideSprite(Ladder2)
        hideSprite(Enemy1)
        hideSprite(Enemy2)
        hideSprite(Enemy3)
        hideSprite(Sword1)
        hideSprite(Sword2)
        hideSprite(Sword3)
        hideSprite(Fireball)
        hideSprite(Platform)
        hideSprite(Platform2)
        hideSprite(Platform3)
        hideSprite(Platform4)
        hideSprite(Dragon)
        hideSprite(Key)
        hideSprite(Cage)
        hide=True
        Hide=True
        HIDE=True
        Runs=0
        setBackgroundImage("/opt/Spyro - Dragon Quest/GameOver.jpg")

    if touching(Spyro,Platform):
        ySpeed=0

    if touching(Spyro,Platform2):
        ySpeed=0

    if touching(Spyro,Platform3):
        ySpeed=0

    if touching(Spyro,Platform4):
        ySpeed=0

    tick(30)


endWait()
