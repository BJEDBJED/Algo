#Knapsack from the bottom

#max profit

def ks(W,waga,profit,n):
    matrix=[[0]*(W+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for W in range(1,W+1):
            if waga[i-1]<=W:
                matrix[i][W]=max(matrix[i-1][W],matrix[i-1][W-waga[i-1]]+profit[i-1])
            else:
                matrix[i][W]=matrix[i-1][W]

    print(matrix[n][W])

profit=[60,100,120,50,20]
waga=[2,40,30,20,10]
W=50
n=len(profit)

print(ks(W,waga,profit,n))

#used objects // from bottom

def ks(W,waga,profit,n):
    matrix=[[0]*(W+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for W in range(1,W+1):
            if waga[i-1]<=W:
                matrix[i][W]=max(matrix[i-1][W],matrix[i-1][W-waga[i-1]]+profit[i-1])
            else:
                matrix[i][W]=matrix[i-1][W]
    
    max_v=matrix[n][W]
    
    wynik=[]
    for i in range(n,0,-1):
        if matrix[i][W] != matrix[i-1][W]:
            wynik.append(profit[i-1])
            W-=waga[i-1]

    print(wynik,max_v)

profit=[60,100,120,50,20]
waga=[2,40,30,20,10]
W=50
n=len(profit)

print(ks(W,waga,profit,n))

#knapsack from the top

def ks2(W,waga,profit,n):
    
    if n==0 or W==0:
        return 0

    if memo[n][W] !=-1:
        return memo[n][W]

    if W >= waga[n-1]:
        memo[n][W]=max(profit[n-1]+ks2(W-waga[n-1],waga,profit,n-1), ks2(W,waga,profit,n-1))
        return memo[n][W]
    elif W<waga[n-1]:
        memo[n][W]=ks2(W,waga,profit,n-1)
        return memo[n][W]

profit=[60,100,120,50,20]
waga=[2,40,30,20,10]
W=50
n=len(profit)

memo=[[-1 for i in range(W+1)] for j in range(n+1)]
print(ks2(W,waga,profit,n))