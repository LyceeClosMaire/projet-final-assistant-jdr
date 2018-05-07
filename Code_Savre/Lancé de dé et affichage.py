from random import * #importation de l'aléatoire

def lancer_des(nb_lancers, nb_faces): # il s'agit ici de la definition de plusieurs jets de dés
    resultats = [] # la liste
    for lancer in range(nb_lancers): # pour lancer pour un certains nombre de lancé
        var =randint(1,nb_faces) # résultat d'un dé allant de 1 à une valeur définie
        print('Lancer n°'+str(lancer+1)+' du dé de ' + str(nb_faces) +': '+str(var)) # afficher les détails de chaque lancés
        resultats.append(var) # on a le resultat ajouter (donc une liste de nombre) sera alétoire sur un dé allant de 1 à une valeur définie
    return(sum(resultats)) # on affiche la somme des résultats

def action(): # definition de la fonction action


    que_faire = input('Que faire ?') # variable que_faire
    total = 0
    txt = que_faire.split('+') # Séparation des +

    if 'ds' in txt[0]: # Si on trouve 'ds' dans le jet, c'est un jet de stat

        #ici on est dans le cas d'un jets simple (de statistique du personnage)
        k = int(txt[0].split('ds')[1]) # même chose qu'à la ligne 18 sauf qu'on prend le nombre de face et pas nombre de dés
        de=randint(1,k)# chercher une valeur aléatoire sachant que le dé à une valeur compris entre 1 et k; k étant valeur défini par nous
        if len(txt) == 2:
            de -= int(txt[1])
        stat = int(input("Entrer votre statistique")) # valeur de la statistique du personnage
        if stat >= de  : # Si la condition est supérieur à la valeur du dé
            print ("réussite") # on affiche réussite
            print(de,"/",stat) # afficher le résultat du dé sur la statistique
        elif stat < de : # Si la condition est inférieur a la valeur du dé
            print ("échec") #on affiche échec
            print(de,"/",stat) # afficher le résultat du dé sur la statistique

    else: #sinon
        #ici on est dans le cas d'un multiple (en général un jet de dégat)
        for item in txt: # pour item dans txt
            if 'd' in item: # si il y a un d dans item
                var = item.split('d') # alors on sépare item en fonction de d
                nb_lances = int(var[0]) # par exemple dans 10d6 ici on parle du 10
                nb_faces = int(var[1]) # par exemple dans 10d6 ici on parle du 6
                total += lancer_des(nb_lances,nb_faces) # ici on addition les totaux (var étant une fonction)
            else: #sinon
                total += int(item) #on ajoute juste la valeur au total par exemple +7

        print(total) # afficher le total



action() #sa appelle la fonction action






