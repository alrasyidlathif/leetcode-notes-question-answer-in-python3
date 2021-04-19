'''
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two 
numbers and return the sum as a linked list.
You may assume the two numbers do not contain any 
leading zero, except the number 0 itself.
Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        save = 0
        res_list = []
        
        while True:
            if (l1 == None) and (l2 == None):
                if save != 0:
                    res_list.append(save)
                break
            
            l1_val = 0
            try:
                l1_val = l1.val
            except:
                print('0k')
                
            l2_val = 0
            try:
                l2_val = l2.val
            except:
                print('ok')
            
            sum = l1_val+l2_val+save
            
            save = 0
            if sum>=10:
                save=1
                sum=sum-10
                
            try:
                l1 = l1.next
            except:
                print('ok')
                
            try:
                l2 = l2.next
            except:
                print('ok')
            
            res_list.append(sum)
        
        for i in range(len(res_list)):
            val = res_list.pop()
            if i != 0:
                res = ListNode(val, res)
            else:
                res = ListNode(val)
        
        return res