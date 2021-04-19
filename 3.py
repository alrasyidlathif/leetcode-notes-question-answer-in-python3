'''
Given a string s, find the length of the longest 
substring without repeating characters.
Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        leng = []
        
        while True:
            temp = []
            count = 0
            temp_s = ""
            
            for i in range(len(s)):
                temp_s = temp_s + s[i]
                if s[i] in temp:
                    leng.append(count)
                    s = s[s.index(s[i])+1:]
                    break
                else:
                    count += 1
                temp.append(s[i])
               
            if temp_s == s:
                leng.append(count)
                break                
        
        if len(leng) == 0:
            return 0
        return max(leng)
