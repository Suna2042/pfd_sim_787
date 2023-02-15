import pygame
import time
from pfdview import Pfd
from player import Player
from traffic import Traffic

class Game:

    def __init__(self):
        #グループ作成
        self.create_group()

        self.screen=pygame.display.get_surface()
        self.pfd=Pfd(self.screen)

        #自機
        player=Player(self.player_group,24000,240)

        #traffic
        self.timer=450
        

    def create_traffic(self):
        self.timer+=1
        if self.timer>500:
            traffic=Traffic(self.traffic_group,1000,1)
            self.timer=0


    def create_group(self):
        self.player_group=pygame.sprite.GroupSingle()
        self.traffic_group=pygame.sprite.Group()

    def run(self):
        self.time_current=time.time()
        self.pfd.draw(240,34000,360)
        self.player_group.update()

        #self.create_traffic()

        #self.traffic_group.draw(self.screen)
        #self.traffic_group.update()