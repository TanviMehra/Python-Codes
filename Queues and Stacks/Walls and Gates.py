from collections import deque
def wallsAndGates(rooms):
    row,col= len(rooms),len(rooms[0])
    for i in range(row):
        for j in range(col):
            if rooms[i][j]==0:
                dfs(i,j,0,rooms)
    return rooms

def dfs(i,j,count,rooms):
    if (i<0 or i>len(rooms)-1 or j<0 or j>len(rooms[0])-1 or count>rooms[i][j]):
        return
    rooms[i][j]=count
    dfs(i+1,j,count+1,rooms)
    dfs(i-1,j,count+1,rooms)
    dfs(i,j-1,count+1,rooms)
    dfs(i,j+1,count+1,rooms)

def wallsAndGatesBFS(rooms):
    row,col= len(rooms),len(rooms[0])
    queue=deque()
    for i in range(row):
        for j in range(col):
            if rooms[i][j]==0:
                queue.append((i,j))

    while queue:
        size=len(queue)
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        for i in range(size):
            x,y= queue.popleft()
            for direction in directions:
                current_x= direction[0]+x
                current_y=direction[1]+y

                if(current_x<0 or current_x>len(rooms)-1 or current_y<0 or current_y>len(rooms[0])-1 or rooms[current_x][current_y]!=2147483647):
                    continue
                rooms[current_x][current_y]=rooms[x][y]+1
                queue.append((current_x,current_y))
        return rooms

rooms= [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print (wallsAndGates(rooms))
print(wallsAndGatesBFS(rooms))
