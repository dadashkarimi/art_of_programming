class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        final_string=""
        
        while num >= 1000:
            final_string += "M"
            num -= 1000
            
        while num >= 500:
            final_string += "D"
            num -= 500
            
        while num >= 100:
            final_string += "C"
            num -= 100
            
        while num >= 50:
            final_string += "L"
            num -= 50
            
        while num >= 10:
            final_string += "X"
            num -= 10
            
        while num >= 5:
            final_string += "V"
            num -= 5
            
        while num >= 1:
            final_string += "I"
            num -= 1


        final_string=final_string.replace("DCCCC","CM").replace("CCCC","CD")
        final_string=final_string.replace("LXXXX","XC").replace("XXXX","XL")
        final_string = final_string.replace("VIIII","IX").replace("IIII","IV")
        
        return final_string
        
        
