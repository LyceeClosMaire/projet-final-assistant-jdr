from random import * #importation de l'aléatoire

def lancer_des(nb_lancers, nb_faces): # il s'agit ici de la definition de plusieurs jets de dés
    resultats = [] # la liste
    for lancer in range(nb_lancers): # pour lancer pour un certains nombre de lancé
        resultats.append(randint(1,nb_faces)) # on a le resultat ajouter (donc une liste de nombre) sera alétoire sur un dé allant de 1 à une valeur définie
    return(sum(resultats)) # on affiche la somme des résultats

def action():
    s=input('que voulez-vous faire ?')
    if s[:6].upper() == 'LANCER':
        info = s.split(' ')
        for u in range(len(info)):
            if info[u].upper() in ['DÉS','DÉ']:
                nb_des = int(info[u-1])
            elif info[u].upper() in ['DE','À']:
                k = int(info[u+1])
    if nb_des > 1 : #si on effectue plusieur lancés
        print ("Pour", nb_des,"lancer de dés de",k,": Vous avez le score de",lancer_des(nb_des,k)) # affichge du nombre de lancer et de la valeur du dé ainsi que sa somme



action()

#ici on est dans le cas d'un multiple (en général un jet de dégat)____________________________________________________________________




