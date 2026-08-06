class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def DigitMultiply(num):
            m=1
            while m>0 and num>0:
                m*=num%10
                num//=10
            return m
        for i in range(n,101):
            if DigitMultiply(i) % t==0:
                return i
        return n