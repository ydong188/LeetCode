'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in dic:
            return (dic[res], i)
        else:
            dic[nums[i]] = i
    return(-1,-1)

def twoSum(nums, target):
    dic = {value: key for key, value in enumerate(nums)}
    for i in range(len(nums)):
        rest = target - nums[i]
        #if rest in dic:
        if rest in dic.keys():
            print(rest)
            return sorted([dic[rest],i])