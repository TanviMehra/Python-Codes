#DFS solution without updating the input data and maintaining a visited.
# Alternate solution involves changing the value of 1 when it is encountered.
def numberOfIslandsDfs(grid):
    row,col=len(grid),len(grid[0])
    count=0
    global visited
    visited=set()

    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1' and (i,j) not in visited:
                count += 1
                dfs(i,j,grid)
    return count
def dfs(i,j,grid):
    if(i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!='1' or (i,j) in visited):
        return
    visited.add((i,j))
    print(visited)
    dfs(i+1,j,grid)
    dfs(i-1,j,grid)
    dfs(i,j-1,grid)
    dfs(i,j+1,grid)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print (numberOfIslandsDfs(grid))