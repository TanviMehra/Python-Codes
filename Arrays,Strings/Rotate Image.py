#using extra space
def transpose(matrix):
    row=len(matrix)
    col=len(matrix[0])
    trans=[[matrix[j][i] for j in range(row)] for i in range(col)]

    for val in trans:
        val.reverse()
    return trans

#without using extra space
def inplaceTranspose(matrix):
    n=len(matrix[0])
    for i in range(n):
        for j in range(i,n):
            matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
    for val in matrix:
        val.reverse()
    return matrix



matrix=[]
n=int(input())
for val in range(n):
    value=list(map(int,input().split()))
    matrix.append(value)
print (transpose(matrix))
print (inplaceTranspose(matrix))