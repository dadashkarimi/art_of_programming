class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1=0
        p2=1
        a = set()
        b = {}
   
        if len(s)<=1:
            return len(s)
        
        for i in range(len(s)):
            b[i]=set()
            
        for i in range(len(s)):
            b[i].add(s[i])
            for j in range(i+1,len(s)):
                if s[j] in b[i]:
                    break
                
                b[i].add(s[j])
        # print(b)
        z = max([len(b[i]) for i in range(len(s))])
        # print([len(b[i]) for i in range(len(s))])
        return z
