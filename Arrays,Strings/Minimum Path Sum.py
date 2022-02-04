def minPathSum(grid):
    row,col= len(grid),len(grid[0])
    '''for r in range(1,row):
        grid[r][0]+=grid[r-1][0]
    for c in range(1,col):
        grid[0][c]+=grid[0][c-1]'''

    for i in range(row):
        for j in range(col):
            if (i>0 and j>0):
                grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
            elif(i>0):
                grid[i][0] += grid[i - 1][0]
            elif (j>0):
                grid[0][j] += grid[0][j - 1]

    return (grid[-1][-1])


grid= [[1,2,3],[4,5,6]]
print (minPathSum(grid))