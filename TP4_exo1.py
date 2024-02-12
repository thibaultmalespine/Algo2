
def quadruplets():
    cpt = 0
    for i in range(4):
        for ii in range(4):
            for iii in  range(4):
                for iv in range(4):
                    if i!=ii and iii!=iv and i+iii < ii:
                        cpt = cpt + 1
    print(cpt)


#quadruplets()

global cpt
global solution
solution = 0
cpt = 0

def ajout_possible(p,sol):
        is_true = True
        if p==0 and sol[0] == 3:
            is_true = False
        if p==1 and sol[0] == sol[1]:
            is_true = False
        if p==1 and sol[0] > sol[1]:
            is_true = False

        if p==2 and sol[0] + sol[2] >= sol[1]:
            is_true = False
        if p==3 and sol[2] == sol[3]:
            is_true = False

         
        return is_true
        

def est_solution(sol):
    return sol[0]!=sol[1] and sol[2]!=sol[3] and sol[0]+sol[2] < sol[1]
L_sol = []
def backtracking(p, N, sol ):
    global solution
    global cpt
    cpt+=1
    if p == N:
        if (est_solution(sol)):
            L_sol.append(sol)
            print(sol)

    else :
        for value in range(4):
            sol[p] = value 
            if ajout_possible(p,sol):
                backtracking(p+1, N, sol)
            
          

backtracking(0,4,[0,0,0,0])
print(cpt)
print(len(L_sol))