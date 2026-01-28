class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       size_nums = len(nums)
       ans = []
    
       dict1={}
       for i in range(0,size_nums):
            #print(i)
            dict1[nums[i]]=i
       
       for k in range(0,size_nums):
            print(k)
            l = target-nums[k]
            
            if l in dict1 and dict1[l]!=k:
                print("he")
                ans.append(k)
                ans.append(dict1[l])
                break
       return ans




