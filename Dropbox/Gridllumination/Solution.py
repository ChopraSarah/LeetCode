"""
There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 if the lamp was not.

 

Example 1:


Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.

The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

Example 2:

Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
Output: [1,1]
Example 3:

Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
Output: [1,1,0]"""


class Solution:
    
    
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lit = []
        #ans =[]
        dict1 = defaultdict(list)
        #dict1[1,2].add(8)
        #print("hey",dict1)
        ans = [0] * len(queries)
        #matrix = []
        for _ in range(5):
            lit.append([0] * 5)
        #lit.append([0] * 5)
        for j in range(0,len(lamps)):
            #print("me",lamps[j])
            r = lamps[j][0]
            c = lamps[j][1]
            rows = n
            cols = n
            for i in range(-min(r, c), min(rows - r, cols - c)):
                #lit[r + i][c + i] = 1
                if (r + i,c + i) in dict1 and lamps[j] not in dict1[r + i,c + i]:
                    dict1[r + i,c + i].append(lamps[j])
                elif (r + i,c + i) not in dict1:
                    dict1[r + i,c + i].append(lamps[j])

                #dict1[(r + i, c + i)].add(lamps[j])
    

                #dict1[[r + i][c + i]] = 
            for i in range(-min(r, cols - c - 1), min(rows - r, c + 1)):
                #lit[r + i][c - i] = 1
                if (r+i,c-i) in dict1 and lamps[j] not in dict1[r + i,c - i]:
                    dict1[r + i,c - i].append(lamps[j])
                elif (r+i,c-i) not in dict1:
                    dict1[r + i,c - i].append(lamps[j])
                #dict1[[r + i][c - i]] = lamps[j]
            for l in lamps[j]:
                #print(l)
                for p in range(0,n):
                    #lit[l][p] =  1
                    #print((0,0) in dict1.keys())
                    if (l,p) in dict1.keys() and lamps[j] not in dict1[l,p]:
                        #print(dict1)
                        dict1[l,p].append(lamps[j])
                    elif (l,p) not in dict1 :
                        dict1[l,p].append(lamps[j])

                    #dict1[[l][p]] = lamps[j]

                # for p in range(0,n):
                #     lit[p][l] =  1
                #     if (p,l) not in dict1 and lamps[j] not in dict1[p,l]:
                #         dict1[p,l].append(lamps[j])
                #     elif (p,l) in dict1:
                #         dict1[p,l].append(lamps[j])
                    #dict1[[p][l]] = lamps[j]
        e = 0
        #print(lit)
        #print(dict1)
        #pprint(dict1)
        # for key, value in dict1.items():
        #     print(f"{key}: {value}")
        #print(json.dumps(dict1, indent=4))
        for k in queries:
            #print(k[0])
            if (k[0],k[1]) in dict1 and dict1[k[0],k[1]] !=[]:
                ans[e] = 1
                e = e + 1
                rangeRow1 = k[0]-1
                rangeRow2 = k[0]+1
                rangeCol1 = k[1]-1
                rangeCol2 = k[1]+1
                for i in range(rangeRow1,rangeRow2+1):
                    for j in range(rangeCol1,rangeCol2+1):
                        if i>=0 and i<n:
                            if j>=0 and j<n and [i,j] in dict1[k[0],k[1]]:
                                #dict1[i,j].values
                                dict1[k[0],k[1]].remove([i,j])
                                for val_list in dict1.values():
                                    val_list[:] = [pair for pair in val_list if pair != (i, j)]
            else:
                ans[e] = 0 
                e = e + 1



        # for k in queries:
        #     print(k)
        #     if lit[k[0]][k[1]] == 1:
        #         ans[e] = 1
        #         lit[k[0]][k[1]] = 0
        #         rangeRow1 = k[0]-1
        #         rangeRow2 = k[0]+1
        #         rangeCol1 = k[1]-1
        #         rangeCol2 = k[1]+1
        #         e = e + 1
        #         for i in range(rangeRow1,rangeRow2+1):
        #             for j in range(rangeCol1,rangeCol2+1):
        #                 if i>=0 and i<n:
        #                     if j>=0 and j<n:
        #                         lit[i][j] = lit[i][j] - 1
        #     else:
        #         ans[e] = 0
        #         e = e + 1


        
        return(ans)
                    
                    





        


        return [1,2,3]
        
