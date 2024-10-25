class Solution(object):
    def twoSum(self, nums, target):
        sum=0
        for a in range(len(nums)):
            for b in range(len(nums)):
                if a==b:
                    continue
                
                if(nums[a]+nums[b]==target):
                    return a,b