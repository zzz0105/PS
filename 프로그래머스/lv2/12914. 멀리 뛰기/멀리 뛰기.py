def solution(n):
    dp = [0]*(max(n,2)+1)
    dp[1], dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%1234567