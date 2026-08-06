class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def MultiplyDigit(num):
            m=1
            while m>0 and num>0:
                m*=num%10
                num//=10
            return m
        for i in range(n,101):
            if MultiplyDigit(i) % t == 0:
                return i
        return n
