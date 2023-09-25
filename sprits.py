import pygame as p
import os as o
import settings as sett
import random as r
import pygame.freetype as pf
import base_fyn as bf
class Player_ball():
    def __init__(self, name, x_y):
        self.skorost = 3
        self.name = name
        self.x_y = x_y
        self.xitbox = p.Rect(self.x_y,(30,30))
    

    def prorisovka(self, okno):
        p.draw.ellipse(okno,(0,250,0),self.xitbox)
    
    def dvizenie(self):
        self.xitbox.center = p.mouse.get_pos()

class Balls():
    def __init__(self, player):
        self.skorostx = r.randint(-2,2)
        self.skorosty = r.randint(-2,2)
        a = player.xitbox.w - 5
        b = player.xitbox.h + 5
        self.color = (r.randint(0,250),r.randint(0,250),r.randint(0,250))
        size = r.randint(a, b)
        self.random_xy()
        self.xitbox = p.Rect(self.x_y,(size,size))
    
    def prorisovka(self, okno):
        p.draw.ellipse(okno,self.color,self.xitbox)
    
    def random_xy (self):
        rand = r.randint(1,4)
        if rand == 1:
            self.x_y =((40,r.randint(0,sett.BISOTA)))
            self.skorostx = r.randint(0,2)
            self.skorosty = r.randint(-2,2)
        elif rand == 2:
            self.x_y =((sett.SHIRINA - 40,r.randint(0,sett.BISOTA)))
            self.skorostx = r.randint(-2,0)
            self.skorosty = r.randint(-2,2)
        elif rand == 3:
            self.x_y =((r.randint(0,sett.SHIRINA), 40))
            self.skorostx = r.randint(-2,2)
            self.skorosty = r.randint(0,2)
        elif rand == 4:
            self.x_y =((r.randint(0,sett.SHIRINA), sett.BISOTA - 40))
            self.skorostx = r.randint(-2,2)
            self.skorosty = r.randint(-2,0)
    
    def dvizenie (self):
        self.xitbox.x += self.skorostx
        self.xitbox.y += self.skorosty