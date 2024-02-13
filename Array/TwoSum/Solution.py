class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenNums = len(nums)
        firstVal = -1
        secondVal = -1
        for i in range(lenNums):
            #print(nums[i])
                firstVal = i
                #print(firstVal)
                valSearch = target-nums[i]
                #print("val",valSearch)
            #for()
                for j in range(lenNums):
                    if(valSearch == nums[j] and j!=i):
                        #secondVal = j
                        return(firstVal,j)
                    

        #if(secondVal!=-1):
            #print(firstVal,secondVal)
            #listA = [firstVal,secondVal]
            #return(listA)
        
