'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''



class Solution:
    def isValid(self, s: str) -> bool:
        mys = []
        
        if len(s)==1:
            return False

        for l in s:
            if l =='(' or  l =='{' or  l =='[':
                mys.append(l)
            elif l ==')' and len(mys)!=0:
                if mys.pop() =='(': 
                    continue
                else:
                    return False
            elif l =='}' and len(mys)!=0:
                if mys.pop() == '{': 
                    continue
                else:
                    return False
            elif l ==']' and len(mys)!=0:
                if mys.pop() == '[': 
                    continue
                else:
                    return False
            else:
                return False
        if len(mys)!=0:
            return False
        return True
                
                


        
        
        
