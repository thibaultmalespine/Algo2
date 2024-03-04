# 1- si b < w <= r alors le trie du tableau n'est pas fini 
#    si b < r < w alors le trie est fini
def drapeau_hollandais(t):
    pass
# 2- jeu de test 
# cas significatif
assert drapeau_hollandais([0,1,2,2,1,0,2,1,0]) == [0,0,0,1,1,1,2,2,2]
# cas particulier
assert drapeau_hollandais([0,1,0,1]) == [0,0,1,1]
assert drapeau_hollandais([2,1,2,1]) == [1,1,2,2]
assert drapeau_hollandais([2,0,2]) == [0,2,2]
assert drapeau_hollandais([0,1,2]) == [0,1,2]
assert drapeau_hollandais([0,0,0]) == [0,0,0]
assert drapeau_hollandais([1,1,1]) == [1,1,1]
assert drapeau_hollandais([2,2,2]) == [2,2,2]
assert drapeau_hollandais([]) == []