# so consider issue -2,3,-4

# cant be linear, as we want to maintain min -2*3 because -6*-4 gives the best result and correct result 


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        maxP=nums[0]
        i=1
        tot=1
        currentP=nums[0]
        currentM=nums[0]
        while i<len(nums):

            temp =currentM

            currentM = min(nums[i], currentM*nums[i],currentP*nums[i])
            currentP = max(nums[i], currentP*nums[i],temp*nums[i])
            #currentP= temp
            
            if currentP>maxP:
                maxP=currentP
                i=i+1
            
            else:
                i=i+1
            
        return maxP
        
        
