#Exponentiation by squaring

def EBS(x,n):
    if n==0:
        return 1
    elif n%2!=0:
        return x*EBS(x,n-1)
    else:
        a=EBS(x,n//2)
        return a**2
    
print(EBS(7,6))

def EBS(x,n):
    if n==0:
        return 1
    elif n%2!=0:
        return x*EBS(x,(n-1)//2)**2
    else:
        return EBS(x,n//2)**2
        
    
print(EBS(7,6))