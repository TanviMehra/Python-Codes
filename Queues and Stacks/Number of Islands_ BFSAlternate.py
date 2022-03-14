from collections import deque
def IslandNumber(grid):
    row,col= len(grid),len(grid[0])
    count=0
    global visited
    visited= set()
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1' and (i,j) not in visited:
                count+=1
                BFS(i,j,grid)
    return count
def BFS(i,j,grid):
    queue=deque()
    queue.append((i,j))
    while queue:
        size=len(queue)
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(size):
            x,y=queue.popleft()
            #visited.add((i,j))
            for dir in directions:
                current_x= x+dir[0]
                current_y= y+dir[1]
                if (current_x<0 or current_x>len(grid)-1 or current_y<0 or current_y>len(grid[0])-1 or grid[current_x][current_y]!='1'or (current_x,current_y) in visited):
                    continue
                queue.append((current_x,current_y))
                visited.add((current_x,current_y))
                #grid[current_x][current_y]='0'




grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print (IslandNumber(grid))