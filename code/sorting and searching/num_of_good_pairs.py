# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        tp = 0

        for key in count:
            tp = tp + (count[key] * (count[key] - 1)) // 2
        
        return tp