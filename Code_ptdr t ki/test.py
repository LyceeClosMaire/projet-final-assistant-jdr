# Créé par martinmaestre, le 30/04/2018 en Python 3.2
import pygame

from pygame.locals import *

pygame.init()

# ########AFFICHAGE###

screenInfo = pygame.display.Info()
(width, height) =(screenInfo.current_w, screenInfo.current_h)

screen = pygame.display.set_mode( (1200, 800) )

# ########LE BACKGROUND###

mouse = pygame.mouse.get_pos()

# ########LA SOURIS#######

image = pygame.image.load("fond.jpg")

# ########LE PERSONNAGE###

(xp,yp) = (0,0)
selectPerso1 = False
truePerso1 = False
perso1S = pygame.image.load("50x50.jpg")
perso1M = pygame.image.load("73x86.jpg")
perso1L = pygame.image.load("120x166.jpg")

emptyList = [True,False,True,True,True,True]

running = True
afficheMenu = False
# #######################LE BÔ MENU####

def menu_haut(x, y, z, empty):
    global b1,b2,b3,b4,b5,b6
    #x = 50
    #y = 150
    #z = 250
    b1 = pygame.Rect(y, x,50 ,50)
    if empty[0]:
        pygame.draw.rect(screen, (127, 255, 127), b1)
    else:
        screen.blit(perso1S,b1)

    b2 = pygame.Rect(z, x, 50, 50)
    if empty[1]:
        pygame.draw.rect(screen, (127, 127, 127), b2)
    else:
        screen.blit(perso1S,b2)

    b3 = pygame.Rect(y, y, 50, 50)
    if empty[2]:
        pygame.draw.rect(screen, (127, 127, 127), b3)
    else:
        screen.blit(perso1S,b3)

    b4 = pygame.Rect(y, z, 50, 50)
    if empty[3]:
        pygame.draw.rect(screen, (127, 127, 127), b4)
    else:
        screen.blit(perso1S,b4)

    b5 = pygame.Rect(z, z, 50, 50)
    if empty[4]:
        pygame.draw.rect(screen, (127, 127, 127), b5)
    else:
        screen.blit(perso1S,b5)

    b6 = pygame.Rect(z, y, 50, 50)
    if empty[5]:
        pygame.draw.rect(screen, (127, 127, 127), b6)
    else:
        screen.blit(perso1S,b6)

# ##################################

def map():
    screen.fill((0,0,0))

    preview = pygame.Rect(200, 200, 800, 400)
    pygame.draw.rect(screen, (0,50,150), preview)

    bgauche = pygame.Rect(100, 350, 50, 100)
    pygame.draw.rect(screen, (0, 50, 150), bgauche)

    bdroite = pygame.Rect(1050, 350, 50, 100)
    pygame.draw.rect(screen, (0, 50, 150), bdroite)

    bbas = pygame.Rect(500, 650, 200, 50)
    pygame.draw.rect(screen, (50, 250, 0), bbas)
# ##################################

while running:

    screen.blit(image, [0,0])

# #########Selection + Vrai perso###

    if selectPerso1:
        (xp,yp) = event.pos
        screen.blit(perso1M,(xp,yp))

    if truePerso1:
        screen.blit(perso1L,(xp,yp))
        emptyList[1] = True

# ##################################

    for event in pygame.event.get() :

        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) :
            running = False

        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if bouton1.collidepoint(event.pos):
                afficheMenu = not afficheMenu
            elif afficheMenu:
                if b2.collidepoint(event.pos):
                    selectPerso1 = True
                    truePerso1 = False
                    emptyList[1] = True
                    # ###

        elif event.type == MOUSEBUTTONUP and event.button == 1:
            if afficheMenu:
                if selectPerso1 == True:
                    selectPerso1 = False
                    truePerso1 = True
                    emptyList[1] = False

        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            if xp < event.pos[0] < xp + 120 and yp < event.pos[1] < yp + 166:
                truePerso1 = False
                emptyList[1] = False


# ###############################

    if map()

    bouton1 = pygame.Rect(50, 50, 50, 50)
    pygame.draw.rect(screen,(147, 147, 255), bouton1)


    if afficheMenu:
        menu_haut(50, 150, 250,emptyList)

    pygame.display.flip()

pygame.quit()