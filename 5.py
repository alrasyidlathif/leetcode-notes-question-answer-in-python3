'''
Given a string s, return the longest palindromic substring in s.
Example:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        save = {}
        for t in range(len(s),1,-1):
            while True:
                exit = 0
                finish = 0
                for i in range(len(s)):
                    if i+t == len(s)+1:
                        exit = 1
                        break
                    if s[i:i+t] == s[i:i+t][::-1]:
                        save[t] = s[i:i+t]
                        finish = 1
                        break
                if exit == 1 or finish == 1:
                    break
            if finish == 1:
                break
        if len(save) == 0:
            return s[0]
        return save[max(save.keys())]
        