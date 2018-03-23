import pygame, sys
from pygame.locals import *

#Constantes de couleurs

NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)

#Les sprites de la map

TERRE = 0
HERBE = 1
EAU = 2
MUR = 3

#Une liste associant les couleurs aux sprites

couleur = {
            MUR : NOIR,
            HERBE : VERT,
            EAU : BLEU,
            TERRE : ROUGE,
            }
tilemap = [
            [MUR, MUR, MUR,  MUR, MUR],
            [MUR, EAU, EAU,  EAU, MUR],
            [MUR, EAU, TERRE,EAU, MUR],
            [MUR, EAU, EAU, EAU,  MUR],
            [MUR, MUR, MUR, MUR,  MUR],

            ]

TAILLE = 40
LONGUEUR = 5
LARGEUR = 5

pygame.init()
debut = pygame.display.set_mode