class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        res = 0
        
        # r automatically increments by 1 each loop, starting at 0
        for r in range(len(s)):
            
            # 1. Add the new right character to the window
            counter[s[r]] = 1 + counter.get(s[r], 0)
            
            # 2. Check if the current window is invalid
            maxCount = max(counter.values())
            window_size = r - l + 1
            
            # If invalid, shrink the window from the left
            if window_size - maxCount > k:
                counter[s[l]] -= 1  # Decrement BEFORE shifting l
                l += 1
                
            # 3. The window is now guaranteed valid, so update max result
            # (Note: r - l + 1 is recalculated dynamically here)
            res = max(res, r - l + 1)
            
        return res