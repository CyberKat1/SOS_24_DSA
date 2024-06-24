# https://leetcode.com/problems/remove-element/solutions/3670940/best-100-c-java-python-beginner-friendly/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index