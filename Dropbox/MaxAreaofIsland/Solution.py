class Solution:
    def recurCal(self, j,k,grid) -> int:
        if j < 0 or j >= len(grid) or k < 0 or k >= len(grid[0]) or grid[j][k] == 0:
            return 0 
        else:
            grid[j][k] = 0
            return 1 + self.recurCal(j-1, k, grid) + self.recurCal(j+1, k, grid) + self.recurCal(j, k-1, grid) + self.recurCal(j, k+1, grid)

        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSix = 0
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[j][k] == 1:
                    maxSix = max(maxSix,self.recurCal(j,k,grid))
        return maxSix



        
