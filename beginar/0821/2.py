n = int(input())

k=0
ans = []
while 2**k<=n:
    ans.append(k)
    k+=1

print(max(ans))




