#Fibo_n
#Funkcja, ktora zwraca n-ta liczbe Fibo

def fibo(n):
    if n<=0:
        return 0
        
    elif n==1:
        return 1
        
    elif n>1:
        return fibo(n-1)+fibo(n-2)
        
print(fibo(5))
#O(2^n)

def fibociag(n):
    lista=[]
    suma=0
    for x in range(0,n+1):
        lista.append(fibo(x))
        suma+=fibo(x)
    return lista,suma

print(fibociag(5))

#v2

def fibo2(n):
    if n<=0:
        return 0
    
    elif n==1:
        return 1
    
    else:
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
    
print(fibo2(5))
#O(n)

    
