/*
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

*/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        #print(colors.extend(colors[0:k]))
        colors.extend(colors[0:k-1]) 
        #print(colors)
        total = 0 
        for j in range(len(colors)):
            #print(j)
            n=0
            while n<k-1 and j + n <len(colors)-1:
                if colors[j + n]!=colors[j + n+1]:
                    n = n + 1
                else:
                    break
                    
            
            if n == k - 1:
                #print(j,"imj")
                total = total + 1
        
        return(total)



        
        
        




        return(4)
        
