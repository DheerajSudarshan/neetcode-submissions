class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        res = nums[0]
        
        while l <= r:
            # OPTIMIZATION/FIX: If the current sub-array is strictly sorted, 
            # the leftmost element is guaranteed to be the smallest.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            m = (l + r) // 2
            res = min(res, nums[m])
            
            # If the left half is sorted, the pivot (min) must be in the right half
            if nums[m] >= nums[l]:
                l = m + 1 
            # Otherwise, the pivot (min) must be in the left half
            else:
                r = m - 1
                
        return res