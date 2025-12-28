
"""
This is reverse fiboncci
you are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
explain


target = 5 


0 ---- 1----2----3----4----5

ways to get to 5 from 5 = 1 (say it as constant) \  1
ways to get to 5 from 4 = 1 \. 1,1

ways to get to 5 from 3 = whatever is in 4 and 5 add them = 2 \  2,1,1
ways to get to 5 from 2. = whatever is in 3 and 4 = 2+1 = 3
--"""
class Solution:
    def climbStairs(self, n: int) -> int:
        second = 1
        first = 1
        for i in range(0,n):
            temp = first
            
            first = first + second
            second = temp
            #print(i)
        return(second)


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two =1,1
#         i = 1
#         while(i<n):
#             temp = one
#             one = two
#             two = temp + two
#             i = i + 1
        
#         return(two)
