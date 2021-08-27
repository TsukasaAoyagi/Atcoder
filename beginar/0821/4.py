import math

n,m = map(int,input().split())

a = list(map(int,input().split()))

ans = []


for i in range(len(a)):
    for j in range(1,m):
        if math.gcd(a[i],j)==1:
            ans.append(j)

ans = sorted(ans)

ans=list(set(ans))

print(ans)




""" for i in len(ans):
    print(ans[i]) """




