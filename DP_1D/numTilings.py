class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp2 = [0] * (n + 1)

        dp[0], dp[1], dp[2] = 1, 1, 2
        dp2[0], dp2[1], dp2[2] = 0, 0, 1

        for i in range(3, n + 1):
            dp2[i] = (dp2[i - 1] + dp[i - 2]) % MOD
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp2[i - 1]) % MOD

        return dp[n]
        