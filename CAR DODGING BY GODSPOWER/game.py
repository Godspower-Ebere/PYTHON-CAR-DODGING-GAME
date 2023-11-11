import pygame
from pygame.locals import *
import random
import time
pygame.init()

size =width,height=(800,800)
screen=pygame.display.set_mode(size)
screen.fill((0,255,255))
icon=pygame.image.load("files/car1.png")
icon=pygame.transform.scale(icon,(20,100))
pygame.display.set_icon(icon)
pygame.display.set_caption("CAR DODGING BY GODSPOWER")
def gameover():
    gameover=True
    song=pygame.mixer.Sound("files/background music.mp3")
    song.stop()
    while gameover:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    main()

def pause():
    pause=True
    song=pygame.mixer.Sound("files/background music.mp3")
    pygame.mixer.pause()
    key=pygame.key.get_pressed()
    myfont=pygame.font.SysFont("impact",100)
    font=myfont.render("PAUSED",1,((255,255,255)))
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_SPACE:
                    pause=False
                    pygame.mixer.unpause()
                    screen.fill((0,255,255))
    
    screen.blit(font,(width/2,height/2))
    screen.fill((0,255,255))
    pygame.display.update()
def main():
    run=True

    FPS=60
    life=0
    count=0
    score=0
    speed=0
    move=10
    num=28
    level="BEGINNERS"

    song=pygame.mixer.Sound("files/background music.mp3")
    song.play()

    clock=pygame.time.Clock()
    myfont=pygame.font.SysFont("impact",30)


    player=pygame.image.load("files/car1.png")
    playerrect=player.get_rect()
    playerrect.center=520,650

    enemy=pygame.image.load("files/car2.png")
    enemyrect=enemy.get_rect()
    enemyrect.center=290,100
    boom=pygame.mixer.Sound("files/boom.wav")
    jamb=pygame.mixer.Sound("files/punch.wav")
    while run:
        clock.tick(FPS)
        speed+=1
        count+=1
        if count==10:
            score+=1
            count=0  

        enemyrect=enemyrect.move([0,move])
        if speed==500:
            FPS+=5
            print(FPS)
            speed=0
        if score>=500:
            level="INTERMIDATE"
        if score>=1500:
            num=40
            level="BOSS"
              
        pygame.draw.rect(screen,((0,0,0)),(150,0,500,height))
        pygame.draw.rect(screen,((255,255,255)),(width/2,0,10,height))
        pygame.draw.rect(screen,((255,255,255)),(165,0,10,height))
        pygame.draw.rect(screen,((255,255,255)),(625,0,10,height))
        pygame.draw.rect(screen,((0,200,0)),(10,20,130,40))
        pygame.draw.rect(screen,((255,255,255)),(0,345,150,100))
        pygame.draw.rect(screen,((0,200,0)),(0,100,150,40))
        pygame.draw.rect(screen,((255,255,255)),(650,340,200,60))
        pygame.draw.rect(screen,((0,0,0)),(650,600,200,60))
        bar=pygame.draw.rect(screen,((255,0,0)),(15,25,life,30))
        if enemyrect[1]==900:
            life+=2
            if bar.width>=120:
                life=120
            enemyrect[1]=-200
            if random.randint(0,1)==0:
                enemyrect.center=520,-200
            elif random.randint(0,1)==1:
                enemyrect.center=290,-200
        if enemyrect.colliderect(playerrect):
            jamb.play()
            life-=3
            if life<=0:
                life=0
                jamb.stop()
                boom.play()
                print("game over")
                song.stop()
                gameover()
        mylevelfont=pygame.font.SysFont("impact",int(num))
        percent=int(life/120*100/1)
        font=myfont.render(f"{percent}%",1,((255,255,255)))
        scorefont=myfont.render(f"Scores:{score}",1,((255,255,255)))
        levelfont=mylevelfont.render(f"{level}",1,((220,0,0)))
        showfont=mylevelfont.render("LEVELS :",1,((220,0,0)))
        speedfont=myfont.render(f"FPS: {FPS}",1,((220,0,0)))

        myfontg=pygame.font.SysFont("Tahoma",20)
        fontg=myfontg.render("CREATED BY:",1,(255,255,0))
        fontg2=myfontg.render("GODSPOWER",1,(255,255,0))
        
        screen.blit(player,playerrect)
        screen.blit(enemy,enemyrect)
        screen.blit(font,(50,20))
        screen.blit(scorefont,(0,100))
        screen.blit(levelfont,(0,height/2))
        screen.blit(showfont,(0,350))
        screen.blit(speedfont,(width-100,350))
        screen.blit(fontg,(width-150,610))
        screen.blit(fontg2,(width-150,630))
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    playerrect.center=290,650
                if event.key==pygame.K_RIGHT:
                    playerrect.center=520,650
                if event.key==pygame.K_SPACE:
                    pause()
        pygame.display.update()
    pygame.quit()
main()
pygame.quit()








