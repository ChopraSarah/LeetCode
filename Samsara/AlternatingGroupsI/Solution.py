/*

There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [1,1,1]

Output: 0

Explanation:



Example 2:

Input: colors = [0,1,0,0,1]

Output: 3

Explanation:



Alternating groups:



 

Constraints:

3 <= colors.length <= 100
0 <= colors[i] <= 1

*/



class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        j = 1
        count = 0
        totLen = len(colors)

        while j <= totLen:
            print(j)
            back = j - 1
            current = j
            
            if j == totLen - 1:
                front = 0
            else:
                front = j + 1
            if j == totLen:
                back = j-1
                current = 0
                front = 1


            if colors[back] != colors[current] != colors[front]:
                count = count + 1
                print(count,j)

            j = j + 1
        
        return(count)
