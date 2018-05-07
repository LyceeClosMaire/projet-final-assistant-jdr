import csv                                           # j'importe de quoi lire et modifier mes dossiers qui me serviront pour les personnages
import os
import pygame
from pygame.locals import *                          #j'importe pygame afin d'ouvrir des fenêtres de choix

pygame.init()



race_csv = "liste_races.csv"
perso_csv = "liste_personnages.csv"
classe_csv = "liste_classe.csv"

fichier_perso = open( perso_csv , mode='w' , newline='')                            #ces deux lignes servent à écrire dans le dossier de personnages existants
ecr_perso = csv.writer(fichier_perso, dialect= 'excel')


fichier_perso2 = open(perso_csv , mode ='r' , newline = '')                         # ces 6 lignes me permettent de lire les csv ( le premier a un deux a la fin pour ne pas confondre avec l'ecriture
fichier_race = open(race_csv , mode ='r' , newline = '')
fichier_classe = open(classe_csv , mode = 'r' , newline= '')

lec_perso = csv.reader(fichier_perso2, dialect='excel')
lec_race = csv.reader(fichier_race , dialect='excel')
lec_classe = csv.reader(fichier_classe, dialect='excel')



blanc = (255,255,255)
noir = (0,0,0)
fenetre = pygame.display.set_mode((1200, 800 ))
font = pygame.font.Font('BradBunR.ttf',50)
etat= 'menu'
ouvert = 1
classe_perso=''
race_perso=''

def menu():
    global etat
    global event

    fenetre.fill( blanc)
    Gt = font.render("Cliquez pour continuer",1,noir)
    fenetre.blit(Gt,(355,350))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
             etat = 'menu2'

    fermeture(event)

def truc():

    fenetre.fill( (127,127,127))

    fermeture(event)


def menu2():
    global etat
    global event

    fenetre.fill( blanc)
    texte1 = font.render("Charger un ancien personnage",1,noir)
    texte2 = font.render("Créer un nouveau personnage",1,noir)

    bouton1 = pygame.Rect(300,200,600,75)
    pygame.draw.rect(fenetre,(255,255,200),bouton1)

    bouton2 = pygame.Rect(300,500,600,75)
    pygame.draw.rect(fenetre,(200,255,255),bouton2)

    fenetre.blit(texte1,(325,200))
    fenetre.blit(texte2,(325, 500))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                mousepos = pygame.mouse.get_pos()

                if bouton1.collidepoint(mousepos):
                    etat = 'truc'

                elif bouton2.collidepoint(mousepos):
                    etat = 'menu3'


    fermeture(event)
    return etat

def menu3():
    global etat
    global event
    global race_perso

    fenetre.fill(blanc)
    texte1 = font.render("Choix de race",1,noir)
    fenetre.blit(texte1,(50,25))

    texte2 = font.render("Humain", 1, noir)
    texte3 = font.render("Nain", 1, noir)                       #je prépare les textes
    texte4 = font.render("Elfe", 1, noir)
    texte5 = font.render("Orc", 1, noir)
    texte6 = font.render("Centaure", 1, noir)
    texte7 = font.render("Gobelin", 1, noir)


    bouton1 = pygame.Rect(175,225,175,75)
    pygame.draw.rect(fenetre,(200,200,255),bouton1)

    bouton2 = pygame.Rect(475,225,140,75)
    pygame.draw.rect(fenetre,(200,200,255),bouton2)

    bouton3 = pygame.Rect(725,225,125,75)
    pygame.draw.rect(fenetre,(200,200,255),bouton3)                 #je positionne et colorise les boutons

    bouton4 = pygame.Rect(175,525,125,75)
    pygame.draw.rect(fenetre,(255,200,200),bouton4)

    bouton5 = pygame.Rect(455,525,195,75)
    pygame.draw.rect(fenetre,(255,200,200),bouton5)

    bouton6 = pygame.Rect(725,525,165,75)
    pygame.draw.rect(fenetre,(255,200,200),bouton6)

    fenetre.blit(texte2,(200,225))
    fenetre.blit(texte3,(500,225))                              #je les positionne
    fenetre.blit(texte4,(750,225))
    fenetre.blit(texte5,(200,525))
    fenetre.blit(texte6,(480,525))
    fenetre.blit(texte7,(750,525))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                mousepos = pygame.mouse.get_pos()

                if bouton1.collidepoint(mousepos):
                    race_perso = 'humain'
                    etat = 'menu4'

                elif bouton2.collidepoint(mousepos):
                    race_perso = 'nain'
                    etat = 'menu4'

                elif bouton3.collidepoint(mousepos):
                    race_perso = 'elfe'
                    etat = 'menu4'

                elif bouton4.collidepoint(mousepos):
                    race_perso = 'orc'
                    etat = 'menu4'

                elif bouton5.collidepoint(mousepos):
                    race_perso = 'centaure'
                    etat = 'menu4'

                elif bouton6.collidepoint(mousepos):
                    race_perso = 'gobelin'
                    etat = 'menu4'

    fermeture(event)
    return etat
    return race_perso

def menu4():
    global etat
    global event
    global classe_perso

    fenetre.fill(blanc)
    texte1 = font.render("Choix de classe",1,noir)
    fenetre.blit(texte1,(50,25))

    texte2 = font.render("Guerrier", 1, noir)
    texte3 = font.render("Chaman", 1, noir)                       #je prépare les textes
    texte4 = font.render("Mage", 1, noir)
    texte5 = font.render("Prêtre", 1, noir)
    texte6 = font.render("Nécromancien", 1, noir)
    texte7 = font.render("Paladin", 1, noir)


    bouton1 = pygame.Rect(175,225,185,75)
    pygame.draw.rect(fenetre,(200,200,200),bouton1)

    bouton2 = pygame.Rect(495,225,160,75)
    pygame.draw.rect(fenetre,(200,200,200),bouton2)

    bouton3 = pygame.Rect(725,225,125,75)
    pygame.draw.rect(fenetre,(200,200,200),bouton3)                 #je positionne et colorise les boutons

    bouton4 = pygame.Rect(175,525,160,75)
    pygame.draw.rect(fenetre,(200,200,200),bouton4)

    bouton5 = pygame.Rect(430,525,300,75)
    pygame.draw.rect(fenetre,(200,200,200),bouton5)

    bouton6 = pygame.Rect(750,525,165,75)
    pygame.draw.rect(fenetre,(200,200,200),bouton6)

    fenetre.blit(texte2,(200,225))
    fenetre.blit(texte3,(500,225))                              #je les positionne
    fenetre.blit(texte4,(750,225))
    fenetre.blit(texte5,(200,525))
    fenetre.blit(texte6,(445,525))
    fenetre.blit(texte7,(775,525))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                mousepos = pygame.mouse.get_pos()

                if bouton1.collidepoint(mousepos):
                    classe_perso = 'guerrier'
                    etat = 'menu5'

                elif bouton2.collidepoint(mousepos):
                    classe_perso = 'chaman'
                    etat = 'menu5'

                elif bouton3.collidepoint(mousepos):
                    classe_perso = 'mage'
                    etat = 'menu5'

                elif bouton4.collidepoint(mousepos):
                    classe_perso = 'pretre'
                    etat = 'menu5'

                elif bouton5.collidepoint(mousepos):
                    classe_perso = 'necromancien'
                    etat = 'menu5'

                elif bouton6.collidepoint(mousepos):
                    classe_perso = 'paladin'
                    etat = 'menu5'

    fermeture(event)
    return etat
    return classe_perso


def menu5():

    global etat
    global event

    fenetre.fill( (133,211,1))

    fermeture(event)


def fermeture(event):
    global ouvert
    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
        ouvert = 0





while ouvert:

    souris = pygame.mouse.get_pos()

    if etat == 'menu':
        menu()

    elif etat == 'truc':
        truc()

    elif etat == 'menu2':
        menu2()

    elif etat == 'menu3':
        menu3()

    elif etat == 'menu4':
        menu4()

    elif etat == 'menu5':
        menu5()
        print(race_perso,classe_perso)

    pygame.display.flip()

pygame.quit()


