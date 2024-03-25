#HASH MAPA 
n=10

def hashfunc(number):
    global n
    return number % n

def lookup(list,number):
    lista=list[hashfunc(number)]
    return number in lista

def add(lista,number):
    if not lookup(lista,number):
        lista[hashfunc(number)].append(number)
    return lista

lista=[[] for i in range(n)]

lista=add(lista,101)
lista=add(lista,777)
lista=add(lista,145)
lista=add(lista,134)
lista=add(lista,666)
lista=add(lista,7)

for i in range(n):
  print("[" + str(i) + "]\t", end ='')
  for el in lista[i]:
    print(el, end =' ')
  print()


x=lookup(lista,677)

print(x)

mojalista=[21,12,3,14,3,254,523,542346,435,6346,35,74,84,85743567,457457,45,746,56,456457,654,756,8,758,4,7457,7,65,75957,987,98978,965,6744,67]

for i in range(len(mojalista)):
   lista=add(lista,mojalista[i])

for i in range(n):
  print("[" + str(i) + "]\t", end ='')
  for el in lista[i]:
    print(el, end =' ')
  print()

example = [333, 987, 456]
for el in example:
	wynik = lookup(lista, el)
	print(str(el) + "\t" + ("jest" if wynik else "nie ma"))

#Zadanie 1: Unikalne Elementy
#Napisz funkcję, która przyjmuje listę elementów i używa funkcji haszującej, aby zwrócić listę zawierającą tylko unikalne elementy z wejściowej listy.
    
lista=[1,22,33,44,44,55,55,66,777]
n=10

def hashf(elem):
    return elem%n
    
def mojafunkcja(lista):
    nowalista=[[] for _ in range(n)]
    for elem in lista:
        index=hashf(elem)
        if elem not in nowalista[index]:
            nowalista[index].append(elem)
    return nowalista

print(mojafunkcja(lista))

#adanie 2: Sprawdzanie Anagramów
#Napisz funkcję, która sprawdza, czy dwa podane słowa są anagramami. Użyj funkcji haszującej do obliczenia wartości hasz dla obu słów i porównaj je, aby ustalić, czy słowa są anagramami. 
#Pamiętaj, że anagramy to słowa lub frazy utworzone przez przestawienie liter innego słowa lub frazy, używając wszystkich oryginalnych liter dokładnie raz.

def hashword(word):
    count={}
    for char in word:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    hashtuple=tuple(sorted(count.items()))
    return hashtuple

def isanagram(word1,word2):
    return hashword(word1)==hashword(word2)

print(isanagram("krowa","worka"))

#v2

from collections import Counter

def isanagram(word1, word2):
    return Counter(word1) == Counter(word2)

print(isanagram("krova", "worka"))