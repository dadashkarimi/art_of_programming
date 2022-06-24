class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        k=10
        rem = x % k
        num = 1
        n = 1
        x1 = x
        x = abs(x)
        print(x)
        while rem != x:
            k = 10*k
            rem = x%k
            n+=1
            
        k=10
        rem = x%k
        sum_=0
        
        for i in range(n):
            sum_=sum_+rem*pow(10,(n-i-1))/(pow(10,i))        
            k=10*k
            rem =x%k-x%(k/10)
        if x1 < 0:
            sum_ = -1*sum_
        if sum_< -pow(2,31) or sum_> pow(2,31)-1:
            return 0
        return sum_
