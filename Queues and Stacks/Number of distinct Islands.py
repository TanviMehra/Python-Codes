
# Time compxity (O(n**2.M**2)- we can do better
class Solution:

    def inUniqueIsland(self,current_island):
        for island in self.unique_islands:
            if len(island)!=len(current_island):
                continue
            for cell1,cell2 in zip(island,current_island):
                if cell1!=cell2:
                    break
            else:
                return False
        return True

    def numDistinctIslands(self, grid):

        rows=len(grid)
        cols=len(grid[0])
        self.unique_islands=[]
        self.visited=set()
        for row in range(rows):
            for col in range(cols):
                self.current_island = []
                self.row_origin=row
                self.col_origin=col
                if grid[row][col]=='1' and (row,col) not in self.visited:
                    self.dfs(row,col,grid)
                    if not self.current_island or not self.inUniqueIsland(self.current_island):
                        continue
                    self.unique_islands.append(self.current_island)
        print(self.unique_islands)
        return len(self.unique_islands)


    def dfs(self,row, col, grid):
        if (row<0 or col<0 or row>len(grid)-1 or col > len(grid[0])-1or grid[row][col]!='1' or (row,col) in self.visited):
            return
        self.visited.add((row,col))
        self.current_island.append((row-self.row_origin,col-self.col_origin))
        self.dfs(row-1,col,grid)
        self.dfs(row+1,col,grid)
        self.dfs(row,col-1,grid)
        self.dfs(row,col+1,grid)

grid= [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","1"],
  ["0","0","1","1","1"]
]
obj=Solution()
print (obj.numDistinctIslands(grid))