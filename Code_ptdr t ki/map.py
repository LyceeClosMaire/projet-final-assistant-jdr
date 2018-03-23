# Créé par martinmaestre, le 05/03/2018 en Python 3.2
import pygame

from pygame.locals import *
pygame.init()


# ########AFFICHAGE###

screenInfo = pygame.display.Info()
(width, height) =(screenInfo.current_w, screenInfo.current_h)

screen = pygame.display.set_mode( (1200, 800) )

# ########LE BACKGROUND###



# ########################

image = pygame.image.load("bg.png")

# ########

perso = pygame.image.load("perso.jpg")

posPerso = [2 ,4]

running = True

bouger_perso = False

while running:

# #################

    screen.blit(image, [0,0])

# #################
    rectangle = pygame.Rect(0, 600, 1200, 200)

    if rectangle.collidepoint(pygame.mouse.get_pos()):
        print('OUI')

    pygame.draw.rect(screen,(255,0,0),rectangle)

# ##################

    [x,y] = posPerso
    screen.blit(perso, [x*50, y*50])
    pygame.display.flip()

    for  event in pygame.event.get() :

        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) :
            running = False
# #####################################


# #################Contrôle du perso###



##        if event.type == KEYUP:
##
##            if bouger_perso == True:
##
##                if event.key == K_UP and posPerso[1] != 0: #Si on appuie sur la flèche du haut, le perso monte monte en Y
##                    posPerso[1] -= 1
##
##                if event.key == K_DOWN and posPerso[1] != 12: #Bas >  baisse en Y
##                    posPerso[1] += 1
##
##                if event.key == K_LEFT and posPerso[0] != 0: #Gauche > Va a gauche en X
##                    posPerso[0] -= 1
##
##                if event.key == K_RIGHT and posPerso[0] != 20: #Droite > Va à droite en Y
##                    posPerso[0] += 1


# ####Déplacer un perso###

        if event.type == pygame.MOUSEBUTTONDOWN: #Quand j'appuie

            (i,j) = pygame.mouse.get_pos() #Je prends la position i j (équivalent à x y)

            (i,j) = (int(i/50),int(j/50)) #Je divise par 50 (car mon image est sur un grille de 1200 sur 800 ou 24 sur 16)


            if event.button == 3:

                if x <= i < x+4 and y <= j < y+4 : #Si ma souris en I / J correspond a la position de l'image +4 (car 200 sur 200 donc 0,0 jusqu'a 200,200)
                    if bouger_perso == True:
                        bouger_perso = False
                        continue                    #Ici je permet au personnage d'être déplacer si on clique dessus, et j'empêche le déplacement en recliquant
                    if bouger_perso == False:       #puis avec la fonction 'continue' j'empêche la boucle de faire l'inverse
                        bouger_perso = True
                        continue

            if event.button == 1:

                    if bouger_perso == True:
                        posPerso = (i,j)

















pygame.quit()