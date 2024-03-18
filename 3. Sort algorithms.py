# Sort algorithms

#quickSort

lista=[23,45,76,29,45,19,21,83]

def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        pivot=lista[len(lista)//2]
        left=[x for x in lista if x<pivot]
        mid=[x for x in lista if x==pivot]
        right=[x for x in lista if x>pivot]
        return quicksort(left)+mid+quicksort(right)

x=quicksort(lista)
print(x)

#mergesort

lista=[23,45,76,29,45,19,21,83]

def mergesort(lista):
    if len(lista)>1:
        mid=len(lista)//2
        left=lista[:mid]
        right=lista[mid:]

        mergesort(left)
        mergesort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lista[k]=left[i]
                i+=1
            else:
                lista[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            lista[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            lista[k]=right[j]
            j+=1
            k+=1
       
mergesort(lista)
print(lista)