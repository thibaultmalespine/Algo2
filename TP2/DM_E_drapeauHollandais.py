# Malespine Thibault

def inv(b,w,r,T,t):
   ok1= 0<=b<=w<=r+1<=len(T)
   ok2= b==0 or set(t[:b])=={0}  
   ok3= b==w or set(t[b:w])=={1}
   ok4= r+1==len(T) or set(t[r+1:])=={2} 
   return ok1 and ok2 and ok3 and ok4 and sorted(t)==sorted(T)

def PS(b,w,r,T,t):
   ok1= 0<=b<=w and w==r+1<=len(T)
   ok2= b==0 or set(t[:b])=={0}  
   ok3= b==w or set(t[b:w])=={1}
   ok4= w==len(T) or set(t[w:])=={2} 
   return ok1 and ok2 and ok3 and ok4 and sorted(t)==sorted(T)


#PE: len(T)>=0
#
#PS: Ai: 0<=i<b -> t[i]=0  ET Ai: b<=i<=r -> t[i]=1 ET Ai: r<i<len(t) -> t[i]=2 ET t=permut(T) 
def drapeau_hollandais(t):
   assert set(t) <= {0,1,2} , "PE"
   T=t[:]
   b=0
   w=0
   r=len(t)-1
   #INV:: 0<=b<=w<=r+1<=len(T) ET Ai: 0<=i<b -> t[i]=0  ET Ai: b<=i<w -> t[i]=1 ET Ai: r<i<len(t) -> t[i]=2 ET t=permut(T)
   assert inv(b,w,r,T,t)  , "Etape 1: initialisations"
   while w<=r:
      #INV ET CC
      assert inv(b,w,r,T,t) and w<=r , "entree boucle"
      B=(r+1)-w   # on affecte la valeur de la variante a B
      assert B>0 ,"Etape 4: la variante est > 0 "
      
      if t[w] == 0:
         t[b],t[w] = t[w],t[b]
         w+=1
         b+=1
      elif t[w] == 1:
         w+=1
      else:
         t[w],t[r] = t[r],t[w]
         r-=1

      assert (r+1)-w<B  ,"Etape 5 : la variante est strictement decroissante"  
      assert inv(b,w,r,T,t)  , "Etape 2: fin iteration"   

   assert inv(b,w,r,T,t) and w>r , "Etape 3: sortie de boucle"   
   #INV ET not(CC)
   #PS
   assert PS(b,w,r,T,t) , "PS"
   return t



from copy import deepcopy
from random import randrange


def test_tri(tri):
    ok=True
    for i in range(10000):
        n=randrange(10)
        #generation d'une liste aleatoire de longueur n d'entiers 0,1 ou 2
        T=[randrange(0,3) for p in range(n)] 
        t=deepcopy(T)
        if sorted(T)!=tri(t):
            ok=False 
            print ("Erreur")
            print(T)
            print(t)
    if ok:
        print("Ok")
 
##################################################################################

t=[2,1,0,1,0,1,0,2,2,1]
print(t)
print(drapeau_hollandais(t))
print(" ")    
        
print("Tests drapeau hollandais:")
test_tri(drapeau_hollandais)

