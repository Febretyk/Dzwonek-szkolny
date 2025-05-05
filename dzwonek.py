import pygame

pygame.init()

okno = pygame.display.set_mode((450, 625))
pygame.display.set_caption("Dzwonek")
zegar = pygame.time.Clock()

tlo = pygame.image.load("zeszyt.png").convert_alpha()
tloB = pygame.image.load("zeszytB.png").convert_alpha()
tloC = pygame.image.load("zeszytC.png").convert_alpha()
tloD = pygame.image.load("zeszytD.png").convert_alpha()
tloE = pygame.image.load("zeszytE.png").convert_alpha()

tloB_width = tloB.get_width()

tlox = 0
tloy = 0

okno = pygame.display.set_mode((450, 625))

guzik = pygame.image.load("dodaj.png").convert_alpha()
guzik_rect = guzik.get_rect(midbottom = (225,550))

pon = pygame.image.load("tydzień/pon.png").convert_alpha()
pon_rect = pon.get_rect(midbottom = (70, 30))
wt = pygame.image.load("tydzień/wt.png").convert_alpha()
wt_rect = wt.get_rect(midbottom = (150, 30))
sr = pygame.image.load("tydzień/sro.png").convert_alpha()
sr_rect = sr.get_rect(midbottom = (230, 30))
cz = pygame.image.load("tydzień/czw.png").convert_alpha()
cz_rect = cz.get_rect(midbottom = (310, 30))
pt = pygame.image.load("tydzień/pt.png").convert_alpha()
pt_rect = pt.get_rect(midbottom = (390, 30))

lekcja = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja6 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja7 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja8 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja9 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja10 = pygame.image.load("LEKCJA2.png").convert_alpha()

lekcja2_1 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_2 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_3 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_4 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_5 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_6 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_7 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_8 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_9 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja2_10 = pygame.image.load("LEKCJA2.png").convert_alpha()

lekcja3_1 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_2 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_3 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_4 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_5 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_6 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_7 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_8 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_9 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja3_10 = pygame.image.load("LEKCJA2.png").convert_alpha()

lekcja4_1 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_2 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_3 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_4 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_5 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_6 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_7 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_8 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_9 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja4_10 = pygame.image.load("LEKCJA2.png").convert_alpha()

lekcja5_1 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_2 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_3 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_4 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_5 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_6 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_7 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_8 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_9 = pygame.image.load("LEKCJA2.png").convert_alpha()
lekcja5_10 = pygame.image.load("LEKCJA2.png").convert_alpha()

lekcjawcisnieta = False
lekcja2wcisnieta = False
lekcja3wcisnieta = False
lekcja4wcisnieta = False
lekcja5wcisnieta = False
lekcja6wcisnieta = False
lekcja7wcisnieta = False
lekcja8wcisnieta = False
lekcja9wcisnieta = False
lekcja10wcisnieta = False
lekcja2_1wcisnieta = False
lekcja2_2wcisnieta = False
lekcja2_3wcisnieta = False
lekcja2_4wcisnieta = False
lekcja2_5wcisnieta = False
lekcja2_6wcisnieta = False
lekcja2_7wcisnieta = False
lekcja2_8wcisnieta = False
lekcja2_9wcisnieta = False
lekcja2_10wcisnieta = False
lekcja3_1wcisnieta = False
lekcja3_2wcisnieta = False
lekcja3_3wcisnieta = False
lekcja3_4wcisnieta = False
lekcja3_5wcisnieta = False
lekcja3_6wcisnieta = False
lekcja3_7wcisnieta = False
lekcja3_8wcisnieta = False
lekcja3_9wcisnieta = False
lekcja3_10wcisnieta = False
lekcja4_1wcisnieta = False
lekcja4_2wcisnieta = False
lekcja4_3wcisnieta = False
lekcja4_4wcisnieta = False
lekcja4_5wcisnieta = False
lekcja4_6wcisnieta = False
lekcja4_7wcisnieta = False
lekcja4_8wcisnieta = False
lekcja4_9wcisnieta = False
lekcja4_10wcisnieta = False
lekcja5_1wcisnieta = False
lekcja5_2wcisnieta = False
lekcja5_3wcisnieta = False
lekcja5_4wcisnieta = False
lekcja5_5wcisnieta = False
lekcja5_6wcisnieta = False
lekcja5_7wcisnieta = False
lekcja5_8wcisnieta = False
lekcja5_9wcisnieta = False
lekcja5_10wcisnieta = False


lekcjay = 150
lekcjax = 225

font = pygame.font.Font("couri.ttf", 28)
text = ""
text2 = ""
text3 = ""
text4 = ""
text5 = ""
text6 = ""
text7 = ""
text8 = ""
text9 = ""
text10 = ""
wtext = ""
wtext2 = ""
wtext3 = ""
wtext4 = ""
wtext5 = ""
wtext6 = ""
wtext7 = ""
wtext8 = ""
wtext9 = ""
wtext10 = ""
stext = ""
stext2 = ""
stext3 = ""
stext4 = ""
stext5 = ""
stext6 = ""
stext7 = ""
stext8 = ""
stext9 = ""
stext10 = ""
ctext = ""
ctext2 = ""
ctext3 = ""
ctext4 = ""
ctext5 = ""
ctext6 = ""
ctext7 = ""
ctext8 = ""
ctext9 = ""
ctext10 = ""
ptext = ""
ptext2 = ""
ptext3 = ""
ptext4 = ""
ptext5 = ""
ptext6 = ""
ptext7 = ""
ptext8 = ""
ptext9 = ""
ptext10 = ""

czarny = (0, 0, 0)

running = True

poniedzialek = True
wtorek = False
sroda = False
czwartek = False
piatek = False

plekcje = 0
wlekcje = 0
slekcje = 0
clekcje = 0
ptlekcje = 0




while running:
    tloBx = tlox+450
    tloCx = tloBx+450
    tloDx = tloCx+450
    tloEx = tloDx+450

    liczbatekstu = len(text)
    liczbatekstu2 = len(text2)
    liczbatekstu3 = len(text3)
    liczbatekstu4 = len(text4)
    liczbatekstu5 = len(text5)
    liczbatekstu6 = len(text6)
    liczbatekstu7 = len(text7)
    liczbatekstu8 = len(text8)
    liczbatekstu9 = len(text9)
    liczbatekstu10 = len(text10)

    liczbawtekstu = len(wtext)
    liczbawtekstu2 = len(wtext2)
    liczbawtekstu3 = len(wtext3)
    liczbawtekstu4 = len(wtext4)
    liczbawtekstu5 = len(wtext5)
    liczbawtekstu6 = len(wtext6)
    liczbawtekstu7 = len(wtext7)
    liczbawtekstu8 = len(wtext8)
    liczbawtekstu9 = len(wtext9)
    liczbawtekstu10 = len(wtext10)

    liczbastekstu = len(stext)
    liczbastekstu2 = len(stext2)
    liczbastekstu3 = len(stext3)
    liczbastekstu4 = len(stext4)
    liczbastekstu5 = len(stext5)
    liczbastekstu6 = len(stext6)
    liczbastekstu7 = len(stext7)
    liczbastekstu8 = len(stext8)
    liczbastekstu9 = len(stext9)
    liczbastekstu10 = len(stext10)

    liczbactekstu = len(ctext)
    liczbactekstu2 = len(ctext2)
    liczbactekstu3 = len(ctext3)
    liczbactekstu4 = len(ctext4)
    liczbactekstu5 = len(ctext5)
    liczbactekstu6 = len(ctext6)
    liczbactekstu7 = len(ctext7)
    liczbactekstu8 = len(ctext8)
    liczbactekstu9 = len(ctext9)
    liczbactekstu10 = len(ctext10)

    liczbaptekstu = len(ptext)
    liczbaptekstu2 = len(ptext2)
    liczbaptekstu3 = len(ptext3)
    liczbaptekstu4 = len(ptext4)
    liczbaptekstu5 = len(ptext5)
    liczbaptekstu6 = len(ptext6)
    liczbaptekstu7 = len(ptext7)
    liczbaptekstu8 = len(ptext8)
    liczbaptekstu9 = len(ptext9)
    liczbaptekstu10 = len(ptext10)

    
    okno.fill((255, 255, 255))
    okno.blit(tlo, (tlox, tloy))
    okno.blit(tloB, (tloBx, tloy))
    okno.blit(tloC, (tloCx, tloy))
    okno.blit(tloC, (tloDx, tloy))
    okno.blit(tloE, (tloEx, tloy))

    
    lekcja_rect1 = lekcja.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay))
    lekcja_rect2 = lekcja2.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+150))
    lekcja_rect3 = lekcja3.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+300))
    lekcja_rect4 = lekcja4.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+450))
    lekcja_rect5 = lekcja5.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+600))
    lekcja_rect6 = lekcja6.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+750))
    lekcja_rect7 = lekcja7.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+900))
    lekcja_rect8 = lekcja8.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+1050))
    lekcja_rect9 = lekcja9.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+1200))
    lekcja_rect10 = lekcja10.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay+1350))
    okno.blit(lekcja, lekcja_rect1)
    okno.blit(lekcja2, lekcja_rect2)
    okno.blit(lekcja3, lekcja_rect3)
    okno.blit(lekcja4, lekcja_rect4)
    okno.blit(lekcja5, lekcja_rect5)
    okno.blit(lekcja6, lekcja_rect6)
    okno.blit(lekcja7, lekcja_rect7)
    okno.blit(lekcja8, lekcja_rect8)
    okno.blit(lekcja9, lekcja_rect9)
    okno.blit(lekcja10, lekcja_rect10)

    
    lekcja_rect2_1 = lekcja2_1.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay))
    lekcja_rect2_2 = lekcja2_2.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+150))
    lekcja_rect2_3 = lekcja2_3.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+300))
    lekcja_rect2_4 = lekcja2_4.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+450))
    lekcja_rect2_5 = lekcja2_5.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+600))
    lekcja_rect2_6 = lekcja2_6.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+750))
    lekcja_rect2_7 = lekcja2_7.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+900))
    lekcja_rect2_8 = lekcja2_8.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+1050))
    lekcja_rect2_9 = lekcja2_9.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+1200))
    lekcja_rect2_10 = lekcja2_10.get_rect(midbottom = (tloBx+lekcjax, tloy+lekcjay+1350))
    okno.blit(lekcja2_1, lekcja_rect2_1)
    okno.blit(lekcja2_2, lekcja_rect2_2)
    okno.blit(lekcja2_3, lekcja_rect2_3)
    okno.blit(lekcja2_4, lekcja_rect2_4)
    okno.blit(lekcja2_5, lekcja_rect2_5)
    okno.blit(lekcja2_6, lekcja_rect2_6)
    okno.blit(lekcja2_7, lekcja_rect2_7)
    okno.blit(lekcja2_8, lekcja_rect2_8)
    okno.blit(lekcja2_9, lekcja_rect2_9)
    okno.blit(lekcja2_10, lekcja_rect2_10)


    lekcja_rect3_1 = lekcja3_1.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay))
    lekcja_rect3_2 = lekcja3_2.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+150))
    lekcja_rect3_3 = lekcja3_3.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+300))
    lekcja_rect3_4 = lekcja3_4.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+450))
    lekcja_rect3_5 = lekcja3_5.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+600))
    lekcja_rect3_6 = lekcja3_6.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+750))
    lekcja_rect3_7 = lekcja3_7.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+900))
    lekcja_rect3_8 = lekcja3_8.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+1050))
    lekcja_rect3_9 = lekcja3_9.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+1200))
    lekcja_rect3_10 = lekcja3_10.get_rect(midbottom = (tloCx+lekcjax, tloy+lekcjay+1350))
    okno.blit(lekcja3_1, lekcja_rect3_1)
    okno.blit(lekcja3_2, lekcja_rect3_2)
    okno.blit(lekcja3_3, lekcja_rect3_3)
    okno.blit(lekcja3_4, lekcja_rect3_4)
    okno.blit(lekcja3_5, lekcja_rect3_5)
    okno.blit(lekcja3_6, lekcja_rect3_6)
    okno.blit(lekcja3_7, lekcja_rect3_7)
    okno.blit(lekcja3_8, lekcja_rect3_8)
    okno.blit(lekcja3_9, lekcja_rect3_9)
    okno.blit(lekcja3_10, lekcja_rect3_10)


    lekcja_rect4_1 = lekcja4_1.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay))
    lekcja_rect4_2 = lekcja4_2.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+150))
    lekcja_rect4_3 = lekcja4_3.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+300))
    lekcja_rect4_4 = lekcja4_4.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+450))
    lekcja_rect4_5 = lekcja4_5.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+600))
    lekcja_rect4_6 = lekcja4_6.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+750))
    lekcja_rect4_7 = lekcja4_7.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+900))
    lekcja_rect4_8 = lekcja4_8.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+1050))
    lekcja_rect4_9 = lekcja4_9.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+1200))
    lekcja_rect4_10 = lekcja4_10.get_rect(midbottom = (tloDx+lekcjax, tloy+lekcjay+1350))
    okno.blit(lekcja4_1, lekcja_rect4_1)
    okno.blit(lekcja4_2, lekcja_rect4_2)
    okno.blit(lekcja4_3, lekcja_rect4_3)
    okno.blit(lekcja4_4, lekcja_rect4_4)
    okno.blit(lekcja4_5, lekcja_rect4_5)
    okno.blit(lekcja4_6, lekcja_rect4_6)
    okno.blit(lekcja4_7, lekcja_rect4_7)
    okno.blit(lekcja4_8, lekcja_rect4_8)
    okno.blit(lekcja4_9, lekcja_rect4_9)
    okno.blit(lekcja4_10, lekcja_rect4_10)

    lekcja_rect5_1 = lekcja5_1.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay))
    lekcja_rect5_2 = lekcja5_2.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+150))
    lekcja_rect5_3 = lekcja5_3.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+300))
    lekcja_rect5_4 = lekcja5_4.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+450))
    lekcja_rect5_5 = lekcja5_5.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+600))
    lekcja_rect5_6 = lekcja5_6.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+750))
    lekcja_rect5_7 = lekcja5_7.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+900))
    lekcja_rect5_8 = lekcja5_8.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+1050))
    lekcja_rect5_9 = lekcja5_9.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+1200))
    lekcja_rect5_10 = lekcja5_10.get_rect(midbottom = (tloEx+lekcjax, tloy+lekcjay+1350))
    okno.blit(lekcja5_1, lekcja_rect5_1)
    okno.blit(lekcja5_2, lekcja_rect5_2)
    okno.blit(lekcja5_3, lekcja_rect5_3)
    okno.blit(lekcja5_4, lekcja_rect5_4)
    okno.blit(lekcja5_5, lekcja_rect5_5)
    okno.blit(lekcja5_6, lekcja_rect5_6)
    okno.blit(lekcja5_7, lekcja_rect5_7)
    okno.blit(lekcja5_8, lekcja_rect5_8)
    okno.blit(lekcja5_9, lekcja_rect5_9)
    okno.blit(lekcja5_10, lekcja_rect5_10)

    
    okno.blit(guzik, guzik_rect)
    okno.blit(pon, pon_rect)
    okno.blit(wt, wt_rect)
    okno.blit(sr, sr_rect)
    okno.blit(cz, cz_rect)
    okno.blit(pt, pt_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                dx, dy = event.rel
                tloy += dy
                


        elif event.type == pygame.MOUSEBUTTONDOWN:

            if guzik_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    print("PRINT")
                    if poniedzialek == True:
                        if plekcje == 0:
                            lekcja = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcjawcisnieta = True
                            plekcje += 1
                        elif plekcje == 1:
                            lekcja2 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2wcisnieta = True
                            plekcje += 1
                        elif plekcje == 2:
                            lekcja3 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3wcisnieta = True
                            plekcje += 1
                        elif plekcje == 3:
                            lekcja4 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4wcisnieta = True
                            plekcje += 1
                        elif plekcje == 4:
                            lekcja5 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5wcisnieta = True
                            plekcje += 1
                        elif plekcje == 5:
                            lekcja6 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja6wcisnieta = True
                            plekcje += 1
                        elif plekcje == 6:
                            lekcja7 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja7wcisnieta = True
                            plekcje += 1
                        elif plekcje == 7:
                            lekcja8 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja8wcisnieta = True
                            plekcje += 1
                        elif plekcje == 8:
                            lekcja9 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja9wcisnieta = True
                            plekcje +=1
                        elif plekcje == 9:
                            lekcja10 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja10wcisnieta = True
                            plekcje +=1
                            
                    elif wtorek == True:
                        if wlekcje == 0:
                            lekcja2_1 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_1wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 1:
                            lekcja2_2 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_2wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 2:
                            lekcja2_3 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_3wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 3:
                            lekcja2_4 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_4wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 4:
                            lekcja2_5 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_5wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 5:
                            lekcja2_6 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_6wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 6:
                            lekcja2_7 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_7wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 7:
                            lekcja2_8 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_8wcisnieta = True
                            wlekcje += 1
                        elif wlekcje == 8:
                            lekcja2_9 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_9wcisnieta = True
                            wlekcje +=1
                        elif wlekcje == 9:
                            lekcja2_10 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja2_10wcisnieta = True
                            wlekcje +=1
                            
                    elif sroda == True:
                        if slekcje == 0:
                            lekcja3_1 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_1wcisnieta = True
                            slekcje += 1
                        elif slekcje == 1:
                            lekcja3_2 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_2wcisnieta = True
                            slekcje += 1
                        elif slekcje == 2:
                            lekcja3_3 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_3wcisnieta = True
                            slekcje += 1
                        elif slekcje == 3:
                            lekcja3_4 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_4wcisnieta = True
                            slekcje += 1
                        elif slekcje == 4:
                            lekcja3_5 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_5wcisnieta = True
                            slekcje += 1
                        elif slekcje == 5:
                            lekcja3_6 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_6wcisnieta = True
                            slekcje += 1
                        elif slekcje == 6:
                            lekcja3_7 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_7wcisnieta = True
                            slekcje += 1
                        elif slekcje == 7:
                            lekcja3_8 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_8wcisnieta = True
                            slekcje += 1
                        elif slekcje == 8:
                            lekcja3_9 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_9wcisnieta = True
                            slekcje +=1
                        elif slekcje == 9:
                            lekcja3_10 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja3_10wcisnieta = True
                            slekcje +=1

                    elif czwartek == True:
                        if clekcje == 0:
                            lekcja4_1 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_1wcisnieta = True
                            clekcje += 1
                        elif clekcje == 1:
                            lekcja4_2 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_2wcisnieta = True
                            clekcje += 1
                        elif clekcje == 2:
                            lekcja4_3 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_3wcisnieta = True
                            clekcje += 1
                        elif clekcje == 3:
                            lekcja4_4 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_4wcisnieta = True
                            clekcje += 1
                        elif clekcje == 4:
                            lekcja4_5 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_5wcisnieta = True
                            clekcje += 1
                        elif clekcje == 5:
                            lekcja4_6 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_6wcisnieta = True
                            clekcje += 1
                        elif clekcje == 6:
                            lekcja4_7 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_7wcisnieta = True
                            clekcje += 1
                        elif clekcje == 7:
                            lekcja4_8 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_8wcisnieta = True
                            clekcje += 1
                        elif clekcje == 8:
                            lekcja4_9 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_9wcisnieta = True
                            clekcje +=1
                        elif clekcje == 9:
                            lekcja4_10 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja4_10wcisnieta = True
                            clekcje +=1
                            
                    elif piatek == True:
                        if ptlekcje == 0:
                            lekcja5_1 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_1wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 1:
                            lekcja5_2 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_2wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 2:
                            lekcja5_3 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_3wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 3:
                            lekcja5_4 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_4wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 4:
                            lekcja5_5 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_5wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 5:
                            lekcja5_6 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_6wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 6:
                            lekcja5_7 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_7wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 7:
                            lekcja5_8 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_8wcisnieta = True
                            ptlekcje += 1
                        elif ptlekcje == 8:
                            lekcja5_9 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_9wcisnieta = True
                            ptlekcje +=1
                        elif ptlekcje == 9:
                            lekcja5_10 = pygame.image.load("LEKCJA.png").convert_alpha()
                            lekcja5_10wcisnieta = True
                            ptlekcje +=1
            
                    
                    

            


            if pon_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = 0
                    print("co do sigmy")
                    poniedzialek = True
                    wtorek = False
                    sroda = False
                    czwartek = False
                    piatek = False
                    lekcjawcisnieta = False
                    lekcja2wcisnieta = False
                    lekcja3wcisnieta = False
                    lekcja4wcisnieta = False
                    lekcja5wcisnieta = False
                    lekcja6wcisnieta = False
                    lekcja7wcisnieta = False
                    lekcja8wcisnieta = False
                    lekcja9wcisnieta = False
                    lekcja10wcisnieta = False

                        


            if wt_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -450
                    print("co do czego")
                    poniedzialek = False
                    wtorek = True
                    sroda = False
                    czwartek = False
                    piatek = False
                    lekcja2_1wcisnieta = False
                    lekcja2_2wcisnieta = False
                    lekcja2_3wcisnieta = False
                    lekcja2_4wcisnieta = False
                    lekcja2_5wcisnieta = False
                    lekcja2_6wcisnieta = False
                    lekcja2_7wcisnieta = False
                    lekcja2_8wcisnieta = False
                    lekcja2_9wcisnieta = False
                    lekcja2_10wcisnieta = False
                    
            if sr_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -900
                    print("errr...")
                    poniedzialek = False
                    wtorek = False
                    sroda = True
                    czwartek = False
                    piatek = False
                    lekcja3_1wcisnieta = False
                    lekcja3_2wcisnieta = False
                    lekcja3_3wcisnieta = False
                    lekcja3_4wcisnieta = False
                    lekcja3_5wcisnieta = False
                    lekcja3_6wcisnieta = False
                    lekcja3_7wcisnieta = False
                    lekcja3_8wcisnieta = False
                    lekcja3_9wcisnieta = False
                    lekcja3_10wcisnieta = False
                    
            if cz_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -1350
                    print("ummm")
                    poniedzialek = False
                    wtorek = False
                    sroda = False
                    czwartek = True
                    piatek = False
                    lekcja4_1wcisnieta = False
                    lekcja4_2wcisnieta = False
                    lekcja4_3wcisnieta = False
                    lekcja4_4wcisnieta = False
                    lekcja4_5wcisnieta = False
                    lekcja4_6wcisnieta = False
                    lekcja4_7wcisnieta = False
                    lekcja4_8wcisnieta = False
                    lekcja4_9wcisnieta = False
                    lekcja4_10wcisnieta = False


            if pt_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -1800
                    print("co do śmigła")
                    poniedzialek = False
                    wtorek = False
                    sroda = False
                    czwartek = False
                    piatek = True
                    lekcja5_1wcisnieta = False
                    lekcja5_2wcisnieta = False
                    lekcja5_3wcisnieta = False
                    lekcja5_4wcisnieta = False
                    lekcja5_5wcisnieta = False
                    lekcja5_6wcisnieta = False
                    lekcja5_7wcisnieta = False
                    lekcja5_8wcisnieta = False
                    lekcja5_9wcisnieta = False
                    lekcja5_10wcisnieta = False

            if lekcja_rect1.collidepoint(event.pos):
                if lekcjawcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 0:
                            print("test")
                            lekcjawcisnieta = True
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect2.collidepoint(event.pos):
                if lekcja2wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 1:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = True
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect3.collidepoint(event.pos):
                if lekcja3wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 2:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = True
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect4.collidepoint(event.pos):
                if lekcja4wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 3:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = True
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect5.collidepoint(event.pos):
                if lekcja5wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 4:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = True
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect6.collidepoint(event.pos):
                if lekcja6wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 5:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = True
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect7.collidepoint(event.pos):
                if lekcja7wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 6:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = True
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect8.collidepoint(event.pos):
                if lekcja8wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 7:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = True
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = False
            if lekcja_rect9.collidepoint(event.pos):
                if lekcja9wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 8:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = True
                            lekcja10wcisnieta = False
            if lekcja_rect10.collidepoint(event.pos):
                if lekcja10wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if plekcje > 9:
                            lekcjawcisnieta = False
                            lekcja2wcisnieta = False
                            lekcja3wcisnieta = False
                            lekcja4wcisnieta = False
                            lekcja5wcisnieta = False
                            lekcja6wcisnieta = False
                            lekcja7wcisnieta = False
                            lekcja8wcisnieta = False
                            lekcja9wcisnieta = False
                            lekcja10wcisnieta = True
                    
            if lekcja_rect2_1.collidepoint(event.pos):
                if lekcja2_1wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 0:
                            lekcja2_1wcisnieta = True
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_2.collidepoint(event.pos):
                if lekcja2_2wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 1:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = True
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_3.collidepoint(event.pos):
                if lekcja2_3wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 2:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = True
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_4.collidepoint(event.pos):
                if lekcja2_4wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 3:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = True
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_5.collidepoint(event.pos):
                if lekcja2_5wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 4:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = True
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_6.collidepoint(event.pos):
                if lekcja2_6wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 5:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = True
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_7.collidepoint(event.pos):
                if lekcja2_7wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 6:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = True
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_8.collidepoint(event.pos):
                if lekcja2_8wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 7:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = True
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_9.collidepoint(event.pos):
                if lekcja2_9wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 8:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = True
                            lekcja2_10wcisnieta = False
            if lekcja_rect2_10.collidepoint(event.pos):
                if lekcja2_10wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if wlekcje > 9:
                            lekcja2_1wcisnieta = False
                            lekcja2_2wcisnieta = False
                            lekcja2_3wcisnieta = False
                            lekcja2_4wcisnieta = False
                            lekcja2_5wcisnieta = False
                            lekcja2_6wcisnieta = False
                            lekcja2_7wcisnieta = False
                            lekcja2_8wcisnieta = False
                            lekcja2_9wcisnieta = False
                            lekcja2_10wcisnieta = True

            if lekcja_rect3_1.collidepoint(event.pos):
                if lekcja3_1wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 0:
                            lekcja3_1wcisnieta = True
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_2.collidepoint(event.pos):
                if lekcja3_2wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 1:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = True
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_3.collidepoint(event.pos):
                if lekcja3_3wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 2:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = True
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_4.collidepoint(event.pos):
                if lekcja3_4wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 3:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = True
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_5.collidepoint(event.pos):
                if lekcja3_5wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 4:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = True
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_6.collidepoint(event.pos):
                if lekcja3_6wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 5:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = True
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_7.collidepoint(event.pos):
                if lekcja3_7wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 6:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = True
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_8.collidepoint(event.pos):
                if lekcja3_8wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 7:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = True
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_9.collidepoint(event.pos):
                if lekcja3_9wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 8:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = True
                            lekcja3_10wcisnieta = False
            if lekcja_rect3_10.collidepoint(event.pos):
                if lekcja3_10wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if slekcje > 9:
                            lekcja3_1wcisnieta = False
                            lekcja3_2wcisnieta = False
                            lekcja3_3wcisnieta = False
                            lekcja3_4wcisnieta = False
                            lekcja3_5wcisnieta = False
                            lekcja3_6wcisnieta = False
                            lekcja3_7wcisnieta = False
                            lekcja3_8wcisnieta = False
                            lekcja3_9wcisnieta = False
                            lekcja3_10wcisnieta = True

            if lekcja_rect4_1.collidepoint(event.pos):
                if lekcja4_1wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 0:
                            lekcja4_1wcisnieta = True
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_2.collidepoint(event.pos):
                if lekcja4_2wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 1:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = True
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_3.collidepoint(event.pos):
                if lekcja4_3wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 2:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = True
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_4.collidepoint(event.pos):
                if lekcja4_4wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 3:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = True
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_5.collidepoint(event.pos):
                if lekcja4_5wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 4:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = True
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_6.collidepoint(event.pos):
                if lekcja4_6wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 5:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = True
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_7.collidepoint(event.pos):
                if lekcja4_7wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 6:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = True
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_8.collidepoint(event.pos):
                if lekcja4_8wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 7:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = True
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_9.collidepoint(event.pos):
                if lekcja4_9wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 8:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = True
                            lekcja4_10wcisnieta = False
            if lekcja_rect4_10.collidepoint(event.pos):
                if lekcja4_10wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if clekcje > 9:
                            lekcja4_1wcisnieta = False
                            lekcja4_2wcisnieta = False
                            lekcja4_3wcisnieta = False
                            lekcja4_4wcisnieta = False
                            lekcja4_5wcisnieta = False
                            lekcja4_6wcisnieta = False
                            lekcja4_7wcisnieta = False
                            lekcja4_8wcisnieta = False
                            lekcja4_9wcisnieta = False
                            lekcja4_10wcisnieta = True

            if lekcja_rect5_1.collidepoint(event.pos):
                if lekcja5_1wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 0:
                            lekcja5_1wcisnieta = True
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_2.collidepoint(event.pos):
                if lekcja5_2wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 1:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = True
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_3.collidepoint(event.pos):
                if lekcja5_3wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 2:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = True
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_4.collidepoint(event.pos):
                if lekcja5_4wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 3:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = True
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_5.collidepoint(event.pos):
                if lekcja5_5wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 4:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = True
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_6.collidepoint(event.pos):
                if lekcja5_6wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 5:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = True
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_7.collidepoint(event.pos):
                if lekcja5_7wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 6:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = True
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_8.collidepoint(event.pos):
                if lekcja5_8wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 7:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = True
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_9.collidepoint(event.pos):
                if lekcja5_9wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 8:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = True
                            lekcja5_10wcisnieta = False
            if lekcja_rect5_10.collidepoint(event.pos):
                if lekcja5_10wcisnieta == False:
                    if pygame.mouse.get_pressed()[0]:
                        if ptlekcje > 9:
                            lekcja5_1wcisnieta = False
                            lekcja5_2wcisnieta = False
                            lekcja5_3wcisnieta = False
                            lekcja5_4wcisnieta = False
                            lekcja5_5wcisnieta = False
                            lekcja5_6wcisnieta = False
                            lekcja5_7wcisnieta = False
                            lekcja5_8wcisnieta = False
                            lekcja5_9wcisnieta = False
                            lekcja5_10wcisnieta = True

                        

        
            


        if event.type == pygame.KEYDOWN:
            if poniedzialek == True:
                if lekcjawcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcjawcisnieta = False
                    else:
                        text += event.unicode
                elif lekcja2wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2wcisnieta = False
                    else:
                        text2 += event.unicode
                elif lekcja3wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text3 = text3[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3wcisnieta = False
                    else:
                        text3 += event.unicode
                elif lekcja4wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text4 = text4[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4wcisnieta = False
                    else:
                        text4 += event.unicode
                elif lekcja5wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text5 = text5[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5wcisnieta = False
                    else:
                        text5 += event.unicode
                elif lekcja6wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text6 = text6[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja6wcisnieta = False
                    else:
                        text6 += event.unicode
                elif lekcja7wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text7 = text7[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja7wcisnieta = False
                    else:
                        text7 += event.unicode
                elif lekcja8wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text8 = text5[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja8wcisnieta = False
                    else:
                        text8 += event.unicode
                elif lekcja9wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text9 = text9[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja9wcisnieta = False
                    else:
                        text9 += event.unicode
                elif lekcja10wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        text10 = text10[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja10wcisnieta = False
                    else:
                        text10 += event.unicode
                        
            elif wtorek == True:
                if lekcja2_1wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext = wtext[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_1wcisnieta = False
                    else:
                        wtext += event.unicode
                elif lekcja2_2wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext2 = wtext2[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_2wcisnieta = False
                    else:
                        wtext2 += event.unicode
                elif lekcja2_3wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext3 = wtext3[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_3wcisnieta = False
                    else:
                        wtext3 += event.unicode
                elif lekcja2_4wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext4 = wtext4[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_4wcisnieta = False
                    else:
                        wtext4 += event.unicode
                elif lekcja2_5wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext5 = wtext5[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_5wcisnieta = False
                    else:
                        wtext5 += event.unicode
                elif lekcja2_6wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext6 = wtext6[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_6wcisnieta = False
                    else:
                        wtext6 += event.unicode
                elif lekcja2_7wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext7 = wtext7[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_7wcisnieta = False
                    else:
                        wtext7 += event.unicode
                elif lekcja2_8wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext8 = wtext8[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_8wcisnieta = False
                    else:
                        wtext8 += event.unicode
                elif lekcja2_9wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext9 = wtext9[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_9wcisnieta = False
                    else:
                        wtext9 += event.unicode
                elif lekcja2_10wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        wtext10 = wtext10[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja2_10wcisnieta = False
                    else:
                        wtext10 += event.unicode
                        
            elif sroda == True:
                if lekcja3_1wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext = stext[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_1wcisnieta = False
                    else:
                        stext += event.unicode
                elif lekcja3_2wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext2 = stext2[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_2wcisnieta = False
                    else:
                        stext2 += event.unicode
                elif lekcja3_3wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext3 = stext3[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_3wcisnieta = False
                    else:
                        stext3 += event.unicode
                elif lekcja3_4wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext4 = stext4[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_4wcisnieta = False
                    else:
                        stext4 += event.unicode
                elif lekcja3_5wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext5 = stext5[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_5wcisnieta = False
                    else:
                        stext5 += event.unicode
                elif lekcja3_6wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext6 = stext6[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_6wcisnieta = False
                    else:
                        stext6 += event.unicode
                elif lekcja3_7wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext7 = stext7[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_7wcisnieta = False
                    else:
                        stext7 += event.unicode
                elif lekcja3_8wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext8 = stext8[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_8wcisnieta = False
                    else:
                        stext8 += event.unicode
                elif lekcja3_9wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext9 = stext9[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_9wcisnieta = False
                    else:
                        stext9 += event.unicode
                elif lekcja3_10wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        stext10 = stext10[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja3_10wcisnieta = False
                    else:
                        stext10 += event.unicode

            elif czwartek == True:
                if lekcja4_1wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext = ctext[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_1wcisnieta = False
                    else:
                        ctext += event.unicode
                elif lekcja4_2wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext2 = ctext2[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_2wcisnieta = False
                    else:
                        ctext2 += event.unicode
                elif lekcja4_3wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext3 = ctext3[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_3wcisnieta = False
                    else:
                        ctext3 += event.unicode
                elif lekcja4_4wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext4 = ctext4[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_4wcisnieta = False
                    else:
                        ctext4 += event.unicode
                elif lekcja4_5wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext5 = ctext5[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_5wcisnieta = False
                    else:
                        ctext5 += event.unicode
                elif lekcja4_6wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext6 = ctext6[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_6wcisnieta = False
                    else:
                        ctext6 += event.unicode
                elif lekcja4_7wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext7 = ctext7[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_7wcisnieta = False
                    else:
                        ctext7 += event.unicode
                elif lekcja4_8wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext8 = ctext8[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_8wcisnieta = False
                    else:
                        ctext8 += event.unicode
                elif lekcja4_9wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext9 = ctext9[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_9wcisnieta = False
                    else:
                        ctext9 += event.unicode
                elif lekcja4_10wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ctext10 = ctext10[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja4_10wcisnieta = False
                    else:
                        ctext10 += event.unicode

            elif piatek == True:
                if lekcja5_1wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext = ptext[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_1wcisnieta = False
                    else:
                        ptext += event.unicode
                elif lekcja5_2wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext2 = ptext2[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_2wcisnieta = False
                    else:
                        ptext2 += event.unicode
                elif lekcja5_3wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext3 = ptext3[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_3wcisnieta = False
                    else:
                        ptext3 += event.unicode
                elif lekcja5_4wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext4 = ptext4[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_4wcisnieta = False
                    else:
                        ptext4 += event.unicode
                elif lekcja5_5wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext5 = ptext5[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_5wcisnieta = False
                    else:
                        ptext5 += event.unicode
                elif lekcja5_6wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext6 = ptext6[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_6wcisnieta = False
                    else:
                        ptext6 += event.unicode
                elif lekcja5_7wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext7 = ptext7[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_7wcisnieta = False
                    else:
                        ptext7 += event.unicode
                elif lekcja5_8wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext8 = ptext8[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_8wcisnieta = False
                    else:
                        ptext8 += event.unicode
                elif lekcja5_9wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext9 = ptext9[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_9wcisnieta = False
                    else:
                        ptext9 += event.unicode
                elif lekcja5_10wcisnieta:
                    if event.key == pygame.K_BACKSPACE:
                        ptext10 = ptext10[:-1]
                    elif event.key == pygame.K_RETURN:
                        lekcja5_10wcisnieta = False
                    else:
                        ptext10 += event.unicode
                    
            


            
        

                

        if tloy > 0:
            tloy = 0
            lekcjay = 150
        if tloy < -1000:
            tloy = -1000


        if liczbatekstu > 15:
            text = text[:-1]
        if liczbatekstu2 > 15:
            text2 = text2[:-1]
        if liczbatekstu3 > 15:
            text3 = text3[:-1]
        if liczbatekstu4 > 15:
            text4 = text4[:-1]
        if liczbatekstu5 > 15:
            text5 = text5[:-1]
        if liczbatekstu6 > 15:
            text6 = text6[:-1]
        if liczbatekstu7 > 15:
            text7 = text7[:-1]
        if liczbatekstu8 > 15:
            text8 = text8[:-1]
        if liczbatekstu9 > 15:
            text9 = text9[:-1]
        if liczbatekstu10 > 15:
            text10 = text10[:-1]

        if liczbawtekstu > 15:
            wtext = wtext[:-1]
        if liczbawtekstu2 > 15:
            wtext2 = wtext2[:-1]
        if liczbawtekstu3 > 15:
            wtext3 = wtext3[:-1]
        if liczbawtekstu4 > 15:
            wtext4 = wtext4[:-1]
        if liczbawtekstu5 > 15:
            wtext5 = wtext5[:-1]
        if liczbawtekstu6 > 15:
            wtext6 = wtext6[:-1]
        if liczbawtekstu7 > 15:
            wtext7 = wtext7[:-1]
        if liczbawtekstu8 > 15:
            wtext8 = wtext8[:-1]
        if liczbawtekstu9 > 15:
            wtext9 = wtext9[:-1]
        if liczbawtekstu10 > 15:
            wtext10 = wtext10[:-1]

        if liczbastekstu > 15:
            stext = stext[:-1]
        if liczbastekstu2 > 15:
            stext2 = stext2[:-1]
        if liczbastekstu3 > 15:
            stext3 = stext3[:-1]
        if liczbastekstu4 > 15:
            stext4 = stext4[:-1]
        if liczbastekstu5 > 15:
            stext5 = stext5[:-1]
        if liczbastekstu6 > 15:
            stext6 = stext6[:-1]
        if liczbastekstu7 > 15:
            stext7 = stext7[:-1]
        if liczbastekstu8 > 15:
            stext8 = stext8[:-1]
        if liczbastekstu9 > 15:
            stext9 = stext9[:-1]
        if liczbastekstu10 > 15:
            stext10 = stext10[:-1]

        if liczbactekstu > 15:
            ctext = ctext[:-1]
        if liczbactekstu2 > 15:
            ctext2 = ctext2[:-1]
        if liczbactekstu3 > 15:
            ctext3 = ctext3[:-1]
        if liczbactekstu4 > 15:
            ctext4 = ctext4[:-1]
        if liczbactekstu5 > 15:
            ctext5 = ctext5[:-1]
        if liczbactekstu6 > 15:
            ctext6 = ctext6[:-1]
        if liczbactekstu7 > 15:
            ctext7 = ctext7[:-1]
        if liczbactekstu8 > 15:
            ctext8 = ctext8[:-1]
        if liczbactekstu9 > 15:
            ctext9 = ctext9[:-1]
        if liczbactekstu10 > 15:
            ctext10 = ctext10[:-1]

        if liczbaptekstu > 15:
            ptext = ptext[:-1]
        if liczbaptekstu2 > 15:
            ptext2 = ptext2[:-1]
        if liczbaptekstu3 > 15:
            ptext3 = ptext3[:-1]
        if liczbaptekstu4 > 15:
            ptext4 = ptext4[:-1]
        if liczbaptekstu5 > 15:
            ptext5 = ptext5[:-1]
        if liczbaptekstu6 > 15:
            ptext6 = ptext6[:-1]
        if liczbaptekstu7 > 15:
            ptext7 = ptext7[:-1]
        if liczbaptekstu8 > 15:
            ptext8 = ptext8[:-1]
        if liczbaptekstu9 > 15:
            ptext9 = ptext9[:-1]
        if liczbaptekstu10 > 15:
            ptext10 = ptext10[:-1]
        



    text_rect = font.render(text, True, czarny)
    okno.blit(text_rect, (lekcja_rect1.x + 20, lekcja_rect1.y + 30))
    text_rect2 = font.render(text2, True, czarny)
    okno.blit(text_rect2, (lekcja_rect2.x + 20, lekcja_rect2.y + 30))
    text_rect3 = font.render(text3, True, czarny)
    okno.blit(text_rect3, (lekcja_rect3.x + 20, lekcja_rect3.y + 30))
    text_rect4 = font.render(text4, True, czarny)
    okno.blit(text_rect4, (lekcja_rect4.x + 20, lekcja_rect4.y + 30))
    text_rect5 = font.render(text5, True, czarny)
    okno.blit(text_rect5, (lekcja_rect5.x + 20, lekcja_rect5.y + 30))
    text_rect6 = font.render(text6, True, czarny)
    okno.blit(text_rect6, (lekcja_rect6.x + 20, lekcja_rect6.y + 30))
    text_rect7 = font.render(text7, True, czarny)
    okno.blit(text_rect7, (lekcja_rect7.x + 20, lekcja_rect7.y + 30))
    text_rect8 = font.render(text8, True, czarny)
    okno.blit(text_rect8, (lekcja_rect8.x + 20, lekcja_rect8.y + 30))
    text_rect9 = font.render(text9, True, czarny)
    okno.blit(text_rect9, (lekcja_rect9.x + 20, lekcja_rect9.y + 30))
    text_rect10 = font.render(text10, True, czarny)
    okno.blit(text_rect10, (lekcja_rect10.x + 20, lekcja_rect10.y + 30))

    

    wtext_rect = font.render(wtext, True, czarny)
    okno.blit(wtext_rect, (lekcja_rect2_1.x + 20, lekcja_rect2_1.y + 30))
    wtext_rect2 = font.render(wtext2, True, czarny)
    okno.blit(wtext_rect2, (lekcja_rect2_2.x + 20, lekcja_rect2_2.y + 30))
    wtext_rect3 = font.render(wtext3, True, czarny)
    okno.blit(wtext_rect3, (lekcja_rect2_3.x + 20, lekcja_rect2_3.y + 30))
    wtext_rect4 = font.render(wtext4, True, czarny)
    okno.blit(wtext_rect4, (lekcja_rect2_4.x + 20, lekcja_rect2_4.y + 30))
    wtext_rect5 = font.render(wtext5, True, czarny)
    okno.blit(wtext_rect5, (lekcja_rect2_5.x + 20, lekcja_rect2_5.y + 30))
    wtext_rect6 = font.render(wtext6, True, czarny)
    okno.blit(wtext_rect6, (lekcja_rect2_6.x + 20, lekcja_rect2_6.y + 30))
    wtext_rect7 = font.render(wtext7, True, czarny)
    okno.blit(wtext_rect7, (lekcja_rect2_7.x + 20, lekcja_rect2_7.y + 30))
    wtext_rect8 = font.render(wtext8, True, czarny)
    okno.blit(wtext_rect8, (lekcja_rect2_8.x + 20, lekcja_rect2_8.y + 30))
    wtext_rect9 = font.render(wtext9, True, czarny)
    okno.blit(wtext_rect9, (lekcja_rect2_9.x + 20, lekcja_rect2_9.y + 30))
    wtext_rect10 = font.render(wtext10, True, czarny)
    okno.blit(wtext_rect10, (lekcja_rect2_10.x + 20, lekcja_rect2_10.y + 30))

    stext_rect = font.render(stext, True, czarny)
    okno.blit(stext_rect, (lekcja_rect3_1.x + 20, lekcja_rect3_1.y + 30))
    stext_rect2 = font.render(stext2, True, czarny)
    okno.blit(stext_rect2, (lekcja_rect3_2.x + 20, lekcja_rect3_2.y + 30))
    stext_rect3 = font.render(stext3, True, czarny)
    okno.blit(stext_rect3, (lekcja_rect3_3.x + 20, lekcja_rect3_3.y + 30))
    stext_rect4 = font.render(stext4, True, czarny)
    okno.blit(stext_rect4, (lekcja_rect3_4.x + 20, lekcja_rect3_4.y + 30))
    stext_rect5 = font.render(stext5, True, czarny)
    okno.blit(stext_rect5, (lekcja_rect3_5.x + 20, lekcja_rect3_5.y + 30))
    stext_rect6 = font.render(stext6, True, czarny)
    okno.blit(stext_rect6, (lekcja_rect3_6.x + 20, lekcja_rect3_6.y + 30))
    stext_rect7 = font.render(stext7, True, czarny)
    okno.blit(stext_rect7, (lekcja_rect3_7.x + 20, lekcja_rect3_7.y + 30))
    stext_rect8 = font.render(stext8, True, czarny)
    okno.blit(stext_rect8, (lekcja_rect3_8.x + 20, lekcja_rect3_8.y + 30))
    stext_rect9 = font.render(stext9, True, czarny)
    okno.blit(stext_rect9, (lekcja_rect3_9.x + 20, lekcja_rect3_9.y + 30))
    stext_rect10 = font.render(stext10, True, czarny)
    okno.blit(stext_rect10, (lekcja_rect3_10.x + 20, lekcja_rect3_10.y + 30))

    ctext_rect = font.render(ctext, True, czarny)
    okno.blit(ctext_rect, (lekcja_rect4_1.x + 20, lekcja_rect4_1.y + 30))
    ctext_rect2 = font.render(ctext2, True, czarny)
    okno.blit(ctext_rect2, (lekcja_rect4_2.x + 20, lekcja_rect4_2.y + 30))
    ctext_rect3 = font.render(ctext3, True, czarny)
    okno.blit(ctext_rect3, (lekcja_rect4_3.x + 20, lekcja_rect4_3.y + 30))
    ctext_rect4 = font.render(ctext4, True, czarny)
    okno.blit(ctext_rect4, (lekcja_rect4_4.x + 20, lekcja_rect4_4.y + 30))
    ctext_rect5 = font.render(ctext5, True, czarny)
    okno.blit(ctext_rect5, (lekcja_rect4_5.x + 20, lekcja_rect4_5.y + 30))
    ctext_rect6 = font.render(ctext6, True, czarny)
    okno.blit(ctext_rect6, (lekcja_rect4_6.x + 20, lekcja_rect4_6.y + 30))
    ctext_rect7 = font.render(ctext7, True, czarny)
    okno.blit(ctext_rect7, (lekcja_rect4_7.x + 20, lekcja_rect4_7.y + 30))
    ctext_rect8 = font.render(ctext8, True, czarny)
    okno.blit(ctext_rect8, (lekcja_rect4_8.x + 20, lekcja_rect4_8.y + 30))
    ctext_rect9 = font.render(ctext9, True, czarny)
    okno.blit(ctext_rect9, (lekcja_rect4_9.x + 20, lekcja_rect4_9.y + 30))
    ctext_rect10 = font.render(ctext10, True, czarny)
    okno.blit(ctext_rect10, (lekcja_rect4_10.x + 20, lekcja_rect4_10.y + 30))

    ptext_rect = font.render(ptext, True, czarny)
    okno.blit(ptext_rect, (lekcja_rect5_1.x + 20, lekcja_rect5_1.y + 30))
    ptext_rect2 = font.render(ptext2, True, czarny)
    okno.blit(ptext_rect2, (lekcja_rect5_2.x + 20, lekcja_rect5_2.y + 30))
    ptext_rect3 = font.render(ptext3, True, czarny)
    okno.blit(ptext_rect3, (lekcja_rect5_3.x + 20, lekcja_rect5_3.y + 30))
    ptext_rect4 = font.render(ptext4, True, czarny)
    okno.blit(ptext_rect4, (lekcja_rect5_4.x + 20, lekcja_rect5_4.y + 30))
    ptext_rect5 = font.render(ptext5, True, czarny)
    okno.blit(ptext_rect5, (lekcja_rect5_5.x + 20, lekcja_rect5_5.y + 30))
    ptext_rect6 = font.render(ptext6, True, czarny)
    okno.blit(ptext_rect6, (lekcja_rect5_6.x + 20, lekcja_rect5_6.y + 30))
    ptext_rect7 = font.render(ptext7, True, czarny)
    okno.blit(ptext_rect7, (lekcja_rect5_7.x + 20, lekcja_rect5_7.y + 30))
    ptext_rect8 = font.render(ptext8, True, czarny)
    okno.blit(ptext_rect8, (lekcja_rect5_8.x + 20, lekcja_rect5_8.y + 30))
    ptext_rect9 = font.render(ptext9, True, czarny)
    okno.blit(ptext_rect9, (lekcja_rect5_9.x + 20, lekcja_rect5_9.y + 30))
    ptext_rect10 = font.render(ptext10, True, czarny)
    okno.blit(ptext_rect10, (lekcja_rect5_10.x + 20, lekcja_rect5_10.y + 30))

    pygame.display.update() 
    zegar.tick(60)
    




pygame.quit()
