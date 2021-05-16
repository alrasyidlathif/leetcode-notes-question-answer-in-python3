'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        star = False
        dot = False
        
        if ("*" in p):
            star = True
        if ("." in p):
            dot = True
            
        if ((not star) and (not dot)):
            print("check star and dot")
            if (s==p):
                return True
            else:
                return False
            
        if (len(p) == 2):
            # p == .* or *.
            if (star and dot):
                return True
            if (len(p)<len(s)):
                return False
            
        if (".*" in p):
            dot_star = p.split(".*")
            if (dot_star[0]==""):
                p = p[2:]
                # if (".*" == p[0:2]):
                for i,j in enumerate(s):
                    if (j!=s[0]):
                        s = s[i:]
                        break
                # if (".*" == p[len(p)-2:len(p)]):
                #     for i,j in enumerate(p):
                #         if (j!=p[0:2]):
                #             p = p[i:]
                #             break
        
        p_list = p.split("*")
        if (p_list[0]==""):
            del p_list[0]
        if (p_list[len(p_list)-1]==""):
            del p_list[len(p_list)-1]
            
        if (len(p_list) == 1):
            if (p_list[0] in s):
                return True
            elif ("." in p):
                if (len(s)==1):
                    return True
                else:
                    dot_idx = p_list[0].index(".")
                    new_p = []
                    for pl in p_list[0]:
                        new_p.append(pl)
                    new_p[dot_idx] = s[dot_idx]
                    p_list[0] = "".join(new_p)
                    if (p_list[0]==s):
                        return True
                    return False
            elif ("*" not in p):
                return False
            
        # print(p_list)
        # print(s)
        
        idx = 0
        for index,i in enumerate(p_list):
            
            # if (idx==len(s)):
            #     break
            
            if (i == s[idx:idx+len(i)]):
                idx+=len(i)
                
                if (index==len(p_list)-1):
                    continue
                    
                while True:
                    if (idx == len(s)-1):
                        break
                    if(i[len(i)-1] == s[idx:idx+1]):
                        idx+=1
                    else:
                        break
            
            elif (len(i)>1 and i[0:len(i)-1]==s[idx:idx+len(i)-1]):
                idx+=len(i)-1
            elif (i == "."):
                idx+=len(i)
            elif (idx==0 and len(i)==1):
                continue
            else:
                if (index < len(p_list)-1):
                    continue
                if (idx==len(s)): # last s sudah dicompare
                    if (p_list[index] == p_list[index-1]):
                        return True
                    return False
                if (i==s[idx]):
                    return True
                return False
        
        if (idx==len(s)):
            return True
        return False
    