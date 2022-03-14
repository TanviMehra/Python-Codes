
# Time compxity (O(mn)
class Solution:

    def numDistinctIslands(self, grid):

        def dfs(row, col, grid, direction):
            if (row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] != 1 or (
            row, col) in visited):
                return

            visited.add((row, col))
            current_island.append(direction)
            dfs(row - 1, col, grid, 'U')
            dfs(row + 1, col, grid, 'D')
            dfs(row, col - 1, grid, 'L')
            dfs(row, col + 1, grid, 'R')
            current_island.append(direction)

        rows=len(grid)
        cols=len(grid[0])
        unique_islands=set()
        visited=set()
        for row in range(rows):
            for col in range(cols):
                current_island = []
                if grid[row][col]==1 and (row,col) not in visited:
                    dfs(row,col,grid,'X')
                    if current_island:
                        unique_islands.add(tuple(current_island))
        print(unique_islands)
        return len(unique_islands)




grid= [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,0,1,1],
  [1,0,1,1,1]
]
obj=Solution()
print (obj.numDistinctIslands(grid))
