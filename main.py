import pygame

pygame.init()

okno = pygame.display.set_mode((450, 150))

tlo = pygame.image.load("zeszyt.png").convert_alpha()
oknox, oknoy = tlo.get_width(), tlo.get_height()
okno = pygame.display.set_mode((450, oknoy))
baza = pygame.image.load("ui.png").convert_alpha()


tlox = 0
tloy = 0


running = True

while running:
    okno.blit(tlo, (0, 0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    okno.blit(baza, (0, 400))



    pygame.display.update()

    pygame.time.Clock().tick(60)
    




pygame.quit()
