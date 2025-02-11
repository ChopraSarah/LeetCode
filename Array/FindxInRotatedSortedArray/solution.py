class Solution:
    def findMin(self, nums: List[int]) -> int:
        myarrlen = len(nums)
        flag = 0
        for j in range(0,myarrlen - 1):
            if nums[j] > nums[j+1]:
                flag = j + 1
        return(nums[flag])
            
        
