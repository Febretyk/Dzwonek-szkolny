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

lekcjay = 150
lekcjax = 225




lekcja_rect2 = lekcja.get_rect(midbottom = (lekcjax, lekcjay+200))

lekcja_rect3 = lekcja.get_rect(midbottom = (lekcjax, lekcjay+400))

lekcja_rect4 = lekcja.get_rect(midbottom = (lekcjax, lekcjay+600))

lekcja_rect5 = lekcja.get_rect(midbottom = (lekcjax, lekcjay+800))
font = 0
surf = 0





running = True

poniedziałek = True
wtorek = False
środa = False
czwartek = False
piątek = False




while running:
    tloBx = tlox+450
    tloCx = tloBx+450
    tloDx = tloCx+450
    tloEx = tloDx+450
    
    okno.fill((255, 255, 255))
    okno.blit(tlo, (tlox, tloy))
    okno.blit(tloB, (tloBx, tloy))
    okno.blit(tloC, (tloCx, tloy))
    okno.blit(tloC, (tloDx, tloy))
    okno.blit(tloE, (tloEx, tloy))
    lekcja_rect1 = lekcja.get_rect(midbottom = (tlox+lekcjax, tloy+lekcjay))
    okno.blit(lekcja, lekcja_rect1)
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
                lekcjay += dy


        elif event.type == pygame.MOUSEBUTTONDOWN:

            if guzik_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    print("PRINT")
                    if poniedziałek == True:
                        lekcja = pygame.image.load("LEKCJA.png").convert_alpha()
                        


            


            if pon_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = 0
                    print("co do sigmy")
                    poniedziałek = True
                    wtorek = False
                    środa = False
                    czwartek = False
                    piątek = False
                        


            if wt_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -450
                    print("co do czego")
                    poniedziałek = False
                    wtorek = True
                    środa = False
                    czwartek = False
                    piątek = False
                    
            if sr_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -900
                    print("errr...")
                    poniedziałek = False
                    wtorek = False
                    środa = True
                    czwartek = False
                    piątek = False
                    
            if cz_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -1350
                    print("ummm")
                    poniedziałek = False
                    wtorek = False
                    środa = False
                    czwartek = True
                    piątek = False

            if pt_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0]:
                    tlox = -1800
                    print("co do śmigła")
                    poniedziałek = False
                    wtorek = False
                    środa = False
                    czwartek = True
                    piątek = False

            


                

        if tloy > 0:
            tloy = 0
            lekcjay = 150
        if tloy < -625:
            tloy = -625
        
            

    pygame.display.update() 
    zegar.tick(60)
    




pygame.quit()
