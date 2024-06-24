# https://leetcode.com/problems/palindrome-linked-list/solutions/5218753/python-two-methods-using-stack-space-o-n-vs-middle-point-space-o-1/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        newCur = head
        while newCur:
            if newCur.val != stack.pop():
                return False
            newCur = newCur.next
        return True
        