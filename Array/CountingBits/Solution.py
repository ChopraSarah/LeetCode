from array import array
class Solution:
    def countBits(self, n: int) -> List[int]:
        arrt = array('h')  
        for x in range(n+1):  
            bin_a = bin(x)
            arrt.append(bin_a.count('1'))
            print(bin_a.count('1'))
        return arrt
