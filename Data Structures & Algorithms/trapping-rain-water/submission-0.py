class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        area = 0
        while right > left :
            if maxLeft > maxRight:
                right-=1
                maxRight = max(height[right],maxRight)
                area += maxRight - height[right]
            else:
                left+=1
                maxLeft = max(height[left],maxLeft)
                area += maxLeft - height[left]
        return area
            

