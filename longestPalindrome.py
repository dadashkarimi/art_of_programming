import numpy as np
def longestPalindrome(s):
    # print(len(s))
    if s ==None or len(s) < 1:
        return ""
    
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        len_ = max(len1, len2)
        if (len_ > end - start):
            start = i - (len_ - 1) / 2;
            end = i + len_ / 2;
        
    
    return s[start:end + 1];


def expandAroundCenter(s, left, right):
    L = left
    R = right
    
    while (L >= 0 and R < len(s) and (s[L] == s[R])):
        L = L -1
        R = R + 1
    
    return R - L - 1

def allCharactersSame(s) :
    n = len(s)
    for i in range(1, n) :
        if s[i] != s[0] :
            return False
    return True

def getAllSubstrings(s):
    
    a = []
    checked = set()

    if len(s)==1:
        
        return [s]
    
    if isPalindromic(s):
        return [s]

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):

            if len(s[i:j]) in checked:
                continue
                
            if len(checked)>0:
                if len(s[i:j])<max(checked):
                    continue

                            
            if isPalindromic(s[i:j]) and s[i:j] not in a:
                a.append(s[i:j])
                checked.add(len(s[i:j]))
                
    return a


def isPalindromic(s):
    if allCharactersSame(s):
        return True
    
    if len(s)==1:
        return True
    
    mid = len(s)/2.0
    i = 0 
    
    while(s[i]==s[len(s)-i-1]):
        if i >= mid:
            return True
        i = i + 1
    return False

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        b = getAllSubstrings(s)
        c = [len(x) for x in b]
        return b[np.argmax(c)]
