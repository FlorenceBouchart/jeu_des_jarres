

import random

try_again = 'OUI'
niveau = 10
jarres = []
trousseau = 0

def choix_niveau(niveau) : 
    global jarres
    while niveau < 1 or niveau > 3 : 
        niveau = int(input("1 : niveau 1\n2 : niveau 2 \n3 : niveau 3\n",))
    if niveau == 1 : 
        jarres = ['key','snake','key','key','key']
        print("Une seule des 5 jarres contient un serpent, ne te trompes pas !\n")
    elif niveau == 2 : 
        jarres = ['key','snake','key','snake','key']
        print("Deux des 5 jarres contiennent des serpents, ne te trompes pas !\n")
    elif niveau == 3 : 
        jarres = ['key','snake','snake','snake','key']
        print("Trois des 5 jarres contiennent des serpents, ne te trompes pas !\n")

def choix_jarres(jarres) :
    global trousseau
    random.shuffle(jarres)
    choice = int(input("Choisis une jarre parmi les 5 :\n- 1 : jarre 1 \n- 2 : jarre 2 \n- 3 : jarre 3 \n- 4 : jarre 4 \n- 5 : jarre 5 \n",))-1
    while int(choice) > 5 and int(choice) < 0 : 
        choice = int(input("Cette jarre n'existe pas \n Choisis une jarre parmi les 5 : \n - 1 : jarre 1 \n- 2 : jarre 2 \n- 3 : jarre 3 \n- 4 : jarre 4 \n- 5 : jarre 5 \n",))-1
    if jarres[choice] == 'key' : 
        print("Vous avez trouvé une clé !")
        trousseau +=1
        print(f'\nVous possédez désormais {trousseau} clés.\n')
    elif jarres[choice] == 'snake' : 
        if trousseau > 0 : 
            print("Le serpent vous vole une clé !")
            trousseau -=1
            print(f'\nVous possédez désormais {trousseau} clés.\n')
        else : 
            trousseau = 4


while try_again == 'OUI' : 
    choix_niveau(niveau)
    
        
    print("Trouve 3 clés : \n")
    trousseau = 0
    while trousseau < 3 :
        choix_jarres(jarres)
    if trousseau == 3 : 
        print("Tu deviens roi du temple!")
    else : 
        print("Le serpent n'a pas trouvé de clé à te voler. Pour se venger il s'en est pris à toi et tu as dû abandonner ta quête !")

    try_again = input("Jouer à nouveau ? OUI / NON  ",)
    while try_again != 'OUI' and try_again != 'NON' : 
        try_again = input("Entrée incorrecte\nJouer à nouveau ? OUI / NON  ",)

