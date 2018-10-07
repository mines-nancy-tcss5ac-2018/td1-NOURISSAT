# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:06:16 2018

@author: Ben Hur
"""

def extract(fichier):
    """Extraxt the list of names from the given txt file."""
    names = []
    for line in open(fichier, 'r'):
        for almost_name in line.split(','):
            names.append(almost_name[1:len(almost_name)-1]) 
    return [i for i in names if i != '']



fichier = 'p022_names.txt'
test = extract(fichier)
test_trie = sorted(test)




alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']




def value(name):
    """Return the value of a name."""
    return sum(alpha.index(str(l)) + 1 for l in name)

assert value('COLIN') == 53





def score(name):
    """Return the score of a name."""
    return (sorted(test).index(name)+1)*value(name)

assert score('COLIN') == 49714





def solve(fichier):
    """Solve the 22nd Euler probleme."""
    return sum(score(name) for name in extract(fichier))

print(solve(fichier))
