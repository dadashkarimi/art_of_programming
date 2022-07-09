from collections import defaultdict
 
def arePermutations(arr1, arr2):
    if (len(arr1) != len(arr2)):
        return False
       
    # Creates an empty hashMap hM
    hM = defaultdict (int)
 
    for i in range (len(arr1)):
         
        x = arr1[i]
        hM[x] += 1
         
    for i in range (len(arr2)):
        x = arr2[i]
 
        # If element is not present
        # in hash map or element
        # is not present less number
        # of times
        if x not in hM or hM[x] == 0:
             return False
 
        hM[x] -= 1
        
    return True



class Solution(object):
    def threeSum(self, nums):
        res=set()

        n,p,z=[],[],[]
        for item in nums:
            if item < 0:
                n.append(item)
            elif item > 0:
                p.append(item)
            else:
                z.append(item)


        nset=set(n)
        pset=set(p)

        if len(z)>=3:
            res.add((0,0,0))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target=-1*(n[i]+n[j])
                if target in pset:
                    res.add(tuple(sorted([n[i],n[j],target])))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target=-1*(p[i]+p[j])
                if target in nset:
                    res.add(tuple(sorted([p[i],p[j],target])))
        if len(z)>=1: 
            for item in pset:
                if -1*item in nset:
                    res.add((-item,0,item))
        return res

    def JThreeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum_zero  = []
        all_good = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    
                    
                    if (nums[i],nums[j],nums[k]) in all_good:
                        sum_zero.append([nums[i],nums[j],nums[k]]) 
                    elif nums[i]+nums[j]+nums[k]==0:
                        all_good[(nums[i],nums[j],nums[k])]=1
                        sum_zero.append([nums[i],nums[j],nums[k]])

        res = []
        for i in sum_zero:
            if i not in res:
                flag = False
                
                for j in res:
                    if arePermutations(i,j):
                        flag = True
                        
                if not flag:
                    res.append(i)

            
        # print(res)
        return res


