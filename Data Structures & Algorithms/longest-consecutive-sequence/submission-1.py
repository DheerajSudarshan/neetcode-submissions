class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 0
        for i in numSet:
            add=1
            if i-1 not in numSet:
                while i+add in numSet:
                    add+=1
            longest = max(add,longest)
        return longest