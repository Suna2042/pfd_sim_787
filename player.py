import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,groups,init_alt,init_spd):
        super().__init__(groups)

        self.alt=init_alt
        self.spd=init_spd
        self.hdg=360
        self.vs=0
        self.pitch=0

    def pilot(self):
        pass
        

    def update(self):
        pass


        