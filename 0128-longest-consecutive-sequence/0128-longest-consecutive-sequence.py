class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for num in nums:
            if num-1 not in s:
                next_num=num+1
                length=1
                while next_num in s:
                    next_num+=1
                    length+=1
                longest=max(length,longest)
        return longest