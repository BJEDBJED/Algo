#LCS
#Najdluzszy wspolny podciag dwoch ciagow

#ver1
def LCS(ciag1,ciag2):
    podciag=[]
    for x in ciag1:
        if x in ciag2:
            podciag.append(x)
    return podciag

ciag1=[213,123,123,12,321,3,213,123213,123,12,3123]
ciag2=[12,3,124,13,123,444,423,4,234]
print(LCS(ciag1,ciag2))

#ver 2
def LCS2(x,y):
    a=len(x)
    b=len(y)
    matrix=[[0 for _ in range(b+1)] for _ in range(a+1)]

    for i in range(1,a+1):
        for j in range(1,b+1):
            if x[i-1] == y[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]

ciag1="cokolwiek kurde"
ciag2="wiek"
print(LCS2(ciag1,ciag2))