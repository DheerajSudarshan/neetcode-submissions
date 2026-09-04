class Solution:

    def encode(self, strs: List[str]) -> str:
        s1=""
        for i in strs:
            s1=s1+i+'~'
        print(s1)
        return s1

    def decode(self, s: str) -> List[str]:
        a=[]
        s2=""
        for i in s:
            if i == '~':
                a.append(s2)
                s2=""
                continue
            s2=s2+i
        return a