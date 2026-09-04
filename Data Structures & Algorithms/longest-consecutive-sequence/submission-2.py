class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            current = nums[i]
            if current - 1 in num_set:
                continue  
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
        return longest