class Solution:
    def isValid(self, s: str) -> bool:
        validPairs = {
            "}" : "{" ,
            "]" : "[" ,
            ")" : "("
        }

        stack =[]

        for i in list(s):
            if i in validPairs.values() :
                stack.append(i)
            elif stack and stack[-1] == validPairs[i]  :
                stack.pop()
            else:
                return False
        
        return not stack