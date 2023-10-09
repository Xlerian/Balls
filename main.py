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
text_chet = pf.Font(None, 20)
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
            if bf.otdacha(player.name) < player.xitbox.width:
                bf.dobavlenie_obnovlenie(player.name, player.xitbox.width)
            # bf.size(player.name, player.xitbox.width)
            a = 1
        if one_event.type == p.KEYDOWN:
            if one_event.key == p.K_f:
                otdacha = bf.otdacha(player.name)
                # print(otdacha)
                # print(player.xitbox.w)
                if bf.otdacha(player.name) < player.xitbox.width:
                    bf.dobavlenie_obnovlenie(player.name, player.xitbox.width)
                # bf.size(player.name, player.xitbox.width)
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
        text_chet.render_to(okno,(sett.BISOTA/2 - 100,1000),f"Счёт:{bf.chet_igroka(player.name)},текущий счёт:{player.xitbox.w}", (250,0,0))
    else:
        text_menu.render_to(okno,(sett.SHIRINA/2,sett.BISOTA/2,),"Вы проиграли, нажмите на F для новой игры.", (250,0,0))
    p.display.update()
    chasi.tick(120)
    