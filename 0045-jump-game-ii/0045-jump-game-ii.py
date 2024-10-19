class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest=0
        end,far=0,0
        n=len(nums)
        for i in range(n-1):
            far=max(far,nums[i]+i)

            if i==end:
                end=far
                smallest+=1
        
        return smallest