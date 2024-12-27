"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""

import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        i = 1
        k = 0 
        #print(len(nums))
        arra = [1] * (len(nums))
        #print(len(arra))
        j = len(nums) - 2
        while i < len(nums):
            print("i",nums[i])
            left = left * nums[i-1]
            right = right * nums[j+1]
            arra[i] = arra[i]*left
            arra[j] = arra[j]*right
            #print(nums[j])
            i = i + 1
            
            j = j -1
        #print(arra)
        return arra

