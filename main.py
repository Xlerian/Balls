import pygame as p
import os as o
import settings as sett
import sprits as spr
import random as r
import pygame.freetype as pf
p.init()
okno = p.display.set_mode((sett.SHIRINA, sett.BISOTA))
chasi = p.time.Clock()
a = 0
while a == 0:
    events = p.event.get()
    for one_event in events:
        if one_event.type == p.QUIT:
            a = 1
    okno.fill((0,50,0))
    p.display.update()
    chasi.tick(10)