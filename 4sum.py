import numpy as np
class Solution(object):
    def fourSum(self, nums, target):
        # For each element apply 3sum
        
        prev1 = np.Inf
        nums.sort()
        res = []
        def threeSum(val, nums, val_left):
            prev2 = np.inf
            for i, num in enumerate(nums):
                if prev2 == num:
                    continue
                prev2 = num
                val_left_rem = val_left - num
                left = i + 1
                right = len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == val_left_rem:
                        res.append([val, num, nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif nums[left] + nums[right] < val_left_rem:
                        left += 1
                    else:
                        right -= 1
                        
                    
        for i, num in enumerate(nums):
            if prev1 == num:
                continue
            prev1 = num
            # apply 3Sum
            val_left = target - num
            threeSum(num, nums[i+1:], val_left)
        return res
        
