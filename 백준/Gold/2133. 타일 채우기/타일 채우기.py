import sys
N=int(sys.stdin.readline())
dp=[0]*(N+1)
if N%2==0:
    dp[2]=3
    for i in range(4,N+1,2):
        for j in range(2,i-2,2):
            dp[i]+=dp[j]*2
        dp[i]+=dp[i-2]*3+2
print(dp[N])