import pygame as p
import os as o
import settings as sett
import sprits as spr
import random as r
import pygame.freetype as pf
import base_fyn as bf
p.init()
def stolknovenie ():
    global igra_menu
    for one_ball in balls:
        if player.xitbox.colliderect(one_ball.xitbox):
            if player.xitbox.height >= one_ball.xitbox.height:
                balls.remove(one_ball)
                player.xitbox.width += 5
                player.xitbox.height += 5
            else:
                igra_menu = 1
okno = p.display.set_mode((sett.SHIRINA, sett.BISOTA))
chasi = p.time.Clock()
text_menu = pf.Font(None, 20)
player = spr.Player_ball(sett.NAME, (sett.SHIRINA/2, sett.BISOTA/2))
balls = []   
sobitie = p.USEREVENT
p.time.set_timer(sobitie, sett.DIFFICULT)
a = 0
igra_menu = 0
while a == 0:
    events = p.event.get()
    for one_event in events:
        if one_event.type == sobitie:
            ball = spr.Balls(player)
            balls.append(ball)
        if one_event.type == p.QUIT:
            bf.dobavlenie_obnovlenie(player.name, player.xitbox.width)
            bf.size(player.name, player.xitbox.width)
            a = 1
        if one_event.type == p.KEYDOWN:
            if one_event.key == p.K_f:
                bf.dobavlenie_obnovlenie(player.name, player.xitbox.width)
                bf.size(player.name, player.xitbox.width)
                igra_menu = 0
                balls = []
                player.xitbox.width = 30
                player.xitbox.height = 30
    okno.fill((0,50,0))
    if igra_menu == 0:
        player.prorisovka(okno)
        for one_ball in balls:
            one_ball.prorisovka(okno)
            one_ball.dvizenie()
        player.dvizenie()
        stolknovenie()
    else:
        text_menu.render_to(okno,(sett.SHIRINA/2,sett.BISOTA/2),"Вы проиграли, нажмите на F для новой игры.")
    p.display.update()
    chasi.tick(120)
    