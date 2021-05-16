'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
1. Only the space character ' ' is considered a whitespace character.
2. Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        new_s = s
        
        c_full = ["0","1","2","3","4","5","6","7","8","9","-","+"]
        c = ["0","1","2","3","4","5","6","7","8","9"]
        c_sign = ["+","-"]
        
        # hilangkan space di depan
        for i,j in enumerate(new_s):
            if (j!=" "):
                print("space dihilangkan")
                new_s = new_s[i:]
                break
                
        s_list = new_s.split(" ")
        if (len(s_list) > 1):
            new_s1 = s_list[0]
            new_s2 = s_list[1]
            if (new_s1 in c_sign):
                new_s = new_s2
            else:
                new_s = new_s1
        else:
            new_s1 = s_list[0]
            new_s = new_s1
            
        new_s = new_s.replace(" ", "")
        
        if (len(new_s)<1):
            return 0
        
        if (new_s[0] not in c_full):
            return 0
        
        if (len(new_s)==1):
            if (s in c_sign):
                return 0
        
        if (new_s[0]=="+" and new_s[1]=="-"):
            return 0
        
        sign = ""
        
        # hilangkan sign
        if (new_s[0]=="+" or new_s[0]=="-"):
            print("sign dihilangkan")
            sign = new_s[0]
            new_s = new_s[1:]
        
        # hilangkan huruf
        for i,j in enumerate(new_s):
            if (j not in c):
                print("huruf dihilangkan")
                new_s = new_s[:i]
                break
        
        # hilangkan 0 di depan
        for i,j in enumerate(new_s):
            if (j!="0"):
                print("0 dihilangkan")
                new_s = new_s[i:]
                break
            if ((i==len(new_s)-1) and j=="0"):
                return 0
                
        if (sign=="-"):
            if (len(str(-1*2**31))<len(sign+new_s)):
                return -1*2**31
            elif ((len(str(-1*2**31))==len(sign+new_s)) and (str(-1*2**31)<=sign+new_s)):
                return -1*2**31
        else:
            if (len(str((1*2**31)-1))<len(new_s)):
                return (1*2**31)-1
            elif ((len(str((1*2**31)-1))==len(new_s)) and (str((1*2**31)-1)<=new_s)):
                return (1*2**31)-1
        
        i_map = {
            "0":0,"1":1,"2":2,
            "3":3,"4":4,"5":5,
            "6":6,"7":7,"8":8,"9":9
        }
        
        digit = len(new_s)
        res = 0
        for i,j in enumerate(range(digit-1,-1,-1)):
            res = res + ( 10**j * i_map[new_s[i]] )
            
        if (sign=="-"):
            return -1*res
        return res
    