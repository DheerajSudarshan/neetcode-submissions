class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            diff=target-n
            if diff in nums and (i!=nums.index(diff)):
                return list(set([i,nums.index(diff)]))