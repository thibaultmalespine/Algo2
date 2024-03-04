def ppp_imp(L):
    for i in range(len(L)):
        

# cas significatif
assert ppp_imp([1,8,7,5,5,6,8]) == 2
assert ppp_imp([1,8,7,5,5,6,7]) == 2
# cas particulier
assert ppp_imp([]) == 0
assert ppp_imp([2,4,6,8]) == 3
assert ppp_imp([1,3,5,7]) == 0
assert ppp_imp([2,4,6,7]) == 3
assert ppp_imp([1,3,5,8]) == 0
