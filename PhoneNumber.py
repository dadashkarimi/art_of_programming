# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
options = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
class Solution:
    def letterCombinations(self, digits):
        
        if len(digits) == 0:
            return []
        
        def helper(i):
            
            if i == len(digits)-1:
                return options[digits[i]]
            
            a = []
            
            remaining = helper(i+1)
            chars = options[digits[i]]
            for ch in chars:
                for i in range(len(remaining)):
                    a.append(ch + remaining[i])
                
            return a
        
        z = helper(0)
        print(z)
        return z
        
    
