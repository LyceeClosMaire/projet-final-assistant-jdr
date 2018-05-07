# Créé par martinmaestre, le 05/03/2018 en Python 3.2
import pygame

from pygame.locals import *

pygame.init()


# ########AFFICHAGE###

screenInfo = pygame.display.Info()
(width, height) =(screenInfo.current_w, screenInfo.current_h)

screen = pygame.display.set_mode( (1200, 800) )

# ########LE BACKGROUND###


image = pygame.image.load("fond.jpg")

# #Les petites variables <3#######

perso = pygame.image.load("perso.jpg")
#
xmenu_bas = pygame.image.load("menu.perso.jpg")
#
xmenu_bas = pygame.transform.scale(xmenu_bas,(1200, 200))
#
xbouton_menu = pygame.image.load("bouton_menu.jpg")
#
posPerso = [2 ,4]
#
running = True
#
bouger_perso = False
#
holding = False # Tenir
#

while running:

# #################

    screen.blit(image, [0,0])


# ################################DESIGN#
# #Le petit menu <3################

    menu_bas = pygame.Rect(0, 600, 1200, 200)

    if menu_bas.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
               print("bite")


    pygame.draw.rect(screen,(0    ,0    ,0  ),menu_bas)
    pygame.Surface.blit(screen,xmenu_bas ,menu_bas)

# #Bouton de mon menu#################

    bouton_menu = pygame.Rect(0, 600, 100, 200)
    pygame.draw.rect(screen,(0  ,0  ,0  ),bouton_menu)
    pygame.Surface.blit(screen, xbouton_menu, bouton_menu)

# #Cadres perso######################

    rectangle1 = pygame.Rect(150, 625, 150, 150)
    pygame.draw.rect(screen, (0 ,0  ,0  ),rectangle1)

    rectangle2 = pygame.Rect(350, 625, 150, 150)
    pygame.draw.rect(screen, (0 ,0  ,0  ),rectangle2)

    rectangle3 = pygame.Rect(550, 625, 150, 150)
    pygame.draw.rect(screen, (0 ,0  ,0  ),rectangle3)

    rectangle4 = pygame.Rect(750, 625, 150, 150)
    pygame.draw.rect(screen, (0 ,0  ,0  ),rectangle4)

    rect5 = pygame.Rect(950, 625, 150, 150)
    rectangle5 = pygame.draw.rect(screen, (0 ,0  ,0  ),rect5)

# ####################################
# #Déplacer mon perso de façon fluide#

    if bouger_perso == True and holding == True:
        (i,j) = pygame.mouse.get_pos()

        if 95 < i < 1105 and 95 < j < 505:    #Je prends la position i j (équivalent à x y)
            posPerso = (i-75,j+-75)

# #Mon petit perso <3################

    [x,y] = posPerso

    screen.blit(perso, [x, y])

# #La petite boucle <3###############

    pygame.display.flip()

# #Les petits events<3###############

    for  event in pygame.event.get() :


        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) :
            running = False

# #####################################


        if event.type == bouton_menu.collidepoint(pygame.mouse.get_pos()):

            print('test')
# ####Déplacer un perso###

        if event.type == pygame.MOUSEBUTTONDOWN: #Quand j'appuie

            (i,j) = pygame.mouse.get_pos() #Je prends la position i j (équivalent à x y)


            if event.button == 3:

                if x <= i < x+200 and y <= j < y+200 : #Si ma souris en I / J correspond a la position de l'image +4 (car 200 sur 200 donc 0,0 jusqu'a 200,200)
                    if bouger_perso == True:
                        bouger_perso = False
                        continue                    #Ici je permet au personnage d'être déplacer si on clique dessus, et j'empêche le déplacement en recliquant
                    if bouger_perso == False:       #puis avec la fonction 'continue' j'empêche la boucle de faire l'inverse
                        bouger_perso = True
                        continue

            if event.button == 1:
                holding = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                holding = False














pygame.quit()