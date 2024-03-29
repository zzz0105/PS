n = int(input())
dp = [float('inf')]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(1,1+n):
    for j in range(1,int(i**0.5)+1):
        dp[i] = min(dp[i],dp[i-j*j]+1)
print(dp[n])