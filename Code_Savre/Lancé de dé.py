from random import * #importation de l'aléatoire

lancer = int(input("combien de lancer voulez vous ?:")) # sélection du nombre de lancer de dé
k =int(input("dé de combien ?")) # nous demande quelle type de dé on veut lancé
de=randint(1,k) # chercher une valeur aléatoire sachant que le dé à une valeur compris entre 1 et k; k étant valeur défini par nous

def lancer_des(nb_lancers, nb_faces): # il s'agit ici de la definition de plusieurs jets de dés
    resultats = [] # la liste
    for lancer in range(nb_lancers): # pour lancer pour un certains nombre de lancé
        resultats.append(randint(1,nb_faces)) # on a le resultat ajouter (donc une liste de nombre) sera alétoire sur un dé allant de 1 à une valeur définie
    return(sum(resultats)) # on afiche la somme des résultats


#ici on est dans le cas d'un multiple (en général un jet de dégat)____________________________________________________________________


if lancer > 1 : #si on effectue plusieur lancés
    print(lancer_des(lancer,k)) # alors on effectue la fonction lancé de dé


#ici on est dans le cas d'un jets simple (de statistique du personnage)_______________________________________________________________


if lancer == 1 : # si on effectue qu'un seul lancé
        stat = int(input("Entrer votre statistique")) # valeur de la statistique du personnage
        if stat >= de  : # Si la condition est supérieur à la valeur du dé
            print ("réussite") # on affiche réussite
            print(de,"/",stat) # afficher le résultat du dé sur la statistique
        elif stat < de : # Si la condition est inférieur a la valeur du dé
            print ("échec") #on affiche échec
            print(de,"/",stat) # afficher le résultat du dé sur la statistique





