import pygame
import random
import math

class Traffic(pygame.sprite.Sprite):

    def __init__(self,groups,spd,alt):
        super().__init__(groups)
        hdg_list=range(-90,90)
        self.heading=random.choice(hdg_list)
        self.distance=10 #ピクセルに直すには:distance*(95/5)(nm)

        self.x_init=300+self.distance*(95/5)*math.sin(self.heading*math.pi/180)
        self.y_init=810-self.distance*(95/5)*math.cos(self.heading*math.pi/180)


        
        

        #ICON
        self.image=pygame.Surface((20,20))
        self.image.fill((255,255,0))
        self.rect=self.image.get_rect(center=(self.x_init,self.y_init))

        #MOVE
        move_list=[1,-1]
        self.speed=spd

            #位置計算
    def move(self): 
        self.distance -= self.speed/(60*60*30)
        self.x=300+self.distance*(95/5)*math.sin(self.heading*math.pi/180)
        self.y=810-self.distance*(95/5)*math.cos(self.heading*math.pi/180)

    def move_rect(self):
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        self.move()
        self.move_rect()