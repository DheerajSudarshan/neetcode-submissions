class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        
        temp=1
        for i in range(len(nums)):
            res[i]=temp
            temp*=nums[i]
        temp=1
        for j in range(len(nums)-1,-1,-1):
            res[j] *=temp
            temp *= nums[j]
        return res