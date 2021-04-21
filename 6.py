'''
The string "PAYPALISHIRING" is written in a zigzag pattern 
on a given number of rows like this: (you may want to display 
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this 
conversion given a number of rows:
string convert(string s, int numRows);

Example:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res_dict = {}
        for i in range(numRows):
            res_dict[i] = []
        
        arah = 1
        idx = 0
        for w in s:
            res_dict[idx].append(w)
            if idx == numRows-1:
                arah = -1
            if idx == 0:
                arah = 1
            if numRows == 1:
                arah = 0
            idx = idx + arah
            
        res = ""
        for i in range(numRows):
            res = res + "".join(res_dict[i])
        
        return res