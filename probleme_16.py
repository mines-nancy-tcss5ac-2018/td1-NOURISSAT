# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def solve(n):
    "Solve the 16th Euler probleme : Return the sum of the digits of 2**n"
    puissance_de_2 = str(2**n)
    return sum(int(puissance_de_2[i]) for i in range (len(puissance_de_2)))
    
    
    
    
    
    
    
assert(solve(15) == 26)
print("La solution au problème 16 est ", solve(1000))