#NWD

#v1

def NWD(x,y):
    lista=[]
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            lista.append(i)
    
    if lista !=[]:
        x=max(lista)
        return f"NWD to {x}"
    else:
        return f"brak NWD"
    
print(NWD(15,29))

#v2

def Euklides(x,y):
    while y:
        x,y=y,x%y
        #print(x,y)
    return f"NWD to {x}"

print(Euklides(300,600))