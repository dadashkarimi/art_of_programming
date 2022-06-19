import numpy as np
def mergeSort(array):
    if len(array)==1:
        return array
    if len(array) == 2:
        return [np.min(array), np.max(array)]
        
    mid = len(array)//2
    L = array[:mid]
    R = array[mid:]
    
    l1 = mergeSort(L)
    l2 = mergeSort(R)
    
    i = 0 
    j = 0 
    a = []
    
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            a.append(l1[i])
            i = i+1
        else:
            a.append(l2[j])
            j = j +1
            
    if i<len(l1):
        a = a+l1[i:]
        
    if j<len(l2):
        a=a+l2[j:]
        
    return a

class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1 + nums2
        b = mergeSort(a)
        
        mid = len(b)//2
        if len(b) % 2 ==0:
            z = b[mid-1]+b[mid]
            return (b[mid-1]+b[mid])/2.0
        else:
            return b[mid]
        
        

            
        
