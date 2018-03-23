import pygame

pygame.init()
pygame.font.init()

RUNNING = True

fenetre = pygame.display.set_mode((800,600))

font = pygame.font.SysFont('Comic Sans MS', 20)

def gerer_events():     #ECHAP = quitte
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

def menu():
    rect = pygame.draw.rect(
        fenetre,
        (0,128,0),
        pygame.Rect(100, 200, 100, 100))

    text = font.render('ButtonA', False, (255,255,255))
    fenetre.blit(text, (100, 200))

    gerer_souris_menu(rect)

def gerer_souris_menu(rectangle):
    global afficher

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        mouse_pos

afficher = menu



###################

def boucle():
    while RUNNING:
        fenetre.fill( (0,0,0) )

        gerer_events()

        afficher()

        pygame.display.update()

    pygame.quit()

boucle()