from random import * #importation de l'aléatoire

lancer = int(input("combien de lancer voulez vous ?:")) # sélection du nombre de lancer de dé

for i in range (lancer): # boucle de lancer
    k =int(input("dé de combien ?")) # nous demande quelle type de dé on veut lancé
    de=randint(1,k) # chercher une valeur aléatoire sachant que le dé à une valeur compris entre 1 et k; k étant valeur défini par nous
    if lancer > 1 :
        k = 6
        print (de)
    elif lancer == 1 :
            stat = int(input("Entrer votre statistique")) # valeur de la statistique du personnage
            if stat >= de  : # Si la condition est supérieur à la valeur du dé
                print ("réussite") # on affiche réussite
            elif stat < de : # Si la condition est inférieur a la valeur du dé
                print ("échec") #on affiche échec
                print(de,"/",stat) # afficher le résultat du dé sur la statistique




def lancer_des(nb_lancers, nb_faces):
    if lancer > 1 :
        k = 6
        print (de)
        return somme