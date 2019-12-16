import pygame 
import random
import time
import sys

class snake:
    def __init__(self):
        self.head=[300,100]
        self.body=[list([self.head[0],self.head[1]]),
        list([self.head[0]+10,self.head[1]]),
        list([self.head[0]+20,self.head[1]])]
        self.dir='LEFT'
    def changeDirTo(self,d):
        if self.dir!='RIGHT' and d=='LEFT':
            self.dir=d
        elif self.dir!='LEFT' and d=='RIGHT':
            self.dir=d
        elif self.dir!='UP' and d=='DOWN':
            self.dir=d
        elif self.dir!='DOWN' and d=='UP':
            self.dir=d

    def move(self,foodpos):
        if self.dir=='RIGHT':
            self.head[0]+=10
        elif self.dir=='LEFT':
            self.head[0]-=10
        elif self.dir=='DOWN':
            self.head[1]+=10
        elif self.dir=='UP':
            self.head[1]-=10
        self.body.insert(0,list(self.head))
        
        if self.head==foodpos:
            return 1
        else:
            self.body.pop()
            return 0

        
    def collision(self):
        if self.head in self.body[1:]:
            return 1
        elif self.head[0]>490 or self.head[0]<0:
            return 1
        elif self.head[1]>490 or self.head[1]<0:
            return 1
        else:
            return 0
    def getDir(self):
        return self.dir
    def getBody(self):
        return self.body
      
        
        

class foodGenerator:
    def __init__(self):
        self.pos=[random.randrange(0,50)*10,random.randrange(0,50)*10]
        
    def setFood(self,body):
        while True:
            x=[random.randrange(0,50)*10,random.randrange(0,50)*10]
            if x not in body:
                break
        self.pos=x

    def getFood(self):
        return self.pos







def gameover():
    pygame.quit()
    sys.exit()

window=pygame.display.set_mode((500,500))
fps=pygame.time.Clock()



snk=snake()
food=foodGenerator()
score=0
speed=15
pause=0

while(True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameover()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snk.changeDirTo('RIGHT')

            elif event.key==pygame.K_LEFT:
                snk.changeDirTo('LEFT')

            elif event.key==pygame.K_UP:
                snk.changeDirTo('UP')

            elif event.key==pygame.K_DOWN:
                snk.changeDirTo('DOWN')
            elif event.key==pygame.K_ESCAPE:
                gameover()
            elif event.key==pygame.K_w:
                speed+=2
            elif event.key==pygame.K_s:
                speed-=2
    
    window.fill(pygame.Color(100,100,100))
  

    for pos in snk.getBody():
        pygame.draw.rect(window, pygame.Color(0,255,0), pygame.Rect(pos[0],pos[1],10,10))
    f=food.getFood()
    pygame.draw.rect(window, pygame.Color(255,0,0), pygame.Rect(f[0],f[1],10,10))
    x=snk.move(f)
    if x==1:
        f=food.setFood(snk.getBody())
        score+=100

    # print(snk.getBody())
    if pause==0:
        pygame.display.flip()
    if snk.collision()==1:
        # gameover()
        pause=1
    pygame.display.set_caption("Snake Rush   //    SCORE="+str(score))

    
    
    fps.tick(speed)

