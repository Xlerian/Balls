import pygame as p
import os as o
import settings as sett
import sprits as spr
import random as r
import pygame.freetype as pf
import base_fyn as bf
p.init()
def stolknovenie ():
    for one_ball in balls:
        if player.xitbox.colliderect(one_ball.xitbox):
            if player.xitbox.height > one_ball.xitbox.height:
                balls.remove(one_ball)
                player.xitbox.width += 5
                player.xitbox.height += 5
okno = p.display.set_mode((sett.SHIRINA, sett.BISOTA))
chasi = p.time.Clock()
player = spr.Player_ball(sett.NAME, (sett.SHIRINA/2, sett.BISOTA/2))
balls = []   
sobitie = p.USEREVENT
p.time.set_timer(sobitie, 500)
a = 0
while a == 0:
    events = p.event.get()
    for one_event in events:
        if one_event.type == sobitie:
            ball = spr.Balls(player)
            balls.append(ball)
        if one_event.type == p.QUIT:
            bf.dobavlenie_obnovlenie(player.name, player.xitbox.width)
            a = 1
    okno.fill((0,50,0))
    player.prorisovka(okno)
    for one_ball in balls:
        one_ball.prorisovka(okno)
        one_ball.dvizenie()
    player.dvizenie()
    stolknovenie()
    p.display.update()
    chasi.tick(120)
    