from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        CounterS1 = Counter(s1)
        CounterS2 = {}
        l = 0

        for r in range(len(s2)):
            # 1. Add the right character to the window
            CounterS2[s2[r]] = 1 + CounterS2.get(s2[r], 0)
            
            # 2. If the window gets bigger than s1, shrink it from the left
            if (r - l + 1) > len(s1):
                CounterS2[s2[l]] -= 1
                
                # Clean up zero-counts so the dictionary comparison works perfectly
                if CounterS2[s2[l]] == 0:
                    del CounterS2[s2[l]]
                
                l += 1
                
            # 3. Check if we have a match
            if CounterS1 == CounterS2:
                return True
                
        return False