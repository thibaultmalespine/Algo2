def quatres_reines():
    for x1 in range(4):
        for x2 in range(4):
            for x3 in range(4):
                for x4 in range(4):
                    if ligne_dif(4,[x1,x2,x3,x4]) and diagonale_dif(4,[x1,x2,x3,x4]):
                        afficherPlateau([x1,x2,x3,x4])
                    



def ligne_dif(p,L):
    
    pasMemeLigne = True
    for i in range(p):
        for y in range(i+1,p):
            if L[i] == L[y] :
                pasMemeLigne = False
    return pasMemeLigne

def diagonale_dif(p,L):
    pasMemeDiagonale = True
    for i in range(p):
        for y in range(i+1,p):
            if abs((y-i)/(L[y]-L[i])) == 1 :
                pasMemeDiagonale = False

    return pasMemeDiagonale



def n_reine(n):
    listeSol=[]
    sol=n*[None]
    p= 0
    placer(p,sol,listeSol)
    return listeSol

def placer(p,sol,listeSol):
    if p == len(sol) and est_solution(sol):
        listeSol.append(sol[:])
    elif p < len(sol):
        for i in range(len(sol)):
            if ajout_possible(p,sol):
                sol[p] = i
                placer(p+1, sol, listeSol)
        sol[p] = None
          

def est_solution(sol):
    return ligne_dif(len(sol),sol) and diagonale_dif(len(sol),sol)

def ajout_possible(p,sol):
    return ligne_dif(p,sol) and diagonale_dif(p,sol)

def afficherPlateau(P):
    for i in range(len(P)):
        for ligne in P:
            if i == ligne : print('|X', end='')
            else : print("| ", end='')
        print('|')

    print('')
        

#quatres_reines()
for plateau in n_reine(5):
    afficherPlateau(plateau)