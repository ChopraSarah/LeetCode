class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        leastSeq = 0
        # if len(nums)<1:
        #     return 0
        for j in numset:
            if j-1 not in numset:
                interimL = 1
                next = j + 1
                while next in numset:
                    interimL+=1
                    next+=1
                leastSeq = max(interimL,leastSeq)
            #print(leastSeq)


        return leastSeq
