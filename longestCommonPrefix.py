import numpy as np

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lens = [len(item) for item in strs]
        
        min_len = strs[np.argmin(lens)]
        lcp = min_len
        i = 0
        print(min_len)
        while i < len(strs):
            word = strs[i]
            
            if not word.startswith(lcp):
                lcp = lcp[0:-1]
                i = 0
                continue
            i = i  + 1
        # print(lcp)
        return lcp
