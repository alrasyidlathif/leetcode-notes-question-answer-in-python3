'''
Given two sorted arrays nums1 and nums2 of size m and n 
respectively, return the median of the two sorted arrays.
Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        join_list = nums1
        for i in nums2:
            join_list.append(i)
            
        join_list.sort()
        n = len(join_list)
        genap = True
        if (n%2==1):
            genap = False
            
        if genap:
            return (join_list[int(n/2)-1] + join_list[int(n/2)+1-1]) / 2
        else:
            return join_list[int((n+1)/2)-1]