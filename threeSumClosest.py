# https://leetcode.com/problems/3sum-closest/
import numpy as np
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # n, p, z = [],[],[]
        # for item in nums:
        #     if item > 0:
        #         p.append(item)
        #     elif item< 0:
        #         n.append(item)
        #     else:
        #         z.append(item)
        # pset = set(p)
        # nset = set(n)
        # res = 
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         target = -1*(n[i]+n[j])
        #         res.add()
        
        nums = sorted(nums)
        n = len(nums)
        mini = float('inf')
        ans = 0
        for i in range(n):
            lp = i + 1
            rp = n-1
            while lp < rp:
                ss = nums[i] + nums[lp] + nums[rp]
                if ss < target:
                    lp += 1
                else:
                    rp -= 1
                diff = abs(target-ss)
                if diff < mini:
                    mini = diff
                    ans = ss              

        return ans

#         nums = sorted(nums)
#         if target < - 3000:
#             nums = nums[:4]
#         if target > 3000:
#             nums = nums[-4:]
            
#         res = []
#         sign = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     val = nums[i]+nums[j]+nums[k]
#                     res.append(val) 
                    
#         residual = [abs(x - target) for x in res]
#         i = np.argmin(residual, axis=None, out=None)
#         return res[i]
