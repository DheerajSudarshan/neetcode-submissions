class Solution:
    def isValid(self, s: str) -> bool:
        a={"[","{","("}
        b={
           "]":"[",
           "}":"{",
           ")":"("
           }
        s1=[]
        if(len(s)%2==1):
            return False
        for i in s:
            if(i in a):
                s1.append(i)
            elif(len(s1)!=0 and b[i]==s1[-1]):
                s1.pop()
            else:
                return False
        if(len(s1)==0):
            return True
        else:
            return False



