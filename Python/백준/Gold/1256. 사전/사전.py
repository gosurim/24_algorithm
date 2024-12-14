import sys
input=sys.stdin.readline
n,m,k=map(int, input().split())
d=[[0 for _ in range(202)] for _ in range(202)]

for i in range(201): # 배열 초기화
    for j in range(i+1):
        if j==0 or j==i:
            d[i][j]=1
        else:
            d[i][j]=d[i-1][j-1]+d[i-1][j]
            if d[i][j]>1000000000:
                d[i][j]=1000000001

if d[n+m][m]<k: # 주어진 자릿수로 만들 수 없는 수
    print(-1)
else:
    while not (n==0 and m==0):
        if d[n-1+m][m] >=k:
            print("a", end="")
            n-=1
        else:
            print("z", end="")
            k-=d[n-1+m][m]
            m-=1

