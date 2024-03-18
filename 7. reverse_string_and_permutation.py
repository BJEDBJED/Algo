#odwracanie ciagu znakow

def reverse_string(string):
    return string[::-1]

def reverse_string2(string):
    return " ".join(reversed(string))

string="przykladowy kawalek tekstu."
print(reverse_string(string))
print(reverse_string2(string))

#permutacje tekstu
import random

def permutation(string):
    if len(string)<=1:
        return set(string)
    
    permutations=[]
    for elem in permutation(string[1:]):
        for i in range(len(string)+1):
            permutations.append(elem[:i]+string[0:1]+elem[i:])
    return set(permutations)
    
string="xtb"    
print(permutation(string))
