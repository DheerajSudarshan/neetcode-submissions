class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        s1=list(s)
        s2=set(x for x in range(ord('a'),ord('z')+1))
        s4=set(x for x in range(ord('0'),ord('9')+1))
        s3=[]
        for i in range(len(s1)):
            if ord(s1[i]) in s2 or ord(s1[i]) in s4:
                s3.append(s1[i])
        
        if len(s3)==0:
            return True
        
        rightPointer = len(s3) - 1
        for i in range(len(s3)//2):
            if s3[i] == s3[rightPointer - i]:
                continue
            else:
                return False
        return True
