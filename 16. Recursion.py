#Recursion

#1
def silnia(x):
    if x==0 or x==1:
        return 1
    else:
        return x*silnia(x-1)

test=silnia(9)
print(test)

#2

ciag=[1,2,3,4,5,6,7,8,9]
n=len(ciag)

def sumaciagu(ciag,n):
    if n==0:
        return 0
    else:
        return sumaciagu(ciag,n-1)+ciag[n-1]

print(sumaciagu(ciag,n))
              
#3

liczba=3456

def odwrocliczbe(liczba):
    liczba_str=str(liczba)
    if len(liczba_str)==1:
        return liczba_str
    else:
        return liczba_str[-1] + odwrocliczbe(int(liczba_str[:-1]))
 
print(odwrocliczbe(liczba))

#4
lista=[123,23,123,12,3412,423,432,423,432432423,4324234324,34215]
lista=sorted(lista)
print(lista)

def binary_search(lista,low,high,x):

    if high>=low:
        mid=(high+low)//2

        if lista[mid]==x:
            return f"znalezione na pozycji {mid+1}"
        
        elif lista[mid]>x:
            return binary_search(lista,low,mid-1,x)
        
        else:
            return binary_search(lista,mid+1,high,x)
        
    else:
        return "ni ma i nie bedzie"
    
print(binary_search(lista,0,len(lista)-1,34125))

#5

def drzewo(n):
    if n == 0:
        print("Silnia z 0 = 1")
        return 1
    else:
        print(f"Silnia z {n} = {n} * Silnia z {n-1}")
        result = n * drzewo(n-1)
        return result

drzewo(3)