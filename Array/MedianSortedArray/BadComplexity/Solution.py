class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA = len(nums1)
        lenB = len(nums2)
        
        totalLen = lenB + lenA
        emptyArr = [0] * totalLen
        medianLoc1 = 0
        medianLoc2 = 0
        if totalLen%2==0:
            medianLoc1,medianLoc2 = totalLen/2 - 1 , (totalLen/2) 
        else:
            medianLoc1,medianLoc2 = 0 , floor(totalLen/2)

        j = 0
        i = 0 
        k = 0
        #print("hey",nums1[0],emptyArr[k])
        while k<=medianLoc2 and i<len(nums1) and j<len(nums2):
            
            if nums1[i]<nums2[j]:
                #print(i,k,emptyArr[k])
                emptyArr[k] = nums1[i]
                i = i + 1
                k = k + 1
            elif nums1[i]>nums2[j]:
                emptyArr[k] = nums2[j]
                k = k + 1
                j = j + 1
        if j <len(nums2) and  k<=medianLoc2:
            while j< len(nums2) and k<=medianLoc2:
                emptyArr[k] = nums2[j]
                j = j + 1
                k = k + 1
        if i < len(nums1) and  k<=medianLoc2:
            while i< len(nums1) and k<=medianLoc2:
                emptyArr[k] = nums1[i]
                i = i + 1
                k = k + 1
            

        if totalLen%2==0:
            medianLoc1,medianLoc2 = k-1 , k-2
            return((emptyArr[k-1] + emptyArr[k-2])/2)
            #return((emptyArr[k-1] + emptyArr[k])/2)
        else:
            medianLoc1,medianLoc2 = 0 , k
            return(emptyArr[k-1])
            #return(emptyArr[k])
        
        
            



        #return(9.0) 

        
