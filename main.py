#Elina_Sumin_ISK22

import pygame #Pygame teegi laadimine
pygame.init() #pygame käivitamine

#Akna lahtihoidmiseks, aken sulgeb ainult, kui X- märgile vajutada, akna vasakul, üleval, servas.
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #ekraani seaded
    screen=pygame.display.set_mode([640,480]) #Display kucatakse suuruses 640x480
    pygame.display.set_caption("Ülesanne2") #Mängule pealkirja lisamine, ekraani nime kuvamine

   #taustapildi lisamine
    bg = pygame.image.load("pildid/bg_shop.webp") #taustapildi lisamine
    screen.blit(bg, [0, 0])

    man = pygame.image.load("pildid/seller.webp") #Spraidi lisamine kaustast pildid, mis asub antud projektis
    man = pygame.transform.scale(man, [265,310]) # spraidi kuju venitamine, vasakule_paremale; üles-alla
    screen.blit(man, [105, 160]) # liigutab spraidi asukohta akna suhtes vasakule-paremale; üles-alla

    chat = pygame.image.load("pildid/chat.webp") #Juttumulli pildi lisamine
    chat = pygame.transform.scale(chat, [250, 210]) #Juttumulli pildi venitamine
    screen.blit(chat, [250, 60]) #Juttumulli pildi liigutamine

    #teksti lisamine
    font = pygame.font.SysFont("Tahoma", 24) #Teksti fonti ja selle suuruse määramine
    text = font.render("Tere, olen Elina", True, [255,255,255]) #Teksti sisu ja värvuse määramine RBG-koodi kasutades
    screen.blit(text, [290,130]) #teksti liigutamine ekraanil õigesse kohta antud kordinaatidega




    pygame.display.flip() #ekraani värskendamine


#Elina_Sumin_ISK22