
# Time compxity (O(mn)
class Solution:

    def numDistinctIslands(self, grid):

        rows=len(grid)
        cols=len(grid[0])
        self.unique_islands=set()
        self.visited=set()
        for row in range(rows):
            for col in range(cols):
                self.current_island = ''
                self.row_origin=row
                self.col_origin=col
                if grid[row][col]=='1' and (row,col) not in self.visited:
                    self.dfs(row,col,grid,'X')
                    if self.current_island:

                        self.unique_islands.add(self.current_island)
        print(self.unique_islands)
        return len(self.unique_islands)


    def dfs(self,row, col, grid,direction):
        if (row<0 or col<0 or row>len(grid)-1 or col > len(grid[0])-1or grid[row][col]!=1 or (row,col) in self.visited):
            return
        self.visited.add((row,col))
        self.current_island+=(direction)
        self.dfs(row-1,col,grid,'U')
        self.dfs(row+1,col,grid,'D')
        self.dfs(row,col-1,grid,'L')
        self.dfs(row,col+1,grid,'R')
        self.current_island+=('X')

grid= [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,0,1,1],
  [0,0,0,1,1]
]
obj=Solution()
print (obj.numDistinctIslands(grid))