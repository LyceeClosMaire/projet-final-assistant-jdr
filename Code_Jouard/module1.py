import csv                                           # j'importe de quoi lire et modifier mes dossiers qui me serviront pour les personnages
import os
import pygame
from pygame.locals import *                          #j'importe pygame afin d'ouvrir des fenêtres de choix

pygame.init()

blanc = (255,255,255)
noir = (0,0,0)
fenetre = pygame.display.set_mode((1200, 800 ))
font = pygame.font.Font('BradBunR.ttf',50)
etat= 'menu'
ouvert = 1


def menu():
    global etat
    fenetre.fill( blanc)
    Gt = font.render("Cliquez pour continuer",1,noir)
    fenetre.blit(Gt,(355,350))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            etat = 'menu2'

def truc():
    fenetre.fill( (127,127,127))


def menu2():

    fenetre.fill( blanc)
    texte1 = font.render("Charger un ancien personnage",1,noir)
    texte2 = font.render("Créer un nouveau personnage",1,noir)
    bouton1 = pygame.draw.rect(fenetre,(255,255,200),(300,200,600,75))
    bouton2 = pygame.draw.rect(fenetre,(200,255,255),(300,500,600,75))
    fenetre.blit(texte1,(325,200))
    fenetre.blit(texte2,(325, 500))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and bouton1.collidepoint(souris):



##def fermeture():
##
##        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
##            ouvert = 0
##    pygame.display.flip()
##
##pygame.quit()
##quit()




while ouvert:

    souris = pygame.mouse.get_pos()

    if etat == 'menu':
        menu()

    elif etat == 'truc':
        truc()

    elif etat == 'menu2':
        menu2()










        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            ouvert = 0
    pygame.display.flip()

pygame.quit()


