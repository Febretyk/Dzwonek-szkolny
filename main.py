import pygame

pygame.init()

okno = pygame.display.set_mode((450, 150))
pygame.display.set_caption("Dzwonek")
zegar = pygame.time.Clock()





tlo = pygame.image.load("zeszyt.png").convert_alpha()
tloB = pygame.image.load("zeszytB.png").convert_alpha()
tloC = pygame.image.load("zeszytC.png").convert_alpha()
tloD = pygame.image.load("zeszytD.png").convert_alpha()
tloE = pygame.image.load("zeszytE.png").convert_alpha()
tloB_width = tloB.get_width()





okno = pygame.display.set_mode((450, 625))
baza = pygame.image.load("ui.png").convert_alpha()


guzik = pygame.image.load("dodaj.png").convert_alpha()
guzik_rect = guzik.get_rect(midbottom = (225,550))

pon = pygame.image.load("tydzień/pon.png").convert_alpha()
pon_rect = pon.get_rect(midbottom = (70,30))
wt = pygame.image.load("tydzień/wt.png").convert_alpha()
wt_rect = wt.get_rect(midbottom = (150,30))
sr = pygame.image.load("tydzień/sro.png").convert_alpha()
sr_rect = sr.get_rect(midbottom = (230,30))
cz = pygame.image.load("tydzień/czw.png").convert_alpha()
cz_rect = cz.get_rect(midbottom = (310,30))
pt = pygame.image.load("tydzień/pt.png").convert_alpha()
pt_rect = pt.get_rect(midbottom = (390, 30))


font = 0
surf = 0


tlox = 0
tloy = 0
tloBx = tlox+450
tloCx = tloBx+450
tloDx = tloCx+450
tloEx = tloDx+450



running = True
dodajwcisniety = False



while running:
    okno.blit(tlo, (tlox, tloy))
    okno.fill((255, 255, 255))
    okno.blit(tlo, (tlox, tloy))
    okno.blit(tloB, (tloBx, 0))
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
            if dodajwcisniety == False:
                if guzik_rect.collidepoint(event.pos):
                    if pygame.mouse.get_pressed()[0]:
                        guzik = pygame.image.load("dodaj2.png").convert_alpha()
                        dodajwcisniety = True

            elif dodajwcisniety == True:
                if guzik_rect.collidepoint(event.pos):
                    if pygame.mouse.get_pressed()[0]:
                        guzik = pygame.image.load("dodaj.png").convert_alpha()
                        dodajwcisniety = False


        elif dodajwcisniety == True:
            tlox = 450

        elif dodajwcisniety == False:
            tlox = 0
                

        if tloy > 0:
            tloy = 0
        if tloy < -625:
            tloy = -625
        
            

   
    



    pygame.display.update() 
    zegar.tick(60)
    




pygame.quit()
