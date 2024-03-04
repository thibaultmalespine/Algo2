# 2)
def insertion(t,K):
    N=len(t)
    T=t[:] #T est une copie utilisée pour garder les valeurs initiales
    assert N>1 and 0<K<N and T[:K] == sorted(T[:K])
    j = K
    x = T[K]
    assert inv(j,K,t,T,x)
    while j!=0 and t[j-1]>x:

        assert inv(j,K,t,T,x)
        assert j!=0 and t[j-1]>x
        t[j] = t[j-1]
        t[j-1] = x
        j = j-1
        assert inv(j,K,t,T,x)

    assert inv(j,K,t,T,x) and (j==0 or t[j-1]<=x)
    t[j]=x
    t[:K+1] == sorted(t[:K+1]) and sorted(t[:K+1]) == sorted(T[:K+1])
    
    return t

def inv(j,K,t,T,x):
    return 0<=j<=K and x==T[K] and t[:j]==T[:j] and t[j:K+1]==sorted(t[j:K+1])


# 1) jeu de test :
# cas significatif
assert insertion([1,5,6,8,7,4,2,3],4) == [1,5,6,7,8,4,2,3]
# cas particuliers
assert insertion([1,5,6,8,7,4,2,3],3) == [1,5,6,8,7,4,2,3]
assert insertion([5,1],1) == [1,5]
assert insertion([5,6],1) == [5,6]

#3)
def tri_insertion(t):
    for k in range(1,len(t)) :
        insertion(t,k)
    return t

from copy import deepcopy
from random import randint
#E : une fonction de tri : tri_a_tester
#génère 1000 listes et vérifie qu’elles sont bien triées par tri_a_tester
#S : affichage d’un message
def test_tri( tri_a_tester ) :
    pb=False
    for i in range(1000) : #nombre de tris
        nb=randint(2,10) #longueur de la liste a trier
        #génération d'une liste aléatoire de nb nombres de [-10,10]
        T=[randint(-10,10) for _ in range(nb)]
        t=deepcopy(T)
        if sorted(T) != tri_a_tester(t) : #liste triée avec la fonction à tester
            pb=True
            print('Pb :')
            print(T)
            print(t)
    if not(pb) :
        print( 'Ok' )
#……………………………………………………………………………………...
#appel de la fonction test_tri pour le tri_insertion
test_tri(tri_insertion) 