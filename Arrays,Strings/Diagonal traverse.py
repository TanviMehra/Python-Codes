def findDiagonalOrder(matrix):
    rows,cols= len(matrix),len(matrix[0])
    num_diagonals= (rows+cols)-1
    out=[]
    res= [[]*num_diagonals for i in range(num_diagonals)]

    for i in range(rows):
        for j in range(cols):
            res[i+j].append(matrix[i][j])
    out.append(res[0][0])

    for k in range(1,len(res)):
        if k%2!=0:
            out.extend(res[k])
        else:
           out.extend(res[k][::-1])
    print (out)


matrix= [
 [ 1, 2, 3,4,5],
 [ 7, 12,14,20,24],
 [ 18,30,40,50,60],
 [21,22,28,29,30]
]
findDiagonalOrder(matrix)