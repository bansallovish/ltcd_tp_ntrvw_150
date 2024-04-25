class Solution(object):
    dp = [-1]*1001
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 or n==2:
            return 1
        else :
            return self.fib(n-1) + self.fib(n-2)
    
    def nthfib(self,n):
        if n==0:
            return 0
        elif n ==1 or n==2:
            return 1
        elif self.dp[n]!=-1:
            return self.dp[n]
        ans =  self.nthfib(n-1) + self.nthfib(n-2)
        self.dp[n] = ans
        return ans

        

obj1 = Solution()
print(obj1.fib(5))
print(obj1.nthfib(50))