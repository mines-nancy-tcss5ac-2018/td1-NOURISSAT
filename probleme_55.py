# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:33:07 2018

@author: nourissa1u
"""

def reverse_str(string):
    """Return the miror image of the number."""
    string_reversed = ""
    for l in string:
        string_reversed = l + string_reversed
    return string_reversed

assert(reverse_str("abcd") == "dcba")







def palindromic(nombre):
    """Return True if a number is a palindromic or False if it isn't."""
    str_nb = str(nombre)
    if reverse_str(str_nb) == str_nb:
        return True
    else:
        return False

assert palindromic(12345654321) == True




def solve(nombre):
    """"Solve the 55th Euler probleme: return the number of Lychrel numbers below ten-thousand"""
    compteur = 0
    for nb in range(nombre):
        nb_itered = nb
        iteration = 0
        while iteration != 50 and palindromic(nb_itered) == False:
            nb_itered = nb_itered + int(reverse_str(str(nb_itered)))
            iteration += 1
        if palindromic(nb_itered) == False:
            compteur += 1
    return compteur
            
        

    
print(solve(10000))

    
    
    