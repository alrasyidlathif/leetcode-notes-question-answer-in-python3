'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (str(x) == str(x)[::-1]):
            return True
        return False
