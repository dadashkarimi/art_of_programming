class Solution(object):
        def myAtoi(self, s):
        # Remove any additional spaces before the given string
        s = s.lstrip()
        
        # If string is empty return 0
        if len(s) == 0:
            return 0

        # String index from where the processing should start
        start = 0
        
        # Handling numbers with +/- sign
        sign_multiplier = 1
        if s[0] == '-': # Handling for negative sign numbers
            sign_multiplier = -1
            start = 1
        elif s[0] == '+': # Handling for signed positive sign number
            start = 1

        result = 0

        index = start
        print(ord("5"),ord("0"),"ff")
        while index < len(s):
            # Handling for non numeric values
            if not('0' <= s[index] <= '9'):
                return result * sign_multiplier

            # Calculate the result for current iteration
            result = result * 10 + ord(s[index]) - ord('0')

            # Check if result exceeds MinInt32 or MaxInt32
            min_int_32 = 2 ** 31
            if result * sign_multiplier <= -min_int_32:
                return -min_int_32
            elif result * sign_multiplier >= min_int_32-1:
                return min_int_32-1
            index+=1

        return result * sign_multiplier
    
# class Solution(object):
#     def myAtoi(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         negative = 0
#         numeric = 0
#         ss =s 
#         start = 0
#         middle = 0
#         sign = 0
        
#         if s in ["","+","-"]:
#             return 0
        
#         if s[0] not in [" ","-","+"] and not s[0].isnumeric():
#             return 0
        
#         for i in range(len(s)):

#             if sign and s[i] in ["-","+"]:
#                 return 0 
            
#             if numeric and s[i] ==" ":
#                 end = i
#                 ss = s[start:end]
                
#                 break
                
#             if s[i] == " ":
#                 continue
                
#             if not numeric and s[i].isnumeric():
#                 start =i
#                 numeric = 1
                

                
                
#             if s[i]==".":
#                 middle = i
                
#             if numeric and (not s[i].isnumeric() or i==len(s)-1) and not s[i]==".":
#                 end = i+1
#                 ss = s[start:end]
#                 break

#             if s[i]=="+":
#                 sign = 1
#                 numeric = 1
#                 start = i+1
                
#             if s[i]=="-": # negative
#                 sign = 1
#                 numeric = 1
#                 negative = 1
#                 start = i+1
                

#         # print(middle,ss[start:middle],)
#         print(ss)
#         if middle:
#             ss = ss[start:middle]+ss[middle+1:end]
#             ss = int(ss)/float(pow(10,len(s)-middle-1))
#             ss = int(ss)
#         else:
#             ss = int(ss)
        
#         print(ss) 
#         # ss = int(ss)
        
#         if negative:
#             ss = -1 * ss
            
#         if ss > pow(2,31):
#             print(ss)
#             print("yes")
#             return pow(2,31)-1
        
#         if ss < -1*pow(2,31)-1:
#             return -1*pow(2,31)
        
#         print(ss) 
#         return ss
