import csv                                           # j'importe de quoi lire et modifier mes dossiers qui me serviront pour les personnages
import pygame
from pygame.locals import *                          #j'importe pygame afin d'ouvrir des fenêtres de choix

pygame.init()

blanc = (255,255,255)
noir = (0,0,0)
fenetre = pygame.display.set_mode((1200, 900 ))
font = pygame.font.Font('BradBunR.ttf',50)
etat= 'menu'

def menu():
    fenetre.fill( blanc)
    Gt = font.render("Cliquez pour continuer",1,noir)
    fenetre.blit(Gt,(355,350))

def truc():
    fenetre.fill( (127,127,127))


def menu2():
    fenetre.fill( blanc)
    texte1 = font.render("Charger un ancien personnage",1,noir)
    texte2 = font.render("Créer un nouveau personnage",1,noir)
    fenetre.blit(texte1,(350,250))
    fenetre.blit(texte2,(350, 550))


















ouvert = 1
while ouvert:


    if etat == 'menu':
        menu()

    if etat == 'truc':
        truc()

    if etat == 'menu2':
        menu2()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            etat = 'menu2'








        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            ouvert = 0
    pygame.display.flip()

pygame.quit()
quit()

