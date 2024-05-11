#max algo

#Kupno i Sprzedaż Akcji - Jedna Transakcja:
#Problem: Mając tablicę, która reprezentuje cenę akcji danej firmy w różnych dniach, oblicz maksymalny możliwy zysk z dokonania tylko jednej transakcji (kupno przed sprzedażą). Nie można sprzedawać akcji przed ich kupieniem.
#Cel: Znajdź maksymalny zysk możliwy do osiągnięcia z jednej transakcji.

#v1 O(n^2)
ceny=[43,46,51,50,40,43,70]
roznice=[]

for j in range(1,len(ceny)):
    for i in range(0,len(ceny)):
        if j>i:
            roznice.append([ceny[j]-ceny[i],ceny[i],ceny[j]])

x=max(roznice)
print(x)

#v2 O(n)

def maxprofit(ceny):
    min_price=float('inf')
    max_profit=0
    for cena in ceny:
        min_price=min(min_price,cena)
        profit=cena-min_price
        max_profit=max(max_profit,profit)
    return max_profit

ceny=[43,46,51,50,40,43,70]
print(maxprofit(ceny))

#Kupno i Sprzedaż Akcji - Dowolna Ilość Transakcji:
#Problem: Podobnie jak wyżej, ale tym razem możesz dokonać dowolnej liczby transakcji, czyli kupić i sprzedać akcje wielokrotnie. Nadal nie można sprzedawać akcji przed ich kupieniem, a po każdej sprzedaży możesz ponownie kupić akcje.
#Cel: Maksymalizacja zysku z wielokrotnych transakcji.

#v1 O(n^2)

ceny=[43,46,51,50,40,43,70]
roznice=[]

for j in range(1,len(ceny)):
    for i in range(0,len(ceny)):
        if j>i:
            roznice.append([ceny[j]-ceny[i],ceny[i],ceny[j]])

total=[]
for elem in roznice:
    total.append(elem[0])

suma=0
for elem in total:
    if elem>0:
        suma+=elem

print(suma)

#v2 O(n)

def maxprofit2(ceny):
    max_profit=0
    for i in range(1,len(ceny)):
        if ceny[i]>ceny[i-1]:
            max_profit+=ceny[i]-ceny[i-1]
            #print(ceny[i]-ceny[i-1])
    return max_profit

ceny=[43,46,51,50,40,43,70]
print(maxprofit2(ceny))

#Kupno i Sprzedaż Akcji z Ograniczeniem Cooldown:
#Problem: Teraz, po sprzedaży akcji, nie możesz dokonać kolejnego zakupu na następny dzień (istnieje jednodniowy "cooldown").
#Cel: Maksymalizuj zysk, uwzględniając ograniczenie cooldown.

ceny=[43,46,51,50,40,43,70]
roznice=[]

for j in range(1,len(ceny)):
    for i in range(0,len(ceny)):
        if j>i and (j-i)!=1:
            roznice.append([ceny[j]-ceny[i],ceny[i],ceny[j]])

total=[]
for elem in roznice:
    total.append(elem[0])

suma=0
for elem in total:
    if elem>0:
        suma+=elem

print(suma)

#Maksymalny Zysk z Transakcji z Ograniczoną Liczbą Transakcji:
#Problem: Mając do dyspozycji tablicę cen akcji, oraz ograniczoną liczbę transakcji (np. 2 kupna i 2 sprzedaże), oblicz maksymalny zysk, jaki możesz osiągnąć.
#Cel: Znajdź maksymalny zysk przy założeniu ograniczonej liczby transakcji.

ceny=[43,46,51,50,40,43,70]
roznice=[]

for j in range(1,len(ceny)):
    for i in range(0,len(ceny)):
        if j>i:
            roznice.append([ceny[j]-ceny[i],ceny[i],ceny[j]])

x=sorted(roznice)
print(x[-1],x[-2])

#NEW

def minmax(price):
    if len(price) < 2:
        return None, None
        
    min_price = price[0]
    max_profit = price[1] - price[0]
    
    for pr in price[1:]:
        max_profit = max(max_profit, pr - min_price)
        min_price = min(min_price, pr)
    
    return min_price, min_price + max_profit
    
    

def maxprofit(price):
    if len(price) < 2:
        return 0
        
    max_profit = 0
    for i in range(1, len(price)):
        if price[i] > price[i - 1]:
            max_profit += price[i] - price[i-1]

    return max_profit

prices = [7,1,5,3,6,4]
profit = maxprofit(prices)
min_price, max_profit = minmax(prices)
print(profit)
print(min_price)
print(max_profit)
