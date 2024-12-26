"""Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise."""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val = True 

        hashMapStruct = {}

        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            val = False
        else:
            for i in range(0,lenS):
                #print(s[i])
                if (hashMapStruct.get(s[i]) is None):
                    hashMapStruct[s[i]] = 1
                else:
                    hashMapStruct[s[i]] = hashMapStruct[s[i]] + 1
            for j in range(0,lenS):
                #print(hashMapStruct.get(t[j]))
                if(hashMapStruct.get(t[j]) is None or hashMapStruct.get(t[j])<1):
                    val = False
                    return val
                else:
                    hashMapStruct[t[j]] = hashMapStruct[t[j]] - 1
        return val
