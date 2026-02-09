
class Solution:
    def findMin(self, nums: List[int]) -> int:
        myarrlen = len(nums)
        flag = 0
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        
        low = 0
        high = len(nums)-1

        while (low<high):
            if nums[low]<nums[high]:
                return nums[low]
            midpoint = (low+ (high))//2
            if nums[midpoint]>nums[midpoint+1]:
                return nums[midpoint+1]
            if nums[low]<nums[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if not nums:
#             return -1
#         if len(nums) == 1:
#             return nums[0]

#         low, high = 0, len(nums) - 1

#         while low < high:
#             if nums[low] < nums[high]:
#                 return nums[low]

#             mid = (low + high) // 2

#             if nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]

#             if nums[low] <= nums[mid]:
#                 low = mid + 1
#             else:
#                 high = mid

#         return nums[low]
