def quintuplet(S):
    L = 5*[None]
    for i in range(1,S+1):
        for ii in range(1,S+1):
            for iii in range(1,S+1):
                for iv in range(1,S+1):
                    for v in range(1,S+1):
                        if i < ii < iii < iv < v and i+ii+iii+iv+v == S:
                            L = [i,ii,iii,iv,v]
                            print(L)

#quintuplet(18)


def est_solution(N,S,t):
    return t == sorted(t) and sum(t) == S

def ajout_possible(p,N,S,t):
    return 0<=p<N and sum(t[:p])<S and t[:p] == sorted(t[:p])

def placer(p,N,S,t):
    if p == N:
        if est_solution(N,S,t):
            print(t)

    else :
        if p == 0 :
            deb = 1
        else : deb = t[p-1]+1
        for i in range(deb, S):
            if ajout_possible(p,N,S,t):
                t[p] = i
                placer(p+1,N,S,t)
  


    

def nuc(N,S):
   t = N*[None]
   p = 0
   placer(p,N,S,t)

nuc(5,18)
nuc(3,9)