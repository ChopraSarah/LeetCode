"""There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


so, in square matrix 5X5,
Start from first row, last row and check going inwards who all can reach the ocean. then do same for last column and first column"""


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pcf,atl = set(),set()
        
        def dfs(r,c,visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r == row or c == col or 
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        for c in range(col):
            dfs(0, c, pcf, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])
        
        for r in range(row):
            dfs(r, 0, pcf, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])
        res = []
        for i in range(row):
            for j in range(col):
                if(i,j) in pcf and (i,j) in atl:
                    res.append([i,j])
        return res


        

        
