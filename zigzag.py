import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==1:
            return s
        if numRows==1:
            numCols=len(s)
        else:
            k = len(s)/(2*numRows-2)
            numCols = numRows + k*(numRows-1)
        a = np.chararray((numRows,numCols))#[[""] * 3 for i in range(3)]
        matrix = np.zeros((numRows,numCols))
        a[:]=''
        
        i = 0 
        j = 0
        flag = 0 
        count = 0
        
        print(numRows,numCols)
        while count< len(s):
            
            matrix[i,j]=1
            # print(i,j)
            a[i,j]=s[count]
            
            if flag ==1:
                j = j+1
                i = i -1
            
            if flag ==0:
                i = i+1
                
            if i==0:
                flag = 0
            
            if i==numRows-1:
                flag =1
                
            count +=1
        s = [''.join(row) for row in a]
        a = ""
        for i in range(len(s)):
            a = a+s[i]+""
            

        return a
        
