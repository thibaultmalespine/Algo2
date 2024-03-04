# 1-a) La fonction tableau_surveille permet de savoir si il existe dans la liste des gardiens LG 
# au moins un gardien à 2 mètre ou moins du tableau T  


# 1-a) Prédicat d'entrée : Soit LG[0 .. N] un tableau de réel de taille N+1, et T un réel ∈ R+

# Prédicat de sortie : on note res le résultat de la fonction :
#       res = true => ∃ i, i ∈ ⟦ 0 ; N ⟧, | LG[i] - T | <= 2 
#       res = false => ∀ y, y ∈ ⟦ 0 ; N ⟧, | LG[y] - T | > 2 

# b)
def tableau_surveille(LG,T):
    assert True ,"PE"
    i=0
    while i<len(LG) and abs(LG[i]-T)>2 :
        i+=1
    return i<len(LG)
# version impérative
def bs(LG,LT):
    drapeau = True
    for T in LT:
        if(tableau_surveille(LG,T) == False):
            drapeau = False
    return drapeau
# version récursive
def bsr(LG,LT):
    if len(LT) == 0 :
        return True
    elif len(LG) == 0 :
        return False
    else :
        return (abs(LT[0]-LG[0]) <= 2 or bsr(LG[1:],[LT[0]])) and bsr(LG,LT[1:])   
# jeu de test
def test1(f) :
    
    # cas significatifs
    assert f([1,5,3],[1,2,4,5.2,7,8.4]) == False
    assert f([2,7],[1,2,4,5.2,7,8.4])

    # cas particuliers
    assert f([],[5]) == False
    assert f([2,7],[])

test1(bs)
test1(bsr)

# 2-1) PS : res = true => bs(lg,LT) = true 
#           res = false => bs(lg,LT) = false

# 2-2) musee([1,2,4,5.2,8.4]) = [3, 7.2] 

# 2-4)
def musee (LT) :
    assert len(LT)>0 and LT==sorted(list(set(LT))) # '' PB PE''
    N=len(LT)
    i=0 #indice du dernier tableau traité
    lg=[LT[i]+2] #choix glouton
    j=0 #indice du dernier gendarme placé
    #INV : les gendarmes de lg[:j+1] déjà placés surveillent les tableaux de LT[:i+1]
    assert bs(lg[:j+1], LT[:i+1])  # '' PB init''
    
    while i < N-1 :
        #INV et CC : les gendarmes de lg[:j+1] déjà placés surveillent les tableaux de LT[:i+1] et CC
        assert bs(lg[:j+1], LT[:i+1]) 
        assert i < N-1
        
        if abs(LT[i+1] - lg[j]) > 2 :
            lg.append(LT[i+1]+2) #placer un nouveau gendarme (choix glouton)
            j+=1
        i+=1 #passer au tableau suivant
        #INV : les gendarmes de lg[:j+1] déjà placés surveillent les tableaux de LT[:i+1]
        assert bs(lg[:j+1], LT[:i+1] ) # '' PB fin d'itération''
    
    #INV et non(CC)
    assert bs(lg[:j+1], LT[:i+1]) and i==N-1 # '' PB sortie de boucle''
    #PS
    assert bs(lg,LT) # '' PB PS''
    return lg

# 2-3) jeu de test :
# cas significatif
assert musee([1,2,4,5.2,8.4]) == [3, 7.2]
# cas particuliers
assert musee([0,15]) == [2, 17]
assert musee([5]) == [7]