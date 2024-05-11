#Dynamic programming

#fibo

def fibo(n,memo={}):
    if n in memo:
       return memo[n]
    if n<=2:
        return 1
    memo[n]=fibo(n-2,memo)+fibo(n-1,memo)
    return memo[n]

print(fibo(4))

#suma podciagu o najwiekszej sumie
ciag=[32,45,67,-89,987,765,-543,3221,3,2]
sumy=[]

def maxsuma(ciag):
    for i in range(len(ciag)):
        for j in range(len(ciag)-1):
            sumy.append(sum(ciag[i:j]))
    return max(sumy)

            
print(maxsuma(ciag))

#Algorytm Kadane'a

def maxsuma2(ciag):
    current_max=ciag[0]
    end_max=ciag[0]

    for x in ciag[1:]:
        end_max=max(x,end_max+x)
        current_max=max(current_max,end_max)
    return end_max

print(maxsuma2(ciag))

#LCS

def lcs(x,y):
    m,n=len(x),len(y)
    tab=[[0]*(n+1) for _ in range(m+1)]

    print(tab)

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                tab[i][j]=tab[i-1][j-1]+1
            else:
                tab[i][j]=max(tab[i-1][j],tab[i][j-1])
    return tab[m][n],tab

print("wynik to",lcs("ABCDAB","ABBADDAB"))

#Jumps table

def tab_jumps(tab):
    n=len(tab)

    if n<=1:
        return 0
    
    jumps=[float('inf')]*n
    jumps[0]=0

    for i in range(n):
        for j in range(i+1,min(i+tab[i]+1,n)):
            jumps[j]=min(jumps[j],jumps[i]+1)
    return jumps[-1]

t=tab_jumps([2, 7, 4, 6, 2, 2, 2, 0, 1, 1])
print(t)