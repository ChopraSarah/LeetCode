class MedianFinder:
    right_heap =[]
    left_heap=[]

    def __init__(self):

        self.left_heap =[]
        self.right_heap = [] 
        

    def addNum(self, num: int) -> None:
        heappush(self.right_heap,-num)
        var = -heappop(self.right_heap)
        heappush(self.left_heap,var)

        if len(self.left_heap)>len(self.right_heap):
            var = heappop(self.left_heap)
            heappush(self.right_heap,-var)
        

    def findMedian(self) -> float:

        if len(self.right_heap) != len(self.left_heap):
            return -self.right_heap[0]
        else:
            return (-self.right_heap[0] + self.left_heap[0]) / 2.0
  
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
