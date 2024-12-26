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
