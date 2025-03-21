
"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0."""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        for i in range(0,len(nums)):
           # print(i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i +1
            right = len(nums) - 1         
            #if i<len(nums) - 1 and nums[i] == nums[i+1] :
                #continue


            while left<right:
                target = 0
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left = left +1
                    while nums[left] == nums[left - 1] and left < right:
                        left = left +1
                if target>0:
                    right = right -1
                if target<0:
                    left = left + 1

        return(res)

          


    



