'''
Given a M x N matrix, calculate maximum sum submatrix of size k x k in a given M x
N matrix in O(M*N) time. Here, 0 < k < M, N.
For example, consider below 5 x 5 matrix
[ 3 -4 6 -5 1 ]
[ 1 -2 8 -4 -2 ]
[ 3 -8 9 3 1 ]
[ -7 3 4 2 7 ]
[ -3 7 -5 7 -6 ]
If k = 2, maximum sum k x k sub-matrix is
[ 9 3 ]
[ 4 2 ]
If k = 3, maximum sum k x k sub-matrix is
[ 8 -4 -2 ]
[ 9 3 1 ]
[ 4 2 7 ]
'''
def maxSumSquareSubMatrix(mat,N,M,K):
    dp = []
    for i in range(M):
        dp.append([0]*N)
    dp[0][0] = mat[0][0]
    for i in range(M):
        for j in range(N):
            if(i==0 and j!=0):
                dp[i][j] = dp[i][j-1] + mat[i][j]
            elif(j==0 and i!=0):
                dp[i][j] = dp[i-1][j] + mat[i][j]
            elif(i!=0 and j!=0):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] + mat[i][j] - dp[i-1][j-1]
    maxi = -1234567890
    for i in range(K-1,M):
        for j in range(K-1,N):
            if(i-K<0 and j-K<0):
                ans = dp[i][j]
            elif(i-K<0):
                ans = dp[i][j] - dp[i][j-K] 
            elif(j-K<0):
                ans = dp[i][j] - dp[i-K][j] 
            else:
                ans = dp[i][j] - dp[i][j-K] - dp[i-K][j] + dp[i-K][j-K]
            if(ans>maxi):
                maxi = ans
                ind_i = i-(K-1)
                ind_j = j-(K-1)
    for i in range(ind_i,ind_i+K):
        for j in range(ind_j,ind_j+K):
            print(mat[i][j],end=" ")
        print()
M,N,K = map(int,input().split(" "))
mat = []
for i in range(M):
    mat.append(list(map(int,input().split(" "))))
maxSumSquareSubMatrix(mat,M,N,K)