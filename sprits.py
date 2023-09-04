import pygame as p
import os as o
import settings as sett
import random as r
import pygame.freetype as pf
class Player_ball():
    def __init__(self, name, x_y):
        self.skorost = 3
        self.size = 1
        self.name = name
        self.x_y = x_y
        self.xitbox = p.Rect(self.x_y,(30,30))
    

    def prorisovka(self, okno):
        p.draw.ellipse(okno,(0,250,0),self.xitbox)
    
    def dvizenie(self):
        self.xitbox.center = p.mouse.get_pos()
        self.xitbox.height +=1
        self.xitbox.width +=1