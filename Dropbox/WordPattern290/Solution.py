"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    
        #print(dataset[key] ==dataset[key1] )   


        result = s.split(" ")
        #print(result)
        dict1 = defaultdict(list)
        dict2 = defaultdict(list)
        if len(result) == len(pattern):
            for i in range(0,len(result)):
                dict1[result[i]].append(i)
                dict2[pattern[i]].append(i)
            
            #print(len(dict1),len(dict2))
            for i in range(0,len(dict1)):  
                #print(dict1[list(dict1.keys())[i]])       
                if dict1[list(dict1.keys())[i]] != dict2[list(dict2.keys())[i]]:
                    return False
            return True
        else:
            return False

        

            
