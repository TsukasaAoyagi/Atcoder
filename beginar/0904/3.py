N = int(input())

p = list(map(int, input().split()))




ans = list(range(N))



for i in range(N):
    ans[p[i]-1]= i+1

print(' '.join(map(str,ans)))
