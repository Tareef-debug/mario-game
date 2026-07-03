import pygame
import random
pygame.init()

screen = pygame.display.set_mode((600,600)) #width 1st height 2nd

pygame.display.set_caption("Mario Game")

score_font=pygame.font.SysFont(None,30)#30-fontsize
over_font= pygame.font.SysFont(None,60)

Mario=pygame.transform.scale(pygame.image.load("mario.png"),(30,45))
coin=pygame.transform.scale(pygame.image.load("coin.png"),(30,30))
gnome=pygame.transform.scale(pygame.image.load("gnome.png"),(30,30))

px,py=300,300
gnomes=[[100,400],[200,250],[500,450],[150,78]]
coins=[]
for x in range(60,550,60):
    for y in range(60,550,60):
        coins.append([x,y])
score=0
lives=5
game_over = False
win=False
while True:
    screen.fill(pygame.Color("black"))
    #get events
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()#close pygame
    #check if game over
    if not game_over and not win:
        keys = pygame.key.get_pressed()
        #W A S D keys
        if keys[pygame.K_LEFT]:
            px-=0.75
        if keys[pygame.K_RIGHT]:
            px+=0.75
        if keys[pygame.K_UP]:
            py-=0.75
        if keys[pygame.K_DOWN]:
            py+=0.75
        #eat the food
        for c in coins:
            if abs(px-c[0])<30 and abs(py-c[1])<30:
                coins.remove(c)
                score+=1
        for g in gnomes:
            g[0]+=random.choice([-2,2])
            g[1]+=random.choice([-2,2])
            #keep the ghosts on the screen
            g[0]=max(0,min(575,g[0]))
            g[1]=max(0,min(575,g[1]))
            #ghost colliseion
            if abs(px-g[0])<20 and abs(py-g[1])<15:
                lives-=1
                px,py=300,300
        if lives<=0:
            game_over=True
        if len(coins)==0:
            win=True
    #draw everything
    screen.blit(Mario,(px,py))
    for g in gnomes:
        screen.blit(gnome,g)
    for c in coins:
        screen.blit(coin,c)
    screen.blit(score_font.render("Score:"+str(score),True,(255,255,0)),(10,10))
    screen.blit(score_font.render("Lives:"+str(lives),True,(255,255,0)),(100,10))
    if game_over:
        screen.blit(over_font.render("GAME OVER",True,(189,35,0)),(300,300))
    if win:
        screen.blit(over_font.render("YOU WIN",True,(189,35,0)),(300,300))
    pygame.display.update()
