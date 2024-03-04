sudo = [0, 8, 7, 0, 0, 0, 5, 2, 0,
        9, 1, 0, 5, 0, 2, 0, 4, 6,
        2, 0, 0, 0, 0, 0, 0, 0, 7,
        0, 9, 0, 0, 2, 0, 0, 1, 0,
        0, 0, 0, 1, 0, 6, 0, 0, 0,
        0, 4, 0, 0, 9, 0, 0, 8, 0,
        6, 0, 0, 0, 0, 0, 0, 0, 3,
        5, 7, 0, 3, 0, 1, 0, 6, 8,
        0, 3, 8, 0, 0, 0, 9, 5, 0]


def ajout_possible(ligne,colonne,région):
    bRetour = True
    
    liste_ligne = [sudo[i] for i in range(ligne*9, (ligne*9)+9)]
    liste_colonne = [sudo[i] for i in range(colonne, 81, 9)]
    liste_région = []
    for i in range(3*(région%3), 3*(région%3)+3):
        for y in range(3*(région//3), 3*(région//3)+3): 
            liste_région.append(sudo[i+9*y])
 
   
    for i in range(1,10):
        if liste_ligne.count(i) == 2 : bRetour = False
        if liste_colonne.count(i) == 2 : bRetour = False
        if liste_région.count(i) == 2 : bRetour = False
        
    return bRetour

    

def sudokus(sudo, r):
    if r == 81:
        afficher(sudo)
        return
        
    if sudo[r] != 0:
        sudokus(sudo, r+1)
    else:
        ligne = r//9
        colonne = r%9
        région = 3*(ligne//3)+(colonne//3)
        for i in range(1,10):
            sudo[r] = i
         
            if ajout_possible(ligne, colonne, région):
                sudokus(sudo, r+1)
            else :
                sudo[r] = 0
       
                
def afficher(sudo):
    print("")
    for i in range(9):
        print(sudo[i*9:(i*9) + 9])
        
    print("")
sudokus(sudo, 0)
