class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #my_set = set()
        return len(nums) != len(set(nums))
        #flag = False
        #for k in nums:
            
            #if k not in my_set:
                #my_set.add(k)
            #else:
            #flag = True
        #return flag
        
        
