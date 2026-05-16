class Solution(object):
    def maxArea(self, height):

        n = len(height)
        left=0
        right = n-1

        maxArea= 0
        while left<right:
            value = min(
                height[left],
                height[right]
            ) * (right-left)

            maxArea = max(maxArea, value)

            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        return maxArea


# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [2,3,4,5,18,17,6]
height = [1, 2, 3, 4, 5, 25, 24, 3, 4]
S = Solution()
print(S.maxArea2(height))
