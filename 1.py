'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if i != nums.index(target-nums[i]):
                    return [i, nums.index(target-nums[i])]
    
    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if (nums[i] not in dic):
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)

        for i in range(len(nums)):
            num = target - nums[i]
            if (num in nums[i+1:]):
                if (dic[nums[i]] != dic[num]):
                    return [dic[nums[i]][0], dic[num][0]]
                else:
                    return [dic[nums[i]][0], dic[num][1]]
