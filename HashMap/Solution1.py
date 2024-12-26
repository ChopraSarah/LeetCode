#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictAsHash = {}
        for i, num in enumerate(nums):
            #print(i,num)

            neednum = target - num
            if neednum in dictAsHash:
                return [i,dictAsHash[neednum]]
            dictAsHash[num] = i
            print("me",dictAsHash)
        #print("me",dictAsHash)
