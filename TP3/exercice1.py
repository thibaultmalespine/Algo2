# PE : soit T une liste non vide et A,B,C trois entier tel que 0<=A<=B+1<=C+1<= len(T) et (T[A:B+1],<) et (T[B+1:C+1],<)
# PS : une liste tab, tel que tab[A:C+1] = sorted(T[A:B+1] + T[B+1:C+1]), et tab[:A] = T[:A] et tab[C+1:] = T[C+1:]

# Triplet de Hoare : {PE} fusion(T,A,B,C) {PS}

def fusion(T,A,B,C):
    pass

# Jeu de test : 
# Cas Spécifique
assert fusion([0,1,2,1,6,7],1,2,4) == [0,1,1,2,6,7]

# Cas Particuliers 
# T déjà trié
# un sous tableau vide
# l'autre vide
# les deux vides
# T[A:C+1] = T
# les deux sous tableaux avec une seule valeur

